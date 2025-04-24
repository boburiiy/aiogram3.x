from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from utils.FSM.states import Form


async def greet_new_user(message: Message, state: FSMContext):
    await state.update_data(name=message.text, id=message.from_user.id)
    await state.set_state(Form.id)
    await message.answer(f"I'm glad to see you here, {message.text}!")


async def welcome(message: Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(f'data set to {data}')
