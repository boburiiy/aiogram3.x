from aiogram.client.default import DefaultBotProperties
from aiogram import Dispatcher, Bot
import environs
env = environs.Env()
dp = Dispatcher()

commands = {
    '/start': "Start the bot",
    '/help': 'Get help',

}

router_paths = [
    'handlers'
]

TOKEN = env.str("TOKEN")
ADMINS = env.list('ADMINS')

bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode='HTML'))


routers = [
    'handlers'
]
