try:
    from RocketParser.Date.Date import Date
    from RocketParser.ProgressBar.ProgressBar import ProgressBar
except ImportError:
    from Date.Date import Date
    from ProgressBar.ProgressBar import ProgressBar

import collections
from typing import List, Dict
import json
import os


class RocketParser:
    def __init__(self):
        self.date = Date()
        self.success = None
        self.solution = dict()
        self.progressBar = ProgressBar()

    def group_by(self, stream, field, filter=None) -> [json, Dict[str, int]]:
        self.omitLines(stream, lines=2)

        self.progressBar.setTotal(os.fstat(stream.fileno()).st_size)

        for line in iter(stream.readline, ''):

            # Update progress bar
            self.progressBar.setIteration(stream.tell())
            self.progressBar.print()

            # Divide line into list
            cell_in_line = line.split('   ')
            cell_in_line = [elem.strip() for elem in cell_in_line if elem]

            # Prepare and aggregate counter
            if self.isCellLineFormatCorrect(cell_in_line):
                self.date.setFullDate(cell_in_line[1])
                self.setSuccess(cell_in_line[-2])

                self.date.setRegexPattern(Date.defaultDateRegexPattern)
                launch_date = self.date.build()

                self.aggregateCount(launch_date, field, filter)

        stream.close()

        res = collections.OrderedDict(sorted(self.solution.items()))
        return [json.dumps(res, indent=4, sort_keys=True), res]

    def omitLines(self, stream, lines: int) -> None:
        for __ in range(0, lines):
            stream.readline()

    @staticmethod
    def isCellLineFormatCorrect(data: List[str]) -> bool:
        return Date.isDateFormat(data[1], pattern=Date.defaultDateRegexPattern)

    def setSuccess(self, successLiteral: str) -> bool:
        if successLiteral is 'S':
            self.success = True
        elif successLiteral is 'F':
            self.success = False

    def aggregateCount(self, launch_date: List[str], field: str, filter: bool):

        if field is 'year':
            aggregationField = launch_date.group(1)
        elif field is 'month':
            aggregationField = launch_date.group(2)

        if filter is None or self.success is filter:
            try:
                self.solution[aggregationField] = (self.solution[aggregationField] + 1)
            except LookupError:
                self.solution[aggregationField] = 1


if __name__ == '__main__':
    parser = RocketParser()
    result_dict = parser.group_by(open("../launchlog.txt"), 'year', filter=None)

    print("JSON format: ", result_dict[0])
    print("Python dictionary format: ", result_dict[1])
