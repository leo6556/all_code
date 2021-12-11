import sqlite3 as sq
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import bot, dp


with sq.connect('MyDB.db') as con:
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOt EXISTS oder (service TEXT, date TEXT, time TEXT)')

async def add_sql(state):
    async with state.proxy() as data:
        print(data)
        cur.execute('INSERT INTO oder VALUES (?,?,?)', tuple(data.values()))
        con.commit()

async def show_sql(message):
    for i in cur.execute('SELECT * FROM oder').fetchall():
        await message.answer(i[0] + i[1]+ i[2] + 'на этом всё')

async def show2():
    return cur.execute('SELECT * FROM oder').fetchall()