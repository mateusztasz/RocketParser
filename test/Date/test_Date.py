from unittest import TestCase
from RocketParser.Date.Date import  Date


class TestDate(TestCase):
    def test_isDateFormat_01(self):
        pattern = Date.defaultDateRegexPattern
        expression = Date.isDateFormat('2013 Jun 12:30', pattern)
        self.assertTrue(expression)

    def test_isDateFormat_02(self):
        pattern = Date.defaultDateRegexPattern
        expression = Date.isDateFormat('1111 January 05 50', pattern)
        self.assertTrue(expression)

    def test_isDateFormat_03(self):
        pattern = Date.defaultDateRegexPattern
        expression = Date.isDateFormat('1956 F 07-30', pattern)
        self.assertTrue(expression)

    def test_isDateFormat_04(self):
        pattern = Date.defaultDateRegexPattern
        expression = Date.isDateFormat('123 Feb 07:30', pattern)
        self.assertFalse(expression)

    def test_isDateFormat_05(self):
        pattern = Date.defaultDateRegexPattern
        expression = Date.isDateFormat('12357 AUG 23:30 pm', pattern)
        self.assertFalse(expression)
