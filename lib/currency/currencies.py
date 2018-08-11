from abc import ABC, abstractmethod


class Currency(ABC):
    """Abstract interface for a currency."""

    @abstractmethod
    def amount(self) -> int:
        pass

    @abstractmethod
    def from_target(self) -> str:
        pass

    @abstractmethod
    def to_target(self) -> str:
        pass


class CurrencyPair(Currency):
    """Concrete converter currency parser.
    Sample: ``100 usd to eur``."""

    def __init__(self, source: str) -> None:
        self._source: str = source

    def amount(self) -> int:
        return int(self._source.split()[0])

    def from_target(self) -> str:
        return self._source.split()[1]

    def to_target(self) -> str:
        return self._source.split()[3]
