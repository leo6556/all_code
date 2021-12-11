import random

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram import types, Dispatcher
from aiogram.types import ContentType

from states.sighup import *
from keyboards.inline.panel_state_sighup import *
from DB.db3_manage import *
from keyboards.inline.show_right_order import *

@dp.message_handler(commands='myorders')
async def show_orders(message : types.Message):
    id = message.from_user.id
    read = await show_right_order(id)
    if len(read) == 0:
        await message.answer(text='У вас пока нет заказов, /sighup - записаться')

    for i in read:
        text = [
            f'*Ваш заказ:* 🔖 # {i[1]}',
            f'*Дата* - {i[3]}',
            f'*Услуга* - {i[2]}',
            f'*Время* - {i[4]}',
            f'*Мастер* - {i[5]}',
            f'*Ваш номер* - {i[6]}',

        ]
        await message.answer(text='\n'.join(text), parse_mode=ParseMode.MARKDOWN, reply_markup=markup22)




@dp.callback_query_handler(Text(startswith='show_'))
async def call_right_order(callback : types.CallbackQuery):
    cur_text = callback.message.text
    print(len(cur_text))

    if callback.data == 'show_more':
        text = cur_text + '\n' + '📍Адрес: просп. Просвещения, 15' + '\n' + '📍Ежедневно c 10:00 до 22:00' "\n" + '📍Связь: +7 (911) 138-99-08'
        await callback.message.edit_text(text=text, reply_markup=markup33)
        await callback.answer()

    elif callback.data == 'show_stop':
        text = cur_text + '\n\n' + '*Вы уверены, что хотите удалить заказ?*🤔'
        await callback.message.edit_text(text=text, reply_markup=markup44, parse_mode=ParseMode.MARKDOWN)
        await callback.answer()

    elif callback.data == 'show_less':
        spl = cur_text.split('📍')
        await callback.message.edit_text(text=spl[0], reply_markup=markup22)
        await callback.answer()

    elif callback.data == 'show_less_back':
        spl = cur_text.split("Ваш номер - ")
        await callback.message.edit_text(text=spl[0]+"Ваш номер - "+spl[1][:11], reply_markup=markup22)
        await callback.answer()

    elif callback.data == 'show_del':
        spl = cur_text.split('#')
        order_num = spl[1][1:5]
        await del_order(order_num)
        await callback.message.edit_text('Заказ расформирован 😌')