from aiogram import Bot, types
from aiogram.dispatcher import  Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
import os

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token='2023366758:AAFObAUVQaFss1A7FpvRRKHWX2zrCfDNyhM')
dp = Dispatcher(bot)

url_kb = InlineKeyboardMarkup(row_width=2)
urlButton1 = InlineKeyboardButton(text='ссылка', url='https://www.youtube.com/watch?v=gpCIfQUbYlY&t=3s')
urlButton2 = InlineKeyboardButton(text='ссылка2', url='http://af-online.lordfilms-s.biz/30151-film-na-sever-cherez-severo-zapad-1959.html')
x = [InlineKeyboardButton(text='ссылка9', url='https://www.youtube.com/watch?v=gpCIfQUbYlY&t=3s'),InlineKeyboardButton(text='ссылка', url='https://www.youtube.com/watch?v=gpCIfQUbYlY&t=3s'),InlineKeyboardButton(text='ссылка', url='https://www.youtube.com/watch?v=gpCIfQUbYlY&t=3s')]
url_kb.add(urlButton1,urlButton2).row(*x)

@dp.message_handler(commands='urlo')
async def url_command(message: types.Message):
    await message.answer('А вот и твои ссылочки:', reply_markup=url_kb)

inl_kb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Зизики', callback_data='zi_1'),
                                               InlineKeyboardButton(text='Зизики', callback_data='zi_9'))

@dp.message_handler(commands='test')
async def test_com(message: types.Message):
    await message.answer('Инлайн кнопка', reply_markup=inl_kb)

# @dp.callback_query_handler(text='zi_1')
# async def callb (callback: types.CallbackQuery):
#     await callback.answer('Ответочка на твой колбек', show_alert=True) # исчезающее сообщение
#     await callback.message.answer(('Ответочка на твой колбек'))
#     await callback.answer()  # чтобы исчезли "часы"

# Колбек для ловди нескольких колбеков
@dp.callback_query_handler(Text(startswith='zi'))
async def callb (callback: types.CallbackQuery):
    callback.message.text
    res = int(callback.data.split('_')[1])
    if res == 9:
        await callback.answer('дурак', show_alert=True)
    else:
        await callback.message.answer(('Ответочка на твоb 2 колбек'))
        await callback.answer()


executor.start_polling(dp, skip_updates=True)
