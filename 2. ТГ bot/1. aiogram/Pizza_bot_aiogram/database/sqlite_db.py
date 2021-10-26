import sqlite3 as sq
from create_bot import dp, bot
def sql_start():
    global con, cur
    with sq.connect('pizza.db') as con:

        cur = con.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')

    # cur.execute('INSERT INTO user VALUES ("ИВАН", 243)')
    #
    # global con, cur
    # con = sq.connect('pizza.db')
    # cur = con.cursor()
    # if con:
    #     print('DB is connect!')
    #     con.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    #     con.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?,?,?,?)', tuple(data.values()))
        con.commit()

async def read(message):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')

async def read2():
    return cur.execute('SELECT * FROM menu').fetchall()

async def sql_del(data):
    print(data)
    cur.execute('DELETE FROM menu WHERE name == ?', (data,))
    con.commit()