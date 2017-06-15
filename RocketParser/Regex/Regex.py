import re


class Regex:
    def __init__(self, matchstring:str):
        self.match_string = matchstring
        # self.rematch = None

    def match(self, regexp: str) -> bool:
        self.rematch = re.match(regexp, self.match_string)
        return bool(self.rematch)

    def group(self, i) -> list:
        return self.rematch.group(i)
