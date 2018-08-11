from abc import ABC, abstractmethod
from typing import Dict, Any, Callable
from lib.web_api.api import Session, BotSession
from lib.web_api.responses import Response, ResponseError
from lib.web_api.urls import Url


class Request(ABC):
    """The abstraction of a specific API request."""

    @abstractmethod
    def get(self) -> Response:
        pass

    @abstractmethod
    def post(self, data: Dict[Any, Any]) -> Response:
        pass


class BotRequest(Request):
    """Provide bot api requests methods. """

    def __init__(self, url: Url) -> None:
        self._session: Session = BotSession(url)

    def get(self) -> Response:
        return self._session.get()

    def post(self, data: Dict[Any, Any]) -> Response:
        return self._session.post(data)


class SafeBotRequest(Request):
    """Represent a safe request.
    Raise an error if specific status code is not presented.
    """

    def __init__(self, url: Url, success: int = 200) -> None:

        def _safe(res: Response) -> Response:
            code: int = res.status_code()
            if code != success:
                raise ResponseError(f'HTTP response error with {code} status code!!!')
            return res

        self._session: Session = BotSession(url)
        self._safe: Callable[[Response], Response] = _safe

    def get(self) -> Response:
        return self._safe(self._session.get())

    def post(self, data: Dict[Any, Any]) -> Response:
        return self._safe(self._session.post(data))
