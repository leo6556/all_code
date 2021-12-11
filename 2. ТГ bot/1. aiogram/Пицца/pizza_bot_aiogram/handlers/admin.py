from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher

from database import sqlite_db
from create_bot import bot
from aiogram.dispatcher.filters import Text
from database import sqlite_db
from mark_up import admin_kb
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

ID = None

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

# Получаем ID текущего модератора
# @dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def make_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Что нужно?', reply_markup= admin_kb.button_admin)
    await message.delete()





# Начало диалога загрузки нового пункта меню
# @dp.message_handler(commands='Загрузить', state=None)
async def cm_start(message: types.Message):
    if message.from_user.id == ID:
        await message.reply('Загрузить фото')
        await FSMAdmin.photo.set()


# Ловим первый ответ и пишем в словарь
# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await  FSMAdmin.next()
        await message.reply('Теперь введи название')


# ловим второй ответ

# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message:types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.reply('Введи описание')


# Ловим третий ответ
# @dp.message_handler(state=FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdmin.next()
        await message.reply('Теперь укажи цену')


# Ловим последний ответ и используем полученные данные
# @dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state:FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = float(message.text)

        await sqlite_db.sql_add_command(state)

        await state.finish()


# Выход из состояний
# @dp.message_handler(state="*", commands='отмена')
# @dp.message_handler(Text(equals='отмена', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('ОК')

# Удаление из меню для админа
# @dp.callback_query_handler(lamda x: x.data and a.data.startswith('del '))
async def del_callb(callback_query: types.CallbackQuery):
    await sqlite_db.sql_del(callback_query.data.replace('del ', ''))
    await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} удлена', show_alert=True)

# @dp.message_handler(commands='удалить')
async def delete_item(message: types.Message):
    if message.from_user.id == ID:
        read = await sqlite_db.read2()
        for ret in read:
            await bot.send_photo(message.from_user.id, ret[0], f'ret[1]\nОписание:блабала')
            await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().
                                   add(InlineKeyboardButton(f'Удлить {ret[1]}', callback_data=f'del {ret[1]}')))



def register_handlers_admin(dp: Dispatcher):
  dp.register_message_handler(cm_start, commands='load', state=None)
  dp.register_message_handler(make_command, commands=['moderator'], is_chat_admin=True)
  dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
  dp.register_message_handler(load_name, state=FSMAdmin.name)
  dp.register_message_handler(load_description, state=FSMAdmin.description)
  dp.register_message_handler(load_price, state=FSMAdmin.price)
  dp.register_message_handler(cancel_handler, state="*", commands='отмена')
  # dp.message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")
  dp.register_callback_query_handler(del_callb, Text(startswith='del'))
  dp.register_message_handler(delete_item, commands='удалить')