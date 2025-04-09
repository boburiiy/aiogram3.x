from aiogram.types import Message

async def echo_handler(message: Message):
    await message.send_copy(message.chat.id)