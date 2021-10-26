import sqlite3

def ensure_con(func):

    def inner(*args, **kwargs):
        with sqlite3.connect('anketa.db') as conn:
            res = func(*args, conn=conn, **kwargs)
        return res

    return inner

@ensure_con
def init_db(conn, forse: bool = False):

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

@ensure_con
def add_m(conn, user_id: int, text: str):
    cur = conn.cursor()
    cur.execute('INSERT INTO user_m (user_id, text) VALUES (?,?)', (user_id, text))
    conn.commit()

@ensure_con
def count_m(conn, user_id: int):
    cur = conn.cursor()
    cur.execute('SELECT count(*) FROM user_m WHERE user_id = ?', (user_id,))
    (res,) = cur.fetchone()
    conn.commit()
    return res

@ensure_con
def list_m(conn, user_id: int, limit: int):
    cur = conn.cursor()
    cur.execute('SELECT id, text FROM user_m WHERE user_id = ? LIMIT ?', (user_id, limit,))
    return cur.fetchall()

if __name__ == '__main__':

    add_m(user_id=123, text='878')

    r = count_m(123)

    print(r)