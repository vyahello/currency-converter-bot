from abc import ABC, abstractmethod


class Currency(ABC):
    """Abstract interface for a currency."""

    @abstractmethod
    def from_target(self) -> str:
        pass

    @abstractmethod
    def to_target(self) -> str:
        pass


class CurrencyPair(Currency):
    """Currency pair."""

    def __init__(self, source: str) -> None:
        self._source = source

    def from_target(self) -> str:
        return self._source.split()[0]

    def to_target(self) -> str:
        return self._source.split()[1]
