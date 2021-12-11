from aiogram import types
from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from creat_bot import bot, dp
from states.Keyboard import *
from manage_db import *


class Driver(StatesGroup):
    when = State()
    car_model = State()
    number = State()
    end = State()


# @dp.callback_query_handler(lambda x: x.data.startswith('dri1'), state=None)
async def stat(callback : types.CallbackQuery, state : FSMContext):
    await Driver.when.set()
    await dri_when(callback.message)

# @dp.callback_query_handler(lambda x : x.data.startswith('1'), state=Driver.when)
async def save_when(callback : types.CallbackQuery, state : FSMContext):
    async with state.proxy() as data:
        data['when'] = callback.data
    await callback.message.edit_text('Теперь введите модель и номер своей машины')
    await Driver.next()

# @dp.message_handlers(state=Driver.car_model)
async def save_car(message : types.Message, state : FSMContext):
    car = message.text
    async with state.proxy() as data:
        data['car'] = car.capitalize()
    await message.answer('Оставьте номер для связи')
    await Driver.next()

# @dp.message_handlers(state=Driver.number)
async def save_number(message : types.Message, state : FSMContext):
    number = message.text
    async with state.proxy() as data:
        data['number'] = number
    await dri_end(message, data)
    await Driver.next()


# @dp.callback_query_handler(lambda x : x.data.startswith('check'), state = Driver.end)
async def ending(callback : types.CallbackQuery, state : FSMContext):
    check = callback.data
    if check == 'check_ok':
        await callback.message.edit_text('Заявка успешно сформирована 🤗')
        await save_driver(state)
        await state.finish()
    else:
        await callback.message.edit_text('Хорошо 😌 вы можете начать заново /drive')
        await state.finish()











def reg_driver(dp : Dispatcher):
    dp.register_callback_query_handler(stat, lambda x: x.data.startswith('dri1'), state=None)
    dp.register_callback_query_handler(save_when, lambda x: x.data.startswith('1'), state=Driver.when)
    dp.register_message_handler(save_car, state=Driver.car_model)
    dp.register_message_handler(save_number, state=Driver.number)
    dp.register_callback_query_handler(ending, lambda x: x.data.startswith('check'), state=Driver.end)















































































