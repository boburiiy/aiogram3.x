from aiogram.types import Message


async def echo(message: Message):
    message.send_copy(message.chat.id)
