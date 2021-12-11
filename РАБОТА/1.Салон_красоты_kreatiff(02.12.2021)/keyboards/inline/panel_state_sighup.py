import time

from states.sighup import *

from aiogram import types, bot
from aiogram.dispatcher import FSMContext

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from DB.db2_manage import *


markup_main_panel = InlineKeyboardMarkup()

but1 = InlineKeyboardButton('Уход за кожей лица', callback_data='order_face')
but2 = InlineKeyboardButton('Брови', callback_data='order_brow')
but3 = InlineKeyboardButton('Ресницы', callback_data='order_lash')
but4 = InlineKeyboardButton('Ман- и педикюр', callback_data='order_man')
but5 = InlineKeyboardButton('Депиляция', callback_data='order_depil')
but6 = InlineKeyboardButton('Парикмахерская', callback_data='order_bar')
but7 = InlineKeyboardButton('Уход за волосами', callback_data='order_care')
but8 = InlineKeyboardButton('Другое', callback_data='order_else')
but9 = InlineKeyboardButton('Приостановить заказ', callback_data='stop_order')

markup_main_panel.row(but1, but7).row(but3, but2).row(but6, but5).row(but4, but8).row(but9)

async def main_panel(message : types.Message):
        await message.answer('Выберите нужную категорию 💁🏼‍♀️', reply_markup=markup_main_panel)

async def main_panel_2(callback : types.CallbackQuery):
        await callback.message.edit_text('Выберите нужную категорию 💁🏼‍♀️', reply_markup=markup_main_panel)
        await callback.answer()



async def shablon(callback : types.CallbackQuery, table, state : FSMContext):
    read = await shablon_show_order(f'{table}')
    dict = {}

    markup = InlineKeyboardMarkup()
    for i in read:
        markup.add(InlineKeyboardButton(f'{i[0]}', callback_data=f'resp_{i[0]}'))
        dict[i[0]] = i[1]
    markup.add(InlineKeyboardButton('Назад', callback_data="back__"))

    async with state.proxy() as data:
        data['master_1'] = dict

    await callback.message.edit_text('Какая вам нужна услуга? 💆🏼‍♀️', reply_markup=markup)
    await callback.answer()



async def panel_of_masters(callback : types.CallbackQuery, var, state):
    v = var.split(',')
    if len(v) <= 1:
        async with state.proxy() as data:
            data['master'] = v[0]
        await Client.next()
        await panel_show_date(callback)
    else:
        markup = InlineKeyboardMarkup(row_width=2)
        for i in v:
            markup.insert(InlineKeyboardButton(f'{i}', callback_data=f'mas_{i}'))
        await callback.message.edit_text('Выберите мастера 🧑🏼‍⚕', reply_markup=markup)
        await callback.answer()


async def panel_show_date(callback : types.CallbackQuery):
    t = time.asctime()
    d = int(t[7:10])
    m = t[4:7]

    month = {'Sep': 'сен', 'Oct': 'окт', 'Nov': 'нояб', 'Dec': 'дек', 'Jan': 'янв', 'Feb': 'фев', 'Mar': 'мар',
             'Apr': 'апр', 'May': 'мая', 'Jun': 'июн',
             'Jul': 'июл', 'Aug': 'авг'}
    month2 = {'Sep': 'окт', 'Oct': 'нояб', 'Nov': 'дек', 'Dec': 'янв', 'Jan': 'фев', 'Feb': 'мар', 'Mar': 'апр',
              'Apr': 'мая', 'May': 'июн', 'Jun': 'июл',
              'Jul': 'авг', 'Aug': 'сен'}
    d_month = {'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31, 'Jan': 31, 'Feb': 28, 'Mar': 31,
             'Apr': 30, 'May': 31, 'Jun': 30,
             'Jul': 31, 'Aug': 31}

    if d_month[m] == 31:
        markup = InlineKeyboardMarkup(row_width=5)
        if d <= 22:
            for i in range(10):
                markup.insert(InlineKeyboardButton(f'{d + i} {month[m]}', callback_data=f'date_{d + i} {month[m]}'))
            markup.row(InlineKeyboardButton('Приостановить оформление', callback_data='stop_order'))
            await callback.message.edit_text('Выбери удобную дату 📅', reply_markup=markup)
        else:
            c = 32 - d
            c_1 = 10 - c
            for i in range(c):
                markup.insert(InlineKeyboardButton(f'{d + i} {month[m]}', callback_data=f'date_{d + i} {month[m]}'))
            for i in range(1, c_1 + 1):
                markup.insert(InlineKeyboardButton(f'{i} {month2[m]}', callback_data=f'date_{i} {month2[m]}'))
            markup.row(InlineKeyboardButton('Приостановить оформление', callback_data='stop_order'))
            await callback.message.edit_text('Выбери удобную дату 📅', reply_markup=markup)

    if d_month[m] == 30:
        markup = InlineKeyboardMarkup(row_width=5)
        if d <= 21:
            for i in range(10):
                markup.insert(InlineKeyboardButton(f'{d + i} {month[m]}', callback_data=f'date_{d + i} {month[m]}'))
            markup.row(InlineKeyboardButton('Приостановить оформление', callback_data='stop_order'))
            await callback.message.edit_text('Выбери удобную дату 📅 ', reply_markup=markup)
        else:
            c = 31 - d
            c_1 = 10 - c
            for i in range(c):
                markup.insert(InlineKeyboardButton(f'{d + i} {month[m]}', callback_data=f'date_{d + i} {month[m]}'))
            for i in range(1, c_1 + 1):
                markup.insert(InlineKeyboardButton(f'{i} {month2[m]}', callback_data=f'date_{i} {month2[m]}'))
            markup.row(InlineKeyboardButton('Приостановить оформление', callback_data='stop_order'))
            await callback.message.edit_text('Выбери удобную дату 📅', reply_markup=markup)

    if d_month[m] == 28:
        markup = InlineKeyboardMarkup(row_width=5)
        if d <= 19:
            for i in range(10):
                markup.insert(InlineKeyboardButton(f'{d + i} {month[m]}', callback_data=f'date_{d + i} {month[m]}'))
            markup.row(InlineKeyboardButton('Приостановить оформление', callback_data='stop_order'))
            await callback.message.edit_text('Выбери удобную дату 📅', reply_markup=markup)
        else:
            c = 29 - d
            c_1 = 10 - c
            for i in range(c):
                markup.insert(InlineKeyboardButton(f'{d + i} {month[m]}', callback_data=f'date_{d + i} {month[m]}'))
            for i in range(1, c_1 + 1):
                markup.insert(InlineKeyboardButton(f'{i} {month2[m]}', callback_data=f'date_{i} {month2[m]}'))
            markup.row(InlineKeyboardButton('Приостановить оформление', callback_data='stop_order'))
            await callback.message.edit_text('Выбери удобную дату 📅', reply_markup=markup)

async def panel_show_time(callback : types.CallbackQuery):
    list = ['10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30',
            '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30',
            '20:00', '20:30', '21:00', '21:30', '22:00']
    markup = InlineKeyboardMarkup(row_width=5)
    for i in list:
        markup.insert(InlineKeyboardButton(f'{i}', callback_data=f'time_{i}'))
    markup.row(InlineKeyboardButton('Приостановить оформление', callback_data='stop_order'))
    await callback.message.edit_text('В какое время вам удобно? 🕓', reply_markup=markup)
    await callback.answer()

async def share_contact(message : types.Message):
    markup = InlineKeyboardMarkup()
    but_1 = InlineKeyboardButton('Автоматически', callback_data='send_auto')
    but_2 = InlineKeyboardButton('Ввести вручную', callback_data='send_hand')
    markup.add(but_1, but_2)

    await message.edit_text('*Поделитесь своим контактом* ☎️\n Это можно сделать как автоматически, так и написать в ручную 👇🏼 ', reply_markup=markup, parse_mode=ParseMode.MARKDOWN)


async def check_order(message : types.Message, text):
    markup = InlineKeyboardMarkup()
    but1 = InlineKeyboardButton('Все верно', callback_data='check_ok')
    but2 = InlineKeyboardButton('Отменить', callback_data='check_stop')
    but3 = InlineKeyboardButton('Заново', callback_data='check_')
    markup.row(but1, but2, but3)

    await message.answer(text='\n'.join(text), reply_markup=markup, parse_mode=ParseMode.MARKDOWN)
