from aiogram import types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import bot, dp
from aiogram.dispatcher.filters import Text
from manage_DN import *
from aiogram.types import  InlineKeyboardButton, InlineKeyboardMarkup

class Admin(StatesGroup):

    get_service = State()
    get_date = State()
    get_time = State()


@dp.message_handler(commands='load', state=None)
async def start(message : types.Message):
    await Admin.get_service.set()
    await message.answer('Выберите нужную услугу')


#Выход из машины состояния
@dp.message_handler(state="*", commands='stop' )
@dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_han(message: types.Message, state : FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer('OK')



@dp.message_handler(state=Admin.get_service)
async def load_service(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['service'] = message.text
    await Admin.next()
    await message.answer('Теперь выбери дату посещения')

@dp.message_handler(state= Admin.get_date)
async def load_date(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['day'] = message.text
    await Admin.next()
    await message.answer('Выберите время')


@dp.message_handler(state=Admin.get_time)
async def load_time(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['time'] = message.text
        await message.answer(data)

    await add_sql(state)

    await state.finish()

@dp.message_handler(state= Admin.get_time)
async def load_price(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text

    async with state.proxy() as data:
        await message.reply(str(data))
    await state.finish()


#УДАЛЕНИЕ

@dp.message_handler(commands='del')
async def dell(message : types.Message):
    red = await show2()

    for i in red:
        print(i)
        await message.answer(i[0] + i[1] + i[2], reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton('Удалить', callback_data='1')))
  