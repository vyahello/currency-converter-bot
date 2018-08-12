from abc import ABC, abstractmethod
from typing import Dict, Any, Callable
from lib.bot import API_KEY
from lib.currency.converters import Converter, CurrencyConverter
from lib.server import requests
from lib.web_api.requests import SafeBotRequest, Request
from lib.web_api.responses import Response
from lib.web_api.urls import HttpsUrlOf


class Answer(ABC):
    """Abstraction for a answer."""

    @abstractmethod
    def chat_id(self) -> int:
        pass

    @abstractmethod
    def message(self) -> str:
        pass


class Message(ABC):
    """Abstraction for a message."""

    @abstractmethod
    def send(self) -> Dict[Any, Any]:
        pass


class BotAnswer(Answer):
    """An answer from a bot."""

    def __init__(self, request: requests.Request) -> None:

        def _req() -> Dict[Any, Any]:
            return request.dct().get('message')

        self._req: Callable[..., Dict[Any, Any]] = _req

    def chat_id(self) -> int:
        return self._req().get('chat').get('id')

    def message(self) -> str:
        return self._req().get('text')


class BotMessage(Message):
    """A message of a bot."""

    def __init__(self, chat_id: int, movie: str) -> None:
        self._chat_id: int = chat_id
        self._converter: Converter = CurrencyConverter(movie)
        self._request: Request = SafeBotRequest(HttpsUrlOf('api.telegram.org/bot', API_KEY, '/sendMessage'))

    def send(self) -> Response:
        return self._request.post({'chat_id': self._chat_id, 'text': self._converter.value()})
