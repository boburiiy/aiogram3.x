from aiogram import Dispatcher, Bot
from environs import Env
from .setups import setup_logging,\
    setup_commands,\
    notify_admins,\
    setup_handlers,\
    setup_callback_handlers

env = Env()
ADMINS = env.list('ADMINS')
TOKEN = env.str('TOKEN')
dp = Dispatcher()
bot = Bot(TOKEN)

keyboards = {
    # "name": 'keyboard'
}

bot_commands = {
    'start': "restart the bot",
    'help': "get some help"
}


def setup_routers(p_to_r_p):
    """
    p_to_r_p = paath to routers package
    """
