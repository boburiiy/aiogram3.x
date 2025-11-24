from aiogram.types import BotCommand, TelegramObject
from aiogram import Bot, Dispatcher, Router
from typing import Callable, Any, Awaitable, Union
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


async def setup_commands(bot: Bot, bot_commands: dict[str, str]):
    await bot.set_my_commands(
        [
            BotCommand(command=cmd, description=desc) for cmd, desc in bot_commands.items()
        ]
    )

target_type = Union[Dispatcher, Router]
handler_type = list[dict[Callable[..., Any], Any]]
middleware_type = list[TelegramObject]


def setup_handlers(target: target_type, handlers: handler_type):
    for handler in handlers:
        target.message.register(handler["handler"], *handler["filters"])


def setup_error_handlers(target: target_type, handler: Awaitable):
    target.error.register(handler)


def setup_callback_handlers(target: target_type, handlers: handler_type):
    for handler in handlers:
        target.callback_query.register(handler["handler"], *handler["filters"])


def setup_middlewares(target: target_type, midwrs: middleware_type):
    for midw in midwrs:
        target.message.middleware(midw)


def setup_callback__middlewares(target: target_type, midwrs: middleware_type):
    for midw in midwrs:
        target.callback_query.middleware(midw)


def setup_routers(dp: Dispatcher, routers: list[Router]):
    for router in routers:
        dp.include_router(router)
