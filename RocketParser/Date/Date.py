try:
    from RocketParser.Regex.Regex import Regex
except ImportError:
    from Regex.Regex import Regex


class Date:
    defaultDateRegexPattern = r"(\d{4})\s(\w+).+"

    def __init__(self):
        self.month = ''
        self.year = ''
        self.string = ''
        self.regexPattern = ''

    def setFullDate(self, string):
        self.string = string

    def getFullDate(self):
        return self.string

    def setRegexPattern(self, pattern):
        self.regexPattern = pattern

    def getRegexPattern(self):
        return self.regexPattern

    @staticmethod
    def isDateFormat(date, pattern: str) -> bool:
        return Regex(date).match(pattern)

    def build(self) -> list:
        extracted_date = Regex(self.getFullDate())
        extracted_date.match(self.getRegexPattern())
        return extracted_date
