import os

from csv_to_json_manual import ManualCsvConverter

def read_data_to_list(file_name):
    if not os.path.exists(file_name):
        print('file',file_name, 'does not exist') 
    else:
        file = open(file_name)
        content = file.readlines()
        file.close()
        if not content:
            print('file',file_name, 'is empty')
        return content


def write_data(file_name, data):
    file = open(file_name, 'w')
    file.write(data)
    file.close()
        
        
def main():
    data = read_data_to_list("input.csv")
    if data:
        converter = ManualCsvConverter(data)
        result = converter.to_json()
        write_data("output.json", result)
    
    
if __name__ == "__main__":
    main()
