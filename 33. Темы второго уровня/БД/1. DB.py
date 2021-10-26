import sqlite3 as sq

with sq.connect('database.db') as con:
    cur = con.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS user (user_id TEXT, source INTEGER)')

    cur.execute('INSERT INTO user VALUES ("ИВАН", 243)')