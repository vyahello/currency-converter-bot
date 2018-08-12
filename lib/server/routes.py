from lib.bot.message import Answer, BotAnswer, BotMessage
from lib.server import Server, SERVER, METHODS, POST, WELCOME_MESSAGE
from lib.server.requests import ServerRequest, Request

_server: Server = SERVER


@_server.route('/', methods=METHODS)
def index():
    request: Request = ServerRequest()
    answer: Answer = BotAnswer(request)

    if request.method() == POST:
        BotMessage(answer.chat_id(), answer.message()).send()

    return WELCOME_MESSAGE
