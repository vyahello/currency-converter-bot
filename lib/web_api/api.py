from abc import ABC, abstractmethod
from typing import Dict, Any
import requests
from lib.web_api.responses import Response, BotResponse
from lib.web_api.urls import Url


class Session(ABC):
    """Abstract interfaces for API Session."""

    @abstractmethod
    def get(self) -> Response:
        pass

    @abstractmethod
    def post(self, data: Dict[Any, Any]) -> Response:
        pass


class BotSession(Session):
    """Provide interfaces for bot api session."""

    def __init__(self, url: Url) -> None:
        self._api: requests.Session = requests.Session()
        self._url = url

    def get(self) -> Response:
        return BotResponse(self._api.get(self._url.compose()))

    def post(self, data: Dict[Any, Any]) -> Response:
        return BotResponse(self._api.post(self._url.compose(), json=data))
