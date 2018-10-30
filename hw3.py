# 1
def count(data):
    return sum(data[i][i] for i in range(len(data)))

# 2
def data_check(data):
    return sum(int(d)**2 for d in data if isinstance(d, int) or str.isnumeric(d))

# 3
import requests
def value_rate():
    a = []
    b = []
    r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    response = r.json()['Valute']
    for currency in response:
        b.append(response[currency]['Value'])
        a.append(list(response[currency].values()))
    listt = [a[i][4] for i in range(len(a)) if max(b) in a[i]]
    return listt

# 4
class Rate:
    def __init__(self, format, diff):
        self.format = format
        self.diff = diff

    def exchange_rates(self):

        r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return r.json()['Valute']

    def make_format(self, currency):

        response = self.exchange_rates()

        if currency in response:
            if self.diff == False:
                if self.format == 'full':
                    return response[currency]

                if self.format == 'value':
                    return response[currency]['Value']
                if self.format == 'name':
                    return response[currency]['Name']
            else:
                return (response[currency]['Value'] - response[currency]['Previous'])

        return 'Error'

    def eur(self):

        return self.make_format('EUR')

    def usd(self):

        return self.make_format('USD')

# 5
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[-1] + fib[-2])
    return sum(fib)

# 6
def dict_fromlist(list):
    dictionary = {list[0]:{list[1]:{list[2]:list[3]}}}
    return dictionary
