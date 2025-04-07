from config import dp
from aiogram.types import Message
@dp.message()
async def start_handler(message:Message):
    await message.answer('hi how are you?')