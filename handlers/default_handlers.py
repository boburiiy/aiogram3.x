from aiogram.filters import CommandStart
from aiogram.types import Message
from handlers.routrs import default_router as router

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Hello, {(message.from_user.id)}!")

@router.message()
async def echo(message: Message):
    await message.send_copy(chat_id=message.chat.id)
