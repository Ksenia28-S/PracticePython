import csv 
import json 

def read_data(file_name):
    file = open(file_name)
    reader = csv.DictReader(file)
    return reader

def convert_csv_to_json(data):
    content = [row for row in data]
    content_final = json.dumps(content, indent=3)
    return content_final

def write_data(file_name, data):
    file = open(file_name, 'w')
    file.write(data)
    file.close()

def main():
    data = read_data("input.csv")
    result = convert_csv_to_json(data)
    write_data("output.json", result)

if __name__ == "__main__":
    main()
