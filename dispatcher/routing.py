from aiogram import F
from aiogram.filters import CommandStart
from handlers.start import start_handler
from handlers.echo import echo_handler
from handlers.greet_user import greet_new_user, welcome
from handlers.callbacks.callback_handler import callback_handler
from config.setups import rout
from utils.FSM.states import Form
routes = [
    rout(start_handler, CommandStart()),
    rout(greet_new_user, Form.name),
    rout(welcome, Form.id)
]

callback_routes = [
    rout(callback_handler)
]
