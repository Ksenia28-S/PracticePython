import unittest

from csv_to_json_manual import ManualCsvConverter

class TestManualCsvConverter(unittest.TestCase):
    
    def test_to_json_valid_input(self):
        my_test1 = ManualCsvConverter(['id,name,salary\n','2,Alex,200000\n'])
        self.assertEqual(my_test1.to_json(), '[{ "id": 2,"name": Alex,"salary": 200000 }]')
        
    def test_to_json_missing_value(self):
        my_test2 = ManualCsvConverter(['id,name,salary\n','2,,200000\n'])
        self.assertEqual(my_test2.to_json(), '[{ "id": 2,"name": null,"salary": 200000 }]')
        
    def test_to_json_only_column_names(self):
        my_test3 = ManualCsvConverter(['id,name,salary'])
        with self.assertRaises(AssertionError):
            my_test3.to_json()

    def test_to_json_wrong_value_count(self):
        my_test4 = ManualCsvConverter(['id,name,salary\n','2'])
        with self.assertRaises(AssertionError):
            my_test4.to_json()
            
if __name__== "__main__":
    unittest.main()
