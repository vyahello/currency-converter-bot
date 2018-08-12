from lib.currency.currencies import SafeSource, Currency


def test_safe_currency(safe_currency: SafeSource) -> None:
    assert safe_currency.match()


def test_currency_pair_match(currency_pair: Currency) -> None:
    assert currency_pair.match()


def test_currency_pair_amount(currency_pair: Currency) -> None:
    assert currency_pair.amount() == 100


def test_currency_pair_from_target(currency_pair: Currency) -> None:
    assert currency_pair.from_target() == 'usd'


def test_currency_pair_to_target(currency_pair: Currency) -> None:
    assert currency_pair.to_target() == 'eur'
