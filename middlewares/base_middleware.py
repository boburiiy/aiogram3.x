from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from typing import Any, Awaitable, Callable
import asyncio


class Throttling(BaseMiddleware):
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
            return
        self.last_call[user_id] = asyncio.get_running_loop().time()
        return await handler(event, data)
