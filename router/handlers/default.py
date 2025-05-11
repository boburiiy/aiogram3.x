from aiogram.types import Message


async def echo(message: Message):
    await message.send_copy(message.chat.id)
