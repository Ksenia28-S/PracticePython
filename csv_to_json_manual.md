# Конвертер csv в json вручную

```python
def read_data_to_list(file_name):
    file = open(file_name)
    content = file.readlines()
    file.close()
    return content  


def write_data(file_name, data):
    file = open(file_name, 'w')
    file.write(data)
    file.close()
    
    
def prepare_data(data):
    title = data.pop(0).strip().split(',')
    return title, data


def convert_row_to_pretty_json(keys, row):
    values = row.strip().split(',')
    dictionary = dict(zip(keys, values))
    template = """{{"id": {}, "name": {}, "birth": {}, "salary": {}, "department": {}}}"""
    return template.format(*[dictionary.get(k) for k in ['id', 'name', 'birth', 'salary', 'department']])

def convert_csv_to_json(data):
    title, data = prepare_data(data)        
    result = [convert_row_to_pretty_json(title, row) for row in data]  
    return str(result)
           
    
def main():
    data = read_data_to_list("input.csv")
    result = convert_csv_to_json(data)
    write_data("output.json", result)


if __name__ == "__main__":
    main()
```
