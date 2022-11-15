# Тесты к конвертеру из csv в json
```python
import unittest

from csv_to_json_manual import *

class TestConverter(unittest.TestCase):
 
    def test_convert_row_to_pretty_json(self):
        keys = ['id', 'name', 'birth', 'salary', 'department']
        row = '1,Alex,1990,100000,5'
        self.assertEqual(convert_row_to_pretty_json(keys, row), '{"id": 1, "name": Alex, "birth": 1990, "salary": 100000, "department": 5}')
        
    def test_convert_row_to_pretty_json_missed_value(self):
        keys = ['id', 'name', 'birth', 'salary', 'department']
        row = '1,,1990,100000,5'
        self.assertEqual(convert_row_to_pretty_json(keys, row), '{"id": 1, "name": , "birth": 1990, "salary": 100000, "department": 5}')
        
    def test_convert_row_to_pretty_json_wrong_order(self):
        keys = ['name', 'id', 'birth', 'salary', 'department']
        row = 'Alex,1,1990,100000,5'
        self.assertEqual(convert_row_to_pretty_json(keys, row), '{"id": 1, "name": Alex, "birth": 1990, "salary": 100000, "department": 5}')
        
if __name__ == "__main__":
    unittest.main()
```
