import sqlite3 as sq

with sq.connect('database.db') as con:
    cur = con.cursor()

    # with open('sql_iterdamp.sql', 'w') as f:
    #     for sql in con.iterdump():
    #         f.write(sql)

    with open('sql_iterdamp.sql', 'r') as f:
        sql = f.read()
        cur.executescript(sql)