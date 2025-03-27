from aiogram.types import BotCommand
from .config import commands
import importlib
import logging
import sys

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='#%(levelname)s %(asctime)s %(process)d %(filename)s:%(lineno)d %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        stream=sys.stdout
    )


async def set_commands(bot):
    commands_list = [
        BotCommand(command=key, description=value) for key, value in commands.items()
    ]
    await bot.set_my_commands(commands_list)


def setup_routers(routers_path, dp):
    for routers_from_path in routers_path:
        routers = importlib.import_module(routers_from_path).routers
        for router in routers:
            dp.include_router(router)
