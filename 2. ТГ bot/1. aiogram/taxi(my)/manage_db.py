import sqlite3 as sq
from creat_bot import dp, bot
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode



'''***************************ПАССАЖИРЫ********************************'''

with sq.connect('DATABASE.db') as con:
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS pasr (p_from TEXT, p_when TEXT,'
                ' p_where TEXT, p_some1 TEXT, p_some2 TEXT)')

async def save_pass(state):
    async with state.proxy() as data:
        cur.execute(f'''INSERT INTO pasr VALUES ("{data['from']}", "{data['when']}", "{data['where']}", "0", "0")''')
        con.commit()

async def show_me_orders(message):
    res = cur.execute('SELECT p_from, p_when, p_where, p_some1, p_some2, rowid FROM pasr').fetchall()

    for i in res:
        text = [
            "Ваш заказ:",
            f"Отправление: c {i[0]}",
            f"Время: {i[1]}",
            f"Куда: {i[2]}"
        ]
        await bot.send_message(message.from_user.id, text='\n'.join(text), reply_markup=InlineKeyboardMarkup().row(InlineKeyboardButton('Подробнее', callback_data='56')
                                                                                            , InlineKeyboardButton('Отменить', callback_data=f'delit{i[-1]}')))


async def del_sqlite(callback, row_id):
    cur.execute(f'DELETE FROM pasr WHERE rowid == "{row_id}"')
    con.commit()
    await callback.message.edit_text('Заказ отменен')






"""*************************************DRIVER***************************************"""


with sq.connect('DATABASE.db') as con:
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS driver (d_when TEXT,'
                'd_car TEXT, d_number TEXT, d_some1 TEXT, d_some2 TEXT)')

async def save_driver(state):
    async with state.proxy() as data:
        cur.execute(f'''INSERT INTO driver VALUES ("{data['when']}", "{data['car']}", "{data['number']}", "0", "0")''')
        con.commit()

