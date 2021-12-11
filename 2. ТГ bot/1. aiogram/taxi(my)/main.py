from aiogram import types
from aiogram.types import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor
from creat_bot import bot, dp
from manage_db import *

from states import state_pass
from states.state_driver import reg_driver





@dp.message_handler(commands=['start', 'greet'])
async def greetinf(message : types.Message):
    text = [
        f'*Добро пожаловать, *{message.from_user.first_name} 🤗 здесь ты можешь найти себе водителя или стать им!',
        "",
        "Выбери нужную тебе команду:",
        "/drive -- оставить заявку",
        "/myorder -- мои заказы",
        "/greet -- экран приветствия",
        "/help -- помощь"
    ]
    await message.answer(text='\n'.join(text), parse_mode=ParseMode.MARKDOWN)

@dp.message_handler(commands='drive')
async def drive(message : types.Message):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.row(InlineKeyboardButton('Водитель 🚘', callback_data="dri1"),
               InlineKeyboardButton('Пассажир 🏂', callback_data="dri2"))

    await message.answer('Вы совершаете поездку как', reply_markup=markup)

@dp.message_handler(commands='myorder')
async def my_order(message : types.Message):
    await show_me_orders(message)

@dp.callback_query_handler(Text(startswith='delit'))
async def del_sql(callback : types.CallbackQuery):
    row_id = callback.data[-1:]
    print(row_id)
    await del_sqlite(callback, row_id)





state_pass.reg_pass(dp)
reg_driver(dp)


executor.start_polling(dp, skip_updates=True)