import unittest
from hour_income import *


class TestHourIncome(unittest.TestCase):

    def test(self):
        Income = HourIncome()
        result = Income.get_hour_income('{ "year": 2016, "month": "JULY", "salary": 1000000 }')
        var1 = '{"year": 2016, "month": "JULY", "salary": 1000000, "hour_income": 5434.78}'
        var2 = '{"year": 2016, "month": "JULY", "salary": 1000000, "hour_income": 5952.38}'
        var3 = '{"year": 2016, "month": "JULY", "salary": 1000000, "hour_income": 5681.82}'
        var4 = '{"year": 2016, "month": "JULY", "salary": 1000000, "hour_income": 6250.0}'
        self.assertTrue(result == var1 or result == var2 or result == var3 or result == var4)

if __name__ == "__main__":
    unittest.main()       