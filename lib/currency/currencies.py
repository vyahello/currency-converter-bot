from abc import ABC, abstractmethod
from typing import List
import functools


class Currency(ABC):
    """Abstract interface for a currency."""

    @abstractmethod
    def match(self) -> bool:
        pass

    @abstractmethod
    def amount(self) -> int:
        pass

    @abstractmethod
    def from_target(self) -> str:
        pass

    @abstractmethod
    def to_target(self) -> str:
        pass


class SafeSource(ABC):
    """Abstract interface for safe validator."""

    @abstractmethod
    def match(self) -> List[str]:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class SafeCurrencyPair(SafeSource):
    """Safe converter currency."""

    def __init__(self, source: str) -> None:
        self._source: str = source

    def match(self) -> List[str]:
        source: List[str] = self._source.split()
        return source if len(source) == 4 else None

    def __str__(self) -> str:
        return f"Request: convert {self._source}"


class CurrencyPair(Currency):
    """Concrete converter currency parser.
    Sample: ``100 usd to eur``."""

    def __init__(self, source: str) -> None:
        self._source: SafeSource = SafeCurrencyPair(source)

    @functools.lru_cache()
    def match(self) -> List[str]:
        return self._source.match()

    def amount(self) -> int:
        return int(self.match()[0])

    def from_target(self) -> str:
        return self.match()[1]

    def to_target(self) -> str:
        return self.match()[3]

    def __str__(self) -> str:
        return str(self._source)
