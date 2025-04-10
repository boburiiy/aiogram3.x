from aiogram.dispatcher.event.telegram import TelegramEventObserver
from aiogram.types import BotCommand
from aiogram import Bot, Dispatcher, Router
from typing import Callable, Any, Union
import logging

import sys


def rout(handler: Callable, *filters: Callable[..., Any]):
    return {
        "handler": handler,
        "filters": list(filters)
    }


async def notify_admins(bot: Bot, admins: list):
    for admin in admins:
        await bot.send_message(admin, "bot started to work 👋🏿")
    await bot.session.close()


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


def setup_handlers(target: Dispatcher | Router, handlers: list[dict]):
    for handler in handlers:
        target.message.register(handler["handler"], *handler["filters"])


def setup_callback_handlers(target: Dispatcher | Router, handlers: list[dict]):
    for handler in handlers:
        target.callback_query.register(handler["handler"], *handler["filters"])
