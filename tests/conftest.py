import pytest
from lib.currency.currencies import SafeSource, Currency, SafeCurrencyPair, CurrencyPair


@pytest.fixture(scope='module')
def source() -> str:
    return '100 usd to eur'


@pytest.fixture(scope='module')
def safe_currency(source: str) -> SafeSource:
    return SafeCurrencyPair(source)


@pytest.fixture(scope='module')
def currency_pair(source: str) -> Currency:
    return CurrencyPair(source)
