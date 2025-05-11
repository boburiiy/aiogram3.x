from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from typing import Any, Awaitable, Callable
# from config.config import bot
import asyncio
import logging


class Throttling(BaseMiddleware):
    """
    Throttling middleware for aiogram 3.x.
    This middleware limits how frequently a user can trigger a handler, preventing spam or excessive requests.
    Attributes:
        delay (float): Minimum time interval (in seconds) required between consecutive calls from the same user.
        last_call (dict): Stores the timestamp of the last call for each user
    """

    def __init__(self, delay: float = 1):
        self.delay = delay
        self.last_call = {}

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],

    ) -> Any:
        user_id = event.from_user.id
        if user_id in self.last_call and (asyncio.get_running_loop().time()-self.last_call[user_id]) < self.delay:
            logging.warning(f'user: {user_id} just playing with me')
            with open('test1.py','w') as f:
                f.write(str(data))
            return
        self.last_call[user_id] = asyncio.get_running_loop().time()
        return await handler(event, data)
