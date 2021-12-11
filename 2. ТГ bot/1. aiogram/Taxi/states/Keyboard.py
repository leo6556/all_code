from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from aiogram import types

'''*******************************PASSENGER****************************'''
markup = InlineKeyboardMarkup()

but1 = InlineKeyboardButton(text='ул. Жуковского', callback_data="ул. Жуковского", pay=True)
but2 = InlineKeyboardButton(text='ул. Линейная', callback_data="ул. Линейная")
but3 = InlineKeyboardButton(text='ул. Ягодная', callback_data="ул. Ягодная")
but4 = InlineKeyboardButton(text='ул. Семейная', callback_data="ул. Семейная")

markup.row(but1, but2).row(but3, but4)

async def pass_from(message : types.Message):
    await message.edit_text('Выберите точку отправления:', reply_markup=markup)




markup2 = InlineKeyboardMarkup()

but1 = InlineKeyboardButton(text='09:00', callback_data="10:00")
but2 = InlineKeyboardButton(text='12:00', callback_data="12:00")
but3 = InlineKeyboardButton(text='15:00', callback_data="15:00")
but4 = InlineKeyboardButton(text='18:00', callback_data="18:00")

markup2.row(but1, but2).row(but3, but4)

async def pass_when(message : types.Message):
    await message.edit_text('Выберите время отправления:', reply_markup=markup2)




markup3 = InlineKeyboardMarkup()

but1 = InlineKeyboardButton(text='Все верно 😄', callback_data="check_ok")
but2 = InlineKeyboardButton(text='Отменить 🥲', callback_data="check_no")

markup3.row(but1, but2)

async def pass_offer(message : types.Message, data):
    text = [
        "*Проверьте детали заказа:*",
        f"*Откуда:* {data['from']},",
        f"*Время:* {data['when']}",
        f"*Куда:* {data['where']}"
    ]
    await message.answer(text='\n'.join(text), reply_markup=markup3, parse_mode=ParseMode.MARKDOWN)


'''*******************************DRIVER****************************'''

markup4 = InlineKeyboardMarkup()

but5 = InlineKeyboardButton(text='09:00', callback_data="10:00")
but6 = InlineKeyboardButton(text='12:00', callback_data="12:00")
but7 = InlineKeyboardButton(text='15:00', callback_data="15:00")
but8 = InlineKeyboardButton(text='18:00', callback_data="18:00")

markup4.row(but5, but6).row(but7, but8)

async def dri_when(message : types.Message):
    await message.edit_text('Выберите время отправления:', reply_markup=markup4)





markup5 = InlineKeyboardMarkup()

but9 = InlineKeyboardButton(text='Все верно', callback_data="check_ok")
but10 = InlineKeyboardButton(text='Отмениить', callback_data="check_no")
markup5.row(but9, but10)

async def dri_end(message : types.Message, data):
    text = [
        "*Проверьте детали заявки:*",
        f"*Время:* {data['when']}",
        f"*Машина:* {data['car']}",
        f"*Номер телефона:* {data['number']}"
    ]
    await message.answer('\n'.join(text), reply_markup=markup5,
                            parse_mode=ParseMode.MARKDOWN)










