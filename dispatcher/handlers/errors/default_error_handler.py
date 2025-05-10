from aiogram.exceptions import *
from aiogram.types import ErrorEvent
import logging

async def err_handler(event: ErrorEvent):
    logging.exception(f'error occured \n{event}')