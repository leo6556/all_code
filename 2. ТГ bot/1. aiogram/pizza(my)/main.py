from aiogram import types
from aiogram.utils import executor

from create_bot import dp, bot
from mode import echo

@dp.message_handler(commands=['start'])
async def start(mwssage: types.Message):
    await mwssage.answer('Приветики')

echo.reg_han(dp)
executor.start_polling(dp)

