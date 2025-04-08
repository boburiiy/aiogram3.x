from dispatcher.config import dp
from dispatcher.handlers.start import start_handler
from aiogram.filters import CommandStart
from .setups import rout

routes = [
    rout(start_handler, CommandStart)
]
