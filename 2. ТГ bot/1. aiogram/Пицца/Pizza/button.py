from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters import Text


bot = Bot(token='2023366758:AAFObAUVQaFss1A7FpvRRKHWX2zrCfDNyhM')
dp = Dispatcher(bot)

answ = dict()

# кнопки - ссылки
markup = InlineKeyboardMarkup(row_width=1)
but1 = InlineKeyboardButton(text='url1', url='https://www.b17.ru/article/94354/')
but2 = InlineKeyboardButton(text='url2', url='https://www.b17.ru/article/94354/')
markup.add(but1, but2)

@dp.message_handler(commands='url')
async def url(message : types.Message):
    await message.answer('Ccilki', reply_markup=markup)


# callback but

markup2 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='like', callback_data='lik1')).add(InlineKeyboardButton(text='dis', callback_data='lik2'))

@dp.message_handler(commands='test')
async def url(message : types.Message):
    await message.answer('Голосование за власть', reply_markup=markup2)

@dp.callback_query_handler(Text(startswith='lik'))
async def callhan(callback : types.CallbackQuery):
    res = callback.data
    print(res)
    print(answ)
    if str(callback.from_user.id) not in answ:
        answ[f'{callback.from_user.id}'] = res
        await callback.message.answer('Вы проголосовали!')
    else:
        await callback.message.answer('Вы уже проголосовали!')
        await callback.answer()


executor.start_polling(dp, skip_updates=True)

