import sqlite3 as sq
import time

with sq.connect('orders_database_archive.db') as con:
    cur = con.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS memory_p (main_data TEXT, user_id TEXT, someelse TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS memory_d (main_data TEXT, user_id TEXT, someelse TEXT)')

with sq.connect('orders_database_archive.db') as con:
    cur = con.cursor()

    cur.execute(f'SELECT main_data FROM memory_p WHERE user_id LIKE "{chat_id}%"')
    n = cur.fetchall()
    print(n)
    update.callback_query.edit_message_text(text=n[0],
                                            parse_mode=ParseMode.MARKDOWN)
    return