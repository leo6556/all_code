import sqlite3 as sq

with sq.connect('DB/database3.db') as con:
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS order_b(user_id TEXT, order_num TEXT, order_service TEXT, order_date TEXT, order_time, order_master TEXT, order_number TEXT, sms_1 TEXT, sms_2 TEXT)')

async def save_order(v1,v2,v3,v4,v5,v6,v7):
    cur.execute(f'INSERT INTO order_b (user_id, order_num, order_service,'
                f'order_date, order_time, order_master, order_number) VALUES("{v1}", "{v2}", "{v3}", "{v4}"'
                f', "{v5}", "{v6}", "{v7}")')
    con.commit()

async def show_right_order(id):
    return cur.execute('SELECT user_id, order_num, order_service,'
                f'order_date, order_time, order_master, order_number FROM order_b WHERE {id} = user_id').fetchall()

async def del_order(order_num):
    cur.execute(f'DELETE FROM order_b WHERE order_num = {order_num}')
    con.commit()