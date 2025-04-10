from aiogram.filters import CommandStart
from magic_filter import F
from .config import dp
from .handlers.start import start_handler
from .handlers.echo import echo_handler
from .handlers.callback_handler import callback_handler
from .setups import rout
from aiogram.filters.callback_data import CallbackData

routes = [
    rout(start_handler, CommandStart()),
    rout(echo_handler),
]

callback_routes = [
    rout(callback_handler, CallbackData.filter(F.data == 'col 1 row 1')),
    rout(callback_handler, CallbackData.filter(F.data == 'new_button_callback')),
]
