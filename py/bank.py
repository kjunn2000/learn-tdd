from money import Money
from exceptions import CurrencyRateNotFoundException

class Bank:
    def __init__(self):
        self.rates = {}
        
    def add_rate(self, from_currency, to_currency, rate):
        self.rates[(from_currency, to_currency)] = rate
        
    def rate(self, from_currency, to_currency):
        if from_currency == to_currency:
            return 1
        elif (from_currency, to_currency) not in self.rates:
            raise CurrencyRateNotFoundException()
        return self.rates[(from_currency, to_currency)]
    
    def convert(self, money, to_currency):
        rate = self.rate(money.currency, to_currency)
        return Money(round(money.amount * rate, 2), to_currency)