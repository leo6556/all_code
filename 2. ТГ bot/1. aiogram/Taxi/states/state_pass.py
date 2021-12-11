from aiogram import types
from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from creat_bot import bot, dp
from states.Keyboard import *
from manage_db import *


class Passenger(StatesGroup):
    froom = State()
    when = State()
    where = State()
    end = State()

# @dp.callback_query_handler(lambda x: x.data.startswith('dri2'), state=None)
async def start(callback : types.CallbackQuery):

    await Passenger.froom.set()
    await pass_from(callback.message)

# @dp.callback_query_handler(lambda x: x.data.startswith("ул."), state=Passenger.froom)
async def save_from(callback : types.CallbackQuery, state : FSMContext):
    async with state.proxy() as data:
        data['from'] = callback.data
    await Passenger.next()
    await pass_when(callback.message)

# @dp.callback_query_handler(lambda x: x.data.endwith(':00'), state=Passenger.when)
async def save_when(callback : types.CallbackQuery, state : FSMContext):
    async with state.proxy() as data:
        data['when'] = callback.data
    await Passenger.next()
    await callback.message.edit_text('Куда едем? Введите улицу')

# @dp.message_handler(state=Passenger.where)
async def save_where (message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['where'] = message.text
    await Passenger.next()
    await pass_offer(message, data)

# @dp.callback_query_handler(lambda x : x.data.startswith('check'), state=Passenger.end)
async def ending(callback : types.CallbackQuery, state : FSMContext):
    check = callback.data

    if check == 'check_ok':
        await callback.message.edit_text('Отлично! Заказ сформирован 🤗')
        await save_pass(state)
        await state.finish()
    elif check == 'check_no':
        await callback.message.edit_text('Хорошо 😌 вы можете начать заново /drive')
        await state.finish()


# @dp.message_handler()
async def echo(message: types.Message):

    markup90 = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='PIPI', request_location=True)
            ]
        ]
    )
    await message.answer('Экран приветствия -- /greet', reply_markup=ReplyKeyboardRemove())



def reg_pass(dp : Dispatcher):
    dp.register_callback_query_handler(start, lambda x: x.data.startswith('dri2'), state=None)
    dp.register_callback_query_handler(save_from, lambda x: x.data.startswith("ул."), state=Passenger.froom)
    dp.register_callback_query_handler(save_when, lambda x: x.data.startswith("1"), state=Passenger.when)
    dp.register_message_handler(save_where, state=Passenger.where)
    dp.register_callback_query_handler(ending, lambda x: x.data.startswith('check'), state=Passenger.end)
    dp.register_message_handler(echo)