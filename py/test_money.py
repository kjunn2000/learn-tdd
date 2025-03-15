import bank
from money import Money
from bank import Bank
from portfolio import Portfolio
from exceptions import CurrencyRateNotFoundException
import pytest


@pytest.fixture
def bank():
    bank = Bank()
    bank.add_rate("EUR", "USD", 1.092)
    return bank


class TestMoney:
    def test_multification(self):
        tenEuros = Money(10, "EUR")
        twentyEuros = Money(20, "EUR")

        assert twentyEuros == tenEuros.times(2)

    def test_division(self):
        originalMoney = Money(4002, "KRW")
        actualMoneyAfterDivision = originalMoney.divide(4)

        expectedMoneyAfterDivision = Money(1000.5, "KRW")

        assert expectedMoneyAfterDivision == actualMoneyAfterDivision

    def test_addition(self, bank):
        fiveDollars = Money(5, "USD")
        tenDollars = Money(10, "USD")
        fifteenDollars = Money(15, "USD")
        portfolio = Portfolio()

        portfolio.add(fiveDollars, tenDollars)

        assert fifteenDollars == portfolio.evaluate(bank, "USD")

    def test_evaluate_success(self, bank):
        fiveDollars = Money(5, "USD")
        tenEuros = Money(10, "EUR")
        fifteenDollars = Money(15.92, "USD")
        portfolio = Portfolio()

        portfolio.add(fiveDollars, tenEuros)

        assert fifteenDollars == portfolio.evaluate(bank, "USD")

    def test_evaluate_non_exist_currency(self, bank):
        fiveDollars = Money(5, "USD")
        tenEuros = Money(10, "EUR")
        tenWons = Money(10, "KRW")
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenEuros, tenWons)

        with pytest.raises(CurrencyRateNotFoundException):
            portfolio.evaluate(bank, "USD")

    def test_convert_non_exist_currency(self):
        bank = Bank()
        ten_euro = Money(10, "EUR")

        with pytest.raises(CurrencyRateNotFoundException):
            bank.convert(ten_euro, "USD")

    def test_convert_exist_currency(self):
        bank = Bank()
        bank.add_rate("EUR", "USD", 1.092)
        ten_euro = Money(10, "EUR")

        result = bank.convert(ten_euro, "USD")

        assert Money(10.92, "USD") == result
