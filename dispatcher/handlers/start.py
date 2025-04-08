from aiogram.types import Message


async def start_handler(message: Message):
    await message.answer('hi how are you?')
