from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand
from environs import Env
import logging
import sys

env = Env()
TOKEN = env.str('TOKEN')
ADMINS = env.str('ADMINS')

bot_commands = {
    'start': "restart the bot",
    'help': "get some help"
}

dp = Dispatcher()
bot = Bot(TOKEN)


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='#%(levelname)s %(asctime)s %(process)d %(filename)s:%(lineno)d %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        stream=sys.stdout
    )


async def setup_start(bot: Bot = bot, admins: list = ADMINS):
    for admin in ADMINS:
        await bot.send_message(chat_id=admin, text=f'hi admin {admin} bot started to work') if admin else print("admin not found")


async def setup_commands():
    await bot.set_my_commands(
        [
            BotCommand(command=cmd, description=desc) for cmd, desc in bot_commands.items()
        ]
    )


def setup_routers(p_to_r_p):
    """
    p_to_r_p = paath to routers package
    """
