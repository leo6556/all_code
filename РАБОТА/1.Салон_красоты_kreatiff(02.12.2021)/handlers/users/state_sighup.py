import random

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram import types, Dispatcher
from aiogram.types import ContentType

from states.sighup import *
from keyboards.inline.panel_state_sighup import *
from DB.db3_manage import *
from .echo import start_state

# НАХОДИТЬСЯ В echo
# @dp.message_handler(commands='sighup', state=None)
# async def start_state(message : types.Message):
#     await Client.service.set()
#     await main_panel(message)

@dp.callback_query_handler(Text(startswith='order_'), state=Client.service)
async def show_category(callback : types.CallbackQuery, state : FSMContext):
    data = callback.data

    if data == 'order_face':
        await shablon(callback, table=f'{data}', state=state)
    elif data == 'order_lash':
        await shablon(callback, table=f'{data}', state=state)
    elif data == 'order_brow':
        await shablon(callback, table=f'{data}', state=state)
    elif data == 'order_depil':
        await shablon(callback, table=f'{data}', state=state)
    elif data == 'order_man':
        await shablon(callback, table=f'{data}', state=state)
    elif data == 'order_bar':
        await shablon(callback, table=f'{data}', state=state)
    elif data == 'order_care':
        await shablon(callback, table=f'{data}', state=state)
    elif data == 'order_else':
        await shablon(callback, table=f'{data}', state=state)

@dp.callback_query_handler(Text(startswith='resp_'), state=Client.service)
async def save_service(callback : types.CallbackQuery, state : FSMContext):

    async with state.proxy() as data:
        v = data['master_1']
        var = v[callback.data[5:]]
        data['service'] = callback.data[5:]
    await Client.next()
    await panel_of_masters(callback, var, state=state)

@dp.callback_query_handler(Text(startswith='mas_'), state=Client.master)
async def save_master(callback : types.CallbackQuery, state : FSMContext):
    async with state.proxy() as data:
        data['master'] = callback.data[4:]
    await Client.next()
    await panel_show_date(callback)

@dp.callback_query_handler(Text(startswith='date_'), state=Client.date)
async def save_date(callback : types.CallbackQuery, state : FSMContext):
    async with state.proxy() as data:
        data['date'] = callback.data[5:]
    await Client.next()
    await panel_show_time(callback)

@dp.callback_query_handler(Text(startswith='time_'), state=Client.time)
async def save_time(callback : types.CallbackQuery, state : FSMContext):
    async with state.proxy() as data:
        data['time'] = callback.data[5:]
    await share_contact(callback.message)


@dp.callback_query_handler(Text(startswith='send_'), state = Client.time)
async def do_it(callback : types.CallbackQuery):
    if callback.data == 'send_auto':
        but_1 = KeyboardButton('👉🏼 Поделиться номером 👈🏼', request_contact=True)
        markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markup.add(but_1)
        await callback.message.delete()
        await callback.message.answer('Просто нажми на кнопку "Поделиться номером"', reply_markup=markup)
        await Client.next()
    else:
        await Client.next()
        await callback.message.edit_text('*Введите свой номер c* +7- или 8-', parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(state=Client.contact)
async def save_number(message : types.Message, state : FSMContext):
    cont = message.text
    id = message.from_user.id

    async with state.proxy() as data:
        rand = random.randint(1000, 9999)
        text = [
            f'*Ваш заказ:* 🔖 # {rand}',
            f'*Дата* - {data["date"]}',
            f'*Услуга* - {data["service"]}',
            f'*Время* - {data["time"]}',
            f'*Мастер* - {data["master"]}',
            f'*Ваш номер* - {cont}',
            "",
            "Проверьте детали заказа 💁‍♀️"
        ]
        data['random'] = rand
        data['number'] = cont
        data['user_id'] = id

    await check_order(message, text)

@dp.message_handler(content_types=ContentType.CONTACT, state = Client.contact)
async def show_order(message : types.Message, state : FSMContext):
    cont = message.contact

    async with state.proxy() as data:
        rand = random.randint(1000, 9999)
        text = [
            f'*Ваш заказ:* 🔖 # {rand}',
            f'*Дата* - {data["date"]}',
            f'*Услуга* - {data["service"]}',
            f'*Время* - {data["time"]}',
            f'*Мастер* - {data["master"]}',
            f'*Ваш номер* - {cont["phone_number"]}',
            "",
            "Проверьте детали заказа 💁‍♀️"
        ]
        data['random'] = rand
        data['number'] = cont["phone_number"]
        data['user_id'] = cont["user_id"]

    await check_order(message, text)

@dp.callback_query_handler(Text(startswith='check_'), state=Client.contact)
async def check_it(callback : types.CallbackQuery, state : FSMContext):

    if callback.data == 'check_ok':
        async with state.proxy() as data:
            await save_order(data["user_id"], data['random'], data['service'], data['date'], data['time']
                             , data['master'], data['number'])
            await callback.message.edit_text('Вы записались 🤗 Cвои заказы можете посмотреть по команде /myorders')
            await state.finish()
    elif callback.data == 'check_stop':
        await state.finish()
        await callback.message.edit_text('Заказ не сформирован 😌 экран приветствия /start')
    else:
        await state.finish()
        await callback.message.edit_text('Давайте сформируем заказ заново 😊')
        await start_state(callback.message)

@dp.callback_query_handler(Text(startswith='back__'), state='*')
async def show_category(callback : types.CallbackQuery):
    data = callback.data
    if data == 'back__':
        await main_panel_2(callback)

@dp.message_handler(commands='stop_order', state='*')
async def show_category(message : types.Message, state : FSMContext):
    await state.finish()
    # await message.delete()
    await message.reply('Заказ не сформирован, страница приветствия /start')


@dp.callback_query_handler(Text(startswith='stop_order'), state='*')
async def show_category(callback : types.CallbackQuery, state : FSMContext):
    await state.finish()
    await callback.message.edit_text('Заказ не сформирован')

@dp.message_handler(state='*')
async def save_number(message : types.Message):

    await message.answer('Вы уже начали офрмлять заявку выше, либо закончите, либо отмените (нажмите на команду /stop_order)')