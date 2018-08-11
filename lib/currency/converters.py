from abc import ABC, abstractmethod
from lib.currency.currencies import Currency, CurrencyPair
from lib.web_api.requests import Request, SafeBotRequest
from lib.web_api.urls import HttpsUrlOf


class Converter(ABC):
    """Abstract interface for a converter."""

    @abstractmethod
    def value(self) -> float:
        pass


class CurrencyConverter(Converter):
    """Currency converter."""

    def __init__(self, source: str) -> None:
        self._currency: Currency = CurrencyPair(source)
        self._request: Request = SafeBotRequest(HttpsUrlOf(
            'free.currencyconverterapi.com/api/v6/convert?q=',
            self._currency.from_target(), '_', self._currency.to_target(), '&compact=ultra'))

    def value(self) -> float:
        return self._request.get().json().get('{}_{}'.format(self._currency.from_target(),
                                                             self._currency.to_target()).upper())
