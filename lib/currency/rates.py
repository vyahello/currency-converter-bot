from abc import abstractmethod, ABC
from lib.currency.currencies import Currency
from lib.web_api.requests import Request, SafeBotRequest
from lib.web_api.urls import HttpsUrlOf


class Rate(ABC):
    """Abstract interface for a rate."""

    @abstractmethod
    def value(self) -> float:
        pass


class CurrencyRate(Rate):
    """Currency rate interface."""

    def __init__(self, currency: Currency) -> None:
        self._currency: Currency = currency
        self._request: Request = SafeBotRequest(HttpsUrlOf(
            'free.currencyconverterapi.com/api/v6/convert?q=',
            self._currency.from_target(), '_', self._currency.to_target(), '&compact=ultra'))

    def value(self) -> float:
        return self._request.get().json().get('{}_{}'.format(self._currency.from_target(),
                                                             self._currency.to_target()).upper())
