import sqlite3 as sq
from create_bot import bot, dp
from aiogram import types

with sq.connect('DB.db') as con:
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, desc TEXT, price TEXT)')


async def add_sql(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?,?,?,?)', tuple(data.values()))
        con.commit()

async def show_menu(message):
    for i in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, i[0], f'{i[1]}\nОписание: {i[2]}\nЦена: {i[3]}')

async def show_menu2():
    return cur.execute('SELECT * FROM menu').fetchall()

async def del_sql(data):
    cur.execute(f'DELETE FROM menu WHERE name == "{data}"')
