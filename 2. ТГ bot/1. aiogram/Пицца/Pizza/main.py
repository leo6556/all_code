from aiogram import Bot, types
from aiogram.utils import executor

from create_bot import dp, bot
from jj import lo987
from database import *
from jj import admin

async def on_startup(_):
    print('Бот вышел в онлайн')
#     await add_sql()


lo987.reg_han_dop(dp)
admin.reg_admin(dp)


@dp.message_handler(commands=['start', 'help'])
async def com_start(message : types.Message):
    await bot.send_message(message.from_user.id, text='Добро пожаловать в пиццерию Мама Джонс')
#
# @dp.message_handler(commands=['where'])
# async def where(message : types.Message):
#     await bot.send_message(message.from_user.id, 'ул. Гоголя, 38')

@dp.message_handler(commands=['time'])
async def time_work(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вс-вс 8:00-24:00')


@dp.message_handler()
async def echo(message : types.Message):
    await message.answer(message.text)
    # await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)




