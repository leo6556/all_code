from aiogram import types
from aiogram.dispatcher import Dispatcher
from create_bot import dp, bot
from manage_DN import *

async def exho(message : types.Message):
    await bot.send_message(message.from_user.id, message.text + '- БРЕХНЯ')

@dp.message_handler(commands='tell')
async def sql(message : types.Message):
    await show_sql(message)


@dp.message_handler(lambda message: 'ufo' in message.text)
async def ufo(message : types.Message):
    await message.answer(808)

@dp.message_handler(lambda message: message.text.startswith('такси'))
async def ufo(message : types.Message):
    await message.answer(809)


def reg_han(dp : Dispatcher):
    dp.register_message_handler(exho)