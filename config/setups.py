from aiogram.types import BotCommand, TelegramObject
from aiogram import Bot, Dispatcher, Router
from typing import Callable, Any, Awaitable
import logging
import sys


def rout(handler: Callable, *filters: Callable[..., Any]):
    """
    Helper to create a handler dict with its filters.

    Args:
        handler: The handler function.
        *filters: Optional filter callables.

    Returns:
        dict: Dictionary with 'handler' and 'filters' keys.
    """
    return {
        "handler": handler,
        "filters": list(filters)
    }


async def notify_admins(bot: Bot, admins: list):
    """
    Notify a list of admins that the bot has started.

    Args:
        bot (Bot): The aiogram Bot instance.
        admins (list): List of admin user IDs.
    """
    for admin in admins:
        await bot.send_message(admin, "bot started to work 👋🏿")
    await bot.session.close()


def setup_logging():
    """
    Configure logging for the application.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='#%(levelname)s %(asctime)s %(process)d %(filename)s:%(lineno)d %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        stream=sys.stdout
    )


async def setup_commands(bot: Bot, bot_commands: dict[str, str]):
    """
    Set bot commands for the Telegram bot.

    Args:
        bot (Bot): The aiogram Bot instance.
        bot_commands (dict): Mapping of command to description.
    """
    await bot.set_my_commands(
        [
            BotCommand(command=cmd, description=desc) for cmd, desc in bot_commands.items()
        ]
    )


def setup_handlers(target: Dispatcher | Router, handlers: list[dict[Awaitable, Any]]):
    """
    Register message handlers with optional filters.

    Args:
        target (Dispatcher | Router): The dispatcher or router to register handlers on.
        handlers (list): List of handler dicts from rout().
    """
    for handler in handlers:
        target.message.register(handler["handler"], *handler["filters"])


def setup_error_handlers(target: Dispatcher | Router, handler: Awaitable):
    """
    Register an error handler.

    Args:
        target (Dispatcher | Router): The dispatcher or router.
        handler (Awaitable): The error handler function.
    """
    target.error.register(handler)


def setup_callback_handlers(target: Dispatcher | Router, handlers: list[dict[Awaitable, Any]]):
    """
    Register callback query handlers with optional filters.

    Args:
        target (Dispatcher | Router): The dispatcher or router.
        handlers (list): List of handler dicts from rout().
    """
    for handler in handlers:
        target.callback_query.register(handler["handler"], *handler["filters"])


def setup_middlewares(target: Dispatcher | Router, midwrs: list[TelegramObject]):
    """
    Register middlewares for message handlers.

    Args:
        target (Dispatcher | Router): The dispatcher or router.
        midwrs (list): List of middleware objects.
    """
    for midw in midwrs:
        target.message.middleware(midw)


def setup_callback__middlewares(target: Dispatcher | Router, midwrs: list[TelegramObject]):
    """
    Register middlewares for callback query handlers.

    Args:
        target (Dispatcher | Router): The dispatcher or router.
        midwrs (list): List of middleware objects.
    """
    for midw in midwrs:
        target.callback_query.middleware(midw)


def setup_routers(dp: Dispatcher, routers: list[Router]):
    """
    Include routers into the dispatcher.

    Args:
        dp (Dispatcher): The main dispatcher.
        routers (list): List of Router instances.
    """
    for router in routers:
        dp.include_router(router)
