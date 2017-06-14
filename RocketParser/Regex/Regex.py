import re


class Regex:
    def __init__(self, matchstring):
        self.match_string = matchstring
        #self.rematch = None

    def match(self, regexp):
        self.rematch = re.match(regexp, self.match_string)
        return bool(self.rematch)

    def group(self, i):
        return self.rematch.group(i)
