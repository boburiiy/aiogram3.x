from aiogram.types import Message
from dispatcher.keyboards.example import kb1,kb2

async def start_handler(message: Message):
    await message.answer('hi how are you?', reply_markup=kb2)
