from aiogram import Bot, Dispatcher, executor, types
from aiogram.bot import api

bot = Bot(
    token='1927368703:AAFL5cNCFbkmxKYoGCQZXybrB_I49SdQbOA'
)
dp = Dispatcher(
    bot=bot
)

@dp.message_handlers(commands=['help'])
async def send_menu(me)