from aiogram import Bot,Dispatcher
from aiogram.client.default import DefaultBotProperties
from environs import env
from .keyboard_builder import kb_builder
from .keyboards import simple_kb
from .setups import (
    notify_admins,
    setup_logging,
    setup_commands,
    setup_handlers,
    setup_callback_handlers
)

env.read_env()
ADMINS = env.list('ADMINS')
TOKEN = env.str('TOKEN')

dp = Dispatcher()
bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode='HTML'))

keyboards = kb_builder("kbb1")
keyboards.Create(simple_kb, "simple_kb")
bot_commands = {
    'start': "restart the bot",
    'help': "get some help"
}
