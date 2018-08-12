from abc import ABC, abstractmethod
from lib.bot import API_KEY
from lib.web_api.requests import Request, SafeBotRequest
from lib.web_api.urls import HttpsUrlOf


class Hook(ABC):
    """Abstract interface for a telegram hook."""

    @abstractmethod
    def set(self) -> None:
        pass

    @abstractmethod
    def delete(self) -> None:
        pass


class WebHook(Hook):
    """Webhook interface."""

    def __init__(self, url: str) -> None:
        self._set: Request = SafeBotRequest(HttpsUrlOf('api.telegram.org/bot', API_KEY, '/setWebhook?url=', url))
        self._delete: Request = SafeBotRequest(HttpsUrlOf('api.telegram.org/bot', API_KEY, '/deleteWebhook'))

    def set(self) -> None:
        self._set.get()

    def delete(self) -> None:
        self._delete.get()
