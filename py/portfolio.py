import functools
import operator
from bank import Bank
from money import Money


class Portfolio:
    def __init__(self):
        self.moneys: list[Money] = []

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def evaluate(self, bank: Bank, currency: str):
        total = 0
        for money in self.moneys:
            money = bank.convert(money, currency)
            total += money.amount
        return Money(total, currency)