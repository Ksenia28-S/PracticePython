class ManualCsvConverter:

    def __init__(self, csv_data):
        self.title = csv_data[0]
        self.values = csv_data[1:]
        

    def prepare_title(self):
        title = self.title.strip().split(',')
        return title
        

    def prepare_row_values(self):
        values = [row.strip().split(',') for row in self.values]
        for i in range(len(values)):
            for j in range(len(values[i])):
                if values[i][j] == '':
                    values[i][j] = 'null'
        return values


    def convert_row_to_json(self, data):
        formatted_values = ",".join([""""{}": {}""".format(key, value) for key, value in data.items()])
        pretty_line = """{{ {} }}""".format(formatted_values)
        return pretty_line


    def to_json(self):
        title = self.prepare_title()
        row_values = self.prepare_row_values()
        
        self.check_data(title, row_values)
        
        result = [self.convert_row_to_json(dict(zip(title, row))) for row in row_values]
        return "[{}]".format(",".join(result))
     
       
    def check_data(self, title, row_values):
        assert len(row_values) != 0, "No values in data"
        for row in row_values:
            assert len(title) == len(row), "Column count is not equals value count"
