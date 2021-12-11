import sqlite3 as sq

with sq.connect('database4.db') as con:
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS ordersa()')