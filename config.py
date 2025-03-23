from aiogram.client.default import DefaultBotProperties
from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand
import environs

env = environs.Env()

TOKEN = env.str("TOKEN")
ADMINS = env.list('ADMINS')

dp = Dispatcher()
env = environs.Env()
bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode='HTML'))


async def notify_admins(message: str, bot: Bot, ADMINS: list = ADMINS):
    for admin in ADMINS:
        if admin:
            await bot.send_message(admin, message)


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Start the bot"),
        BotCommand(command="/help", description="Get help"),
        BotCommand(command="/info", description="Get information"),
    ]
    await bot.set_my_commands(commands)
