from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery


async def callback_handler(query: CallbackQuery, callback_data: CallbackData):
            await query.answer("Callback handler triggered")
