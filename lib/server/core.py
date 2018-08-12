from abc import ABC, abstractmethod
from typing import Any, Callable, Iterable
from flask import Flask


class Server(ABC):
    """Represent abstraction for a server."""

    @abstractmethod
    def route(self, path: str, methods: Iterable[str]) -> Callable[..., Any]:
        pass

    @abstractmethod
    def run(self, host: str = None, port: int = None, debug: Any = None, **options: Any) -> None:
        pass


class WebServer(Server):
    """Represent web server."""

    def __init__(self, name: str = __name__) -> None:
        self._app: Flask = Flask(name)

    def route(self, path: str, methods: Iterable[str]) -> Callable[..., Any]:
        return self._app.route(path, methods=methods)

    def run(self, host: str = None, port: int = None, debug: Any = None, **options: Any) -> None:
        return self._app.run(host, port, debug, **options)
