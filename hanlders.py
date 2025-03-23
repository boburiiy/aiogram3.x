from aiogram.filters import CommandStart
from aiogram.types import Message
from config import dp


@dp.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer(f"Hello, {(message.from_user.id)}!")


@dp.message()
async def echo(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")
