from Date.Date import Date
from typing import List, Dict
import collections
import json


class RocketParser:
    def __init__(self):
        self.date = Date()
        self.success = None
        self.solution = dict()

    def group_by(self, stream, field, filter=None):
        self.omitLines(stream, lines=2)

        for line in stream:
            cell_in_line = line.split('   ')
            cell_in_line = [elem.strip() for elem in cell_in_line if elem]

            if self.isCellLineFormatCorrect(cell_in_line):
                self.date.setFullDate(cell_in_line[1])
                self.setSuccess(cell_in_line[-2])

                self.date.setRegexPattern(Date.defaultDateRegexPattern)
                launch_date = self.date.build()

                self.aggregateCount(launch_date, field, filter)

        res = collections.OrderedDict(sorted(self.solution.items()))
        return json.dumps(res, indent=4, sort_keys=True)

    def omitLines(self, stream, lines):
        for __ in range(0, lines):
            stream.readline()

    @staticmethod
    def isCellLineFormatCorrect(data: List[str]) -> bool:
        if Date.isDateFormat(data[1], pattern=Date.defaultDateRegexPattern):
            return True
        else:
            return False

    def setSuccess(self, successLiteral: str) -> bool:
        if successLiteral is 'S':
            self.success = True
        elif successLiteral is 'F':
            self.success = False

    def aggregateCount(self, launch_date: list, field: str, filter: bool):

        if field is 'year':
            aggregationField = launch_date.group(1)
        elif field is 'month':
            aggregationField = launch_date.group(2)

        if filter is None or \
                        self.success is filter:
            try:
                self.solution[aggregationField] = (self.solution[aggregationField] + 1)
            except LookupError:
                self.solution[aggregationField] = 1


if __name__ == '__main__':
    parser = RocketParser()
    result_dict = parser.group_by(open("../launchlog.txt"), 'month', filter=None)
    print(result_dict)
