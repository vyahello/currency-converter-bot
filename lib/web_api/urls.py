from abc import ABC, abstractmethod
from typing import Any


class Url(ABC):
    """Represent the abstraction of url."""

    @abstractmethod
    def compose(self) -> str:
        pass


class HttpsUrlOf(Url):
    """Gather url components together."""

    def __init__(self, *url_elements: Any) -> None:
        self._url = url_elements

    def compose(self) -> str:
        return f"https://{''.join(map(str, self._url))}"
