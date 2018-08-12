from abc import abstractmethod, ABC
from lib.currency.currencies import Currency, CurrencyPair
from lib.currency.rates import Rate, CurrencyRate


class Converter(ABC):
    """Abstract interface for a converter."""

    @abstractmethod
    def value(self) -> str:
        pass


class CurrencyConverter(Converter):
    """Currency converter."""

    def __init__(self, source: str) -> None:
        self._currency: Currency = CurrencyPair(source)

    def value(self) -> str:
        if self._currency.match():
            rate: Rate = CurrencyRate(self._currency)
            return "{request}\n" \
                   "Initial: 1 {frm} = {initial} {to}\n" \
                   "Result: {amount} {frm} = {result} {to}".format(request=self._currency,
                                                                   amount=self._currency.amount(),
                                                                   initial=rate.value(),
                                                                   frm=self._currency.from_target(),
                                                                   result=self._currency.amount() * rate.value(),
                                                                   to=self._currency.to_target())
        return "Please use next pattern: <Amount> <from currency> to <to currency>\n" \
               "Example: 100 usd to eur"
