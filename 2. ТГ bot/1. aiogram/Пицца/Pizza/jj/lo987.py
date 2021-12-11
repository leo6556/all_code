from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from create_bot import bot, dp
from database import show_menu

# @dp.message_handler(commands=['where'])
async def where(message : types.Message):
    await bot.send_message(message.from_user.id, 'ул. Гоголя, 38')

def reg_han_dop(dp: Dispatcher):
    dp.register_message_handler(where, commands=['wher'])

@dp.message_handler(commands='menu')
async def pizza_menu(message : types.Message):
    await show_menu(message)
