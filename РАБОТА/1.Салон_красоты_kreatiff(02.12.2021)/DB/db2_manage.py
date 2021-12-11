import sqlite3 as sq

with sq.connect('DB/database2.db') as con:
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS order_face(name TEXT, master TEXT, sms_1 TEXT, sms_2 TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS order_lash(name TEXT, master TEXT, sms_1 TEXT, sms_2 TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS order_brow(name TEXT, master TEXT, sms_1 TEXT, sms_2 TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS order_man(name TEXT, master TEXT, sms_1 TEXT, sms_2 TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS order_depil(name TEXT, master TEXT, sms_1 TEXT, sms_2 TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS order_bar(name TEXT, master TEXT, sms_1 TEXT, sms_2 TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS order_care(name TEXT, master TEXT, sms_1 TEXT, sms_2 TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS order_else(name TEXT, master TEXT, sms_1 TEXT, sms_2 TEXT)')

async def shablon_show_order(table):
    return cur.execute(f'SELECT name, master FROM {table}').fetchall()

