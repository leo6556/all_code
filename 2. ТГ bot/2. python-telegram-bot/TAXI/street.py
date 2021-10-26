import sqlite3 as sq
#
#
# with sq.connect('orders_database.db') as con:
#     cur = con.cursor()
#
#     cur.execute('CREATE TABLE IF NOT EXISTS user (user_id TEXT, busy INTEGER, name TEXT, car TEXT, number INTEGER, time TEXT, from_1 TEXT, where_1 TEXT, sale TEXT )')
#
#     # cur.execute('INSERT INTO user VALUES ("ИВАН", 243)')
#
#
#
#
# with sq.connect('orders_database.db') as con:
#     cur = con.cursor()
#
#     cur.execute('CREATE TABLE IF NOT EXISTS user (user_id TEXT,'
#                 ' text TEXT,'
#                 ' name TEXT,'
#                 ' valid INTEGER'
#                 )
#     # cur.execute('INSERT INTO user VALUES ("ИВАН", 243)')


# ****************************************************************************8888
import time

# with sq.connect('driver_database.db') as con:
#     cur = con.cursor()
#
#     cur.execute('CREATE TABLE IF NOT EXISTS user (user_id TEXT, busy INTEGER, name TEXT, car TEXT, number INTEGER, time TEXT, from_1 TEXT, where_1 TEXT, sale TEXT )')

    # cur.execute('INSERT INTO user VALUES ("ИВАН", 243)')

# with sq.connect('orders_database.db') as con:
#     cur = con.cursor()
#
#     cur.execute('CREATE TABLE IF NOT EXISTS ordersa (user_id TEXT, car TEXT, name TEXT, valid INTEGER, number TEXT, time TEXT, from_2 TEXT, where_2 TEXT, price INT)')


#  Алгоритм перезаписей БД поездок-завтра (и очистка БД завтра) в БД поездок-сегодня
o = time.asctime()
print(o[11:16])

with sq.connect('driver_database_tomr.db') as con:
        cur = con.cursor()

        cur.execute('SELECT * from user')
        n = cur.fetchall()
        print(n)
        l = len(n)

        for i in range(l):
            io = n[i]

            with sq.connect('driver_database.db') as con:
                cur = con.cursor()

                cur.execute(f'INSERT INTO user VALUES {io}')




