from aiogram.filters import CommandStart
from .config import dp
from .handlers.start import start_handler
from .handlers.echo import echo_handler
from .setups import rout

routes = [
    rout(start_handler, CommandStart()),
    rout(echo_handler),
]
