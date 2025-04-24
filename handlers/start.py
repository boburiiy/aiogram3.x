from aiogram.types import Message
from config.config import keyboards
from aiogram.fsm.context import FSMContext
from utils.FSM.states import Form
names = []


async def start_handler(message: Message, state: FSMContext):
    await state.clear()
    if message.from_user.id in names:
        await message.answer('hi how are you?')
        return
    await message.answer('hi how are you?\nwhat`s your name?', reply_markup=keyboards.get('simple_kb', 'inline'))
    await state.set_state(Form.name)
