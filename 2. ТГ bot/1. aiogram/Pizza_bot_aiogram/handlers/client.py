from aiogram import types, Dispatcher
from create_bot import bot, dp
from mark_up import kb_client
from aiogram.types import ReplyKeyboardRemove
from create_bot import dp
from database import sqlite_db

# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Приятного аппетита',
                           reply_markup=kb_client)


# @dp.message_handler(commands=['Режим_работы'])
async def pizza_worttime(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00',
                           reply_markup=ReplyKeyboardRemove())

# @dp.message_handler(commands=['Расположение'])
async  def pizza_place(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Колбасная, 15',
                           reply_markup=ReplyKeyboardRemove())


# @dp.message_handler(commands=['меню'])
async def pizza_menu(message: types.Message):
    await sqlite_db.read(message)

def register_handlers_client(dp: Dispatcher):
  dp.register_message_handler(command_start, commands=['start', 'help'])
  dp.register_message_handler(pizza_worttime, commands=['Режим_работы'])
  dp.register_message_handler(pizza_place, commands=['Расположение'])
  dp.register_message_handler(pizza_menu, commands=['меню'])

