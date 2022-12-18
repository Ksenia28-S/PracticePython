import json
from random import randint

class NumberWorkDays:

    def get_days(self):
        return randint(20, 23)

class HourIncome:
    
    def get_hour_income(self, input_json):
        json_object = json.loads(input_json)
        days_number = NumberWorkDays().get_days()
        hour_income = round(json_object['salary']/(days_number * 8), 2)
        json_object['hour_income'] = hour_income
        return json.dumps(json_object)

        