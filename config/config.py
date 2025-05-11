from aiogram.client.default import DefaultBotProperties
from .middlewares import middlewares_list
from aiogram import Bot, Dispatcher
from router.base_router import r1
from dotenv import dotenv_values
env = dotenv_values()
from .setups import (
    setup_routers,
    notify_admins,
    setup_logging,
    setup_commands,
    setup_handlers,
    setup_middlewares,
    setup_error_handlers,
    setup_callback_handlers,
    setup_callback__middlewares
)
__all__ = [
    'setup_routers',
    'setup_callback__middlewares',
    'setup_callback_handlers',
    'setup_error_handlers',
    'setup_middlewares',
    'setup_commands',
    'setup_handlers',
    'setup_logging',
    'notify_admins',
    'middlewares_list',
    'bot_commands',
    'routers',
    'ADMINS',
    'bot',
    'dp',
]
 # reading enviroment variables

ADMINS = env.get('ADMINS').split()  # defining admins
TOKEN = env.get('TOKEN')  # defining bot token
dp = Dispatcher()
bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode='HTML'))

routers = [
    # including routers
    r1
]

bot_commands = {
    # Default bot commands
    'start': "restart the bot",
    'help': "get some help"
}
