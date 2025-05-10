from aiogram.types import Message
from html import escape


async def start_handler(message: Message):
    name = escape(message.from_user.first_name)
    await message.answer(f"hi {name} nice to see you there how i can help you today?")


async def echo(message: Message):
    await message.send_copy(message.chat.id)
