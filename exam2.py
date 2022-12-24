class StrategyDeal:
    def __init__(self, data):
        self.bank = data[3]
        self.entry = data[0]
        self.target = data[1]
        self.close = data[2]
        
    def get_targets(self):
        return [float(x) for x in d.target.split(':')[1].split(',')]

    def get_target_percents(self, targets):
        return [round(((x / float(d.entry.split(':')[1])) - 1)*100, 3) for x in targets]

    def get_target_banks(self, targets):
        return [round(x* float(d.bank.split(':')[1]), 3) for x in targets]
        # список значений банков, если продавать активы по таргетам, как в пример, округленные до 3 знака [1069.12, 1133.764, 1168.573]

    def __str__(self):
        # текстовое представление сделки
        pass


def read_data(file_name):
    file = open("deal.txt")
    content = file.read()
    file.close()
    return content
    
def prepare_data(data):
    deals = content.split('-----')
    prep_data = [line.rstrip().split(',') for line in data]
    content = [i for i in prep_data if i != ['']]
    content = [line.strip().split('\n') for line in content]
    result = []
    for i in content:
        t = list(filter(lambda x: x != '', i))
        result.append(t)
    return result

def write_data(file_name, data):
    file = open(file_name, 'w')
    file.write(data)
    file.close()


def main():
    content = read_data('deals.txt')
    content_prepared = prepare_data(content)
    
    result = deal
    write_data('out.txt', result)


if __name__ == '__main__':    
    main() 