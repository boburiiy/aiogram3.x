from aiogram.filters import CommandStart
from .handlers.default import start_handler
from .handlers.callbacks.callback_handler import callback_handler
from .handlers.errors.default_error_handler import err_handler
from config.setups import rout
routes = [
    rout(start_handler, CommandStart()),
]

callback_routes = [
    rout(callback_handler)
]
