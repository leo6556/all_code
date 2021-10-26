import sqlite3

con = None

def gen_con():
    global con
    if con is None:
        con = sqlite3.connect('anketa.db')
    return con

def init_db(forse: bool = False):
    conn = gen_con()

    cur = conn.cursor()

    if forse:
        cur.execute('DROP TABLE IF EXISTS user_m')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS user_m (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    text TEXT NOT NULL
    )
    ''')


    conn.commit()


def add_m(user_id: int, text: str):
    conn = gen_con()
    cur = conn.cursor()
    cur.execute('INSERT INTO user_m (user_id, text) VALUES (?,?)', (user_id, text))
    conn.commit()

def count_m(user_id: int):
    conn = gen_con()
    cur = conn.cursor()
    cur.execute('SELECT count(*) FROM user_m WHERE user_id = ?', (user_id,))
    (res,) = cur.fetchone()
    conn.commit()
    return res


if __name__ == '__main__':
    init_db()

    add_m(user_id=123, text='878')

    r = count_m(123)

    print(r)