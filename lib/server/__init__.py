from typing import Tuple
from lib.server.core import Server, WebServer

SERVER: Server = WebServer()
WELCOME_MESSAGE: str = '<h1>Converter currency bot server powered by flask micro-web framework.' \
                       ' Core is written by V.Yahello</h1>'
METHODS: Tuple[str, ...] = ('POST', 'GET')
POST = 'POST'

from . import routes
