from aiogram.dispatcher.event.telegram import TelegramEventObserver
from typing import Callable, Any, Union
from aiogram.types import BotCommand
from aiogram.filters import CommandStart
from aiogram import Bot, Dispatcher
import logging

import sys


def rout(handler: Callable, *filter: Callable[..., Any]):
    return {
        "handler": handler,
        "filter": filter
    }


async def notify_admins(bot: Bot, admins: list):
    for admin in admins:
        await bot.send_message(admin, "bot started to work 👋🏿")


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='#%(levelname)s %(asctime)s %(process)d %(filename)s:%(lineno)d %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        stream=sys.stdout
    )


async def setup_commands(bot: Bot, bot_commands: dict):
    await bot.set_my_commands(
        [
            BotCommand(command=cmd, description=desc) for cmd, desc in bot_commands.items()
        ]
    )


def setup_handlers(dp: Dispatcher, handlers: list[dict]):
    for handler in handlers:
        print(handler)
        # dp.message.register(handler["handler"], *handler["filter"])
