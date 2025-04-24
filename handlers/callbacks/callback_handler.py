from aiogram.types import CallbackQuery

async def callback_handler(query: CallbackQuery):
            await query.message.answer("Callback handler triggered")
