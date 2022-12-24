class StrategyDeal:
    def __init__(self, bank, entry, targets, close):
        self.bank = bank
        self.entry = entry
        self.target = target
        self.close = close
        
    def get_targets(self):
        # вернуть список таргетов в виде числовых значений float [21.5, 22.8, 23.5]
        pass 

    def get_target_percents(self):
        # вернуть список процентов, как в примере, округленные до 3 знака [6.912, 13.376, 16.857]
        pass

    def get_target_banks(self):
        # список значений банков, если продавать активы по таргетам, как в пример, округленные до 3 знака [1069.12, 1133.764, 1168.573]
        pass

    def __str__(self):
        # текстовое представление сделки
        pass


def read_data(file_name):
    file = open("deal.txt")
    content = file.read()
    file.close()
    
def prepare_data(data):
    deals = content.split('-----')
    prep_data = [line.rstrip().split(',') for line in data]
    content = [i for i in prep_data if i != ['']]
    content = [line.strip().split('\n') for line in content]

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