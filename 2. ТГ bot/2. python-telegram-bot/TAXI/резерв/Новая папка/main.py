from telegram import Update
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import ParseMode
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import CallbackContext
from telegram.ext import ConversationHandler
from telegram.ext import MessageHandler
from telegram.ext import CommandHandler
from telegram.ext import CallbackQueryHandler

import sqlite3 as sq
import time, random

# with sq.connect('driver_database.db') as con:
#     cur = con.cursor()
#
#     cur.execute('CREATE TABLE IF NOT EXISTS user (user_id TEXT, busy INTEGER, name TEXT, car TEXT, number INTEGER, time TEXT, from_1 TEXT, where_1 TEXT, sale TEXT )')

    # cur.execute('INSERT INTO user VALUES ("ИВАН", 243)')

# with sq.connect('driver_data.db') as con:
#     cur = con.cursor()
#
#     cur.execute('CREATE TABLE IF NOT EXISTS user_data (main_data TEXT, user_id TEXT, who_data TEXT, have INTEGER DEFAULT 0, some TEXT)')


# with sq.connect('orders_database.db') as con:
#     cur = con.cursor()
#
#     cur.execute('CREATE TABLE IF NOT EXISTS ordersa (user_id TEXT, car TEXT, name TEXT, valid INTEGER, number TEXT, time TEXT, from_2 TEXT, where_2 TEXT, price INT)')

FROM1, FROM1_2, FROM1_3, WHERE1, TIME1, TIME1_1, OFFER1, PAYMENT1, END1, PHONE1 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 630828
PAYMENT2, WHERE2,  TIME2,  FROM2, CAR2, CAR2_1, CAR2_2 = 99,88,10,11,12, 13, 14
END2, END2_2, WHO = 15, 16, 17
DAY = 897
MODEL, NUMBER_CAR, PHONE = 45,46,47
ROWID1, ROWID2, ROWID3, ROWID4 = 55,56,57,58
WHERE_1, WHERE_2, WHERE_3, WHERE_4 = 101,102,103,104
THIS_IS = 1000
ALL_ORDER = 900
TEXTU, TEXTU2 = 5784, 30945816
BRIEF_MODEL, BRIEF_PHONE, BRIEF2_FROM2 =487996,56567863, 839
fps = 19090
MYORDERS= 89348438475897
SPARE1, BRIEF2 = 7348, 897897567


def main_database():

    # Записи сегодняшних поездок в архив

    with sq.connect('orders_database.db') as con:
        cur = con.cursor()

        cur.execute('SELECT * from ordersa')
        n = cur.fetchall()
        l = len(n)

        for i in range(l):
            io = n[i]

            with sq.connect('orders_database_archive.db') as con:
                cur = con.cursor()
                cur.execute(f'INSERT INTO ordersa VALUES {io}')

    # Очистка БД поездок-сегодня
    with sq.connect('orders_database.db') as con:
        cur = con.cursor()
#-->>>>>Разобраться работает ли условие rowia > 1 и есть ли вообще необходимость в этом условии#
        cur.execute('DELETE from ordersa WHERE rowid > 1')


    # Перезапись БД поездки-завтра в БД на поездки-сегодня + Очистка БД поездки-завтра

    with sq.connect('orders_database_tomr.db') as con:
        cur = con.cursor()
        cur.execute('SELECT * from ordersa')
        n = cur.fetchall()
        l = len(n)

        for i in range(l):
            io = n[i]

            with sq.connect('orders_database.db') as con:
                cur = con.cursor()
                cur.execute(f'INSERT INTO ordersa VALUES {io}')

    # Очистка БД поездок-завтра
    with sq.connect('orders_database_tomr.db') as con:
        cur = con.cursor()
        cur.execute('DELETE from ordersa WHERE rowid > 1')


    # Удаление потенциальных водителей с БД-сегодня + перезапись с БД-завтра на БД-сегодня + очистка БД-завтра

    with sq.connect('driver_database.db') as con:
        cur = con.cursor()
        cur.execute('DELETE from user WHERE rowid > 1')

    with sq.connect('driver_database_tomr.db') as con:
        cur = con.cursor()

        cur.execute('SELECT user_id, name, car, number, time, from_1, where_1, sale from user')
        n = cur.fetchall()
        print(n)
        l = len(n)
        print(l)

        for i in range(l):
            io = n[i]

            with sq.connect('driver_database.db') as con:
                cur = con.cursor()
                cur.execute(f'INSERT INTO user (user_id, name, car, number, time, from_1, where_1, sale)  VALUES {io}')

    with sq.connect('driver_database_tomr.db') as con:
        cur = con.cursor()
        cur.execute('DELETE from user WHERE rowid > 1')

def clean_db():
    # Очистка БД поездок-сегодня
    with sq.connect('orders_database.db') as con:
        cur = con.cursor()
        cur.execute('DELETE from ordersa')

    # Очистка БД поездок-завтра
    with sq.connect('orders_database_tomr.db') as con:
        cur = con.cursor()
        cur.execute('DELETE from ordersa')

    with sq.connect('driver_database_tomr.db') as con:
        cur = con.cursor()
        cur.execute('DELETE from user')

    with sq.connect('driver_database.db') as con:
        cur = con.cursor()
        cur.execute('DELETE from user')

# Cинхронизация БД со временем

def sinc():


    with sq.connect('update_database.db') as con:
        cur = con.cursor()
        cur.execute('SELECT * FROM user')
        n = cur.fetchall()

        t = time.asctime()
        print(t)
        m_1 = t[4:7]
        t = t[8:10]
        t_1 = t.replace(' ', '')

        # print(len(m_1), len(n[0][1]))
        # print(len(t_1), len(n[0][0]))

        if m_1 == n[0][1] and t_1 == n[0][0]:
            return

        if int(t_1) - int(n[0][0]) == 1 and n[0][1] == m_1:
            main_database()
            #     Записать новую дату и месяц в БД
            with sq.connect('update_database.db') as con:
                cur = con.cursor()
                cur.execute(f'UPDATE user SET day = "{t_1}", month = "{m_1}"')

        elif m_1 != n[0][1]:
            main_database()
            with sq.connect('update_database.db') as con:
                cur = con.cursor()
                cur.execute(f'UPDATE user SET day = "{t_1}", month = "{m_1}"')
        else:
            # -->># Очистиь все БД (логично ли???)
            clean_db()
            with sq.connect('update_database.db') as con:
                cur = con.cursor()
                cur.execute(f'UPDATE user SET day = "{t_1}", month = "{m_1}"')



def echo(update:Update, context:CallbackContext):

    # Cинхронизация БД со временем
    sinc()

    name = update.message.chat.full_name

    text = [
        f'*Доброго времени суток*, {name} 😊',
        'Пока в новом Садовом не проложили   общественный транспорт, здесь ты можешь найти водителя или стать им',
        '',
        "Выбери нужную операцию (просто нажми на //команду):",
        "",
        "🤝 /drive - оставить заявку (водитель\пассажир)",
        "",
        "📋 /myorder -- мои заказы",
        "",
        "💁‍♀️/help -- помощь",
        "",
        "💳 /donations -- поддержать",
        "",
    ]
    update.message.reply_text(text='\n'.join(text),
                              parse_mode=ParseMode.MARKDOWN)

def donat(update:Update, context:CallbackContext):
    # Cинхронизация БД со временем
    sinc()

    text = [
        '💈 Размещение ТГ-бота на сервере VDSina обходится в 30-40$ в месяц',
        'поэтому приветствуется любая поддержка 😎',
        '*Сбербанк:* 5469-4400-2801-9256'
    ]

    update.message.reply_text(text='\n'.join(text),
                              parse_mode=ParseMode.MARKDOWN)

def helping(update:Update, context:CallbackContext):

    texp = [
        '📍 Список команд: /drive, /myorder, /help, /donations',
        '📍 Для того, чтобы активировать команду можно: или нажать прямо на команду (она выделеяется синим '
        'шрифтом) или отправить команду обычной клавиатурой.',
        '📍 Пожелания для улучшения сервиса и отладки ошибок можете направлять на контакт: @admin_tg'

    ]
    update.message.reply_text(text ='\n'.join(texp))

def my_order_main(update:Update, context:CallbackContext):

    markup = InlineKeyboardMarkup(
        inline_keyboard= [
            [
                InlineKeyboardButton('Водитель 👨‍✈️', callback_data='driv'),
                InlineKeyboardButton('Пассажир 💁‍♀️', callback_data='pass')
            ]
        ]
    )
    update.message.reply_text('Вы хотите посмотреть заказ, вы в нем?',
                              reply_markup=markup)

def callback_for_order(update:Update, context:CallbackContext):

    # Cинхронизация БД со временем
    sinc()

    data = update.callback_query.data
    print(data)

    if data == 'pass':

        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton('Подтвердить заказ', callback_data='ending'),
                    InlineKeyboardButton('Отменить', callback_data='stop'),
                ]
            ]
        )

        chat_id = update.effective_message.chat_id

        with sq.connect('orders_database.db') as con:

            cur = con.cursor()

            cur.execute(f'SELECT * from ordersa WHERE user_id LIKE "%{chat_id}" and valid = 0')

            n = cur.fetchall()

            if len(n) == 0:
                context.user_data[MYORDERS] = 8899
            if len(n) > 0:
                context.user_data[TEXTU] = n[0][0][:10]
                context.user_data[TEXTU2] = n[0][0][10:]
            # print(n)

            for i in n:
                print(i)

                text = [
                    f'*Ваш  Заказ:* #{i[-1][2:]}',
                    f'',
                    f'*Машина:* {i[1]}',
                    f'*Отправление:*{i[2]} с {i[6]} в {i[5]} до {i[-2]}',
                    f'*Оплата:* {i[-1][:2]}р. наличными водителю',
                    f'*Номер водителя для связи:* {i[4]}'
                ]

                if 'бесплатно' in i[-1]:
                    print(888)
                    text = [
                        f'*Ваш  Заказ:* #{i[-1][-4:]}',
                        f'',
                        f'*Машина:* {i[1]}',
                        f'*Отправление:*{i[2]} с {i[6]} в {i[5]} до {i[-2]}',
                        f'*Оплата:* бесплатно',
                        f'*Номер водителя для связи:* {i[4]}'
                    ]

                update.callback_query.edit_message_text(text='\n'.join(text),
                                          reply_markup=markup,
                                          parse_mode=ParseMode.MARKDOWN)

            with sq.connect('orders_database_tomr.db') as con:

                cur = con.cursor()

                cur.execute(f'SELECT * from ordersa WHERE user_id LIKE "%{chat_id}" and valid = 0')

                n = cur.fetchall()

                if len(n) == 0 and context.user_data[MYORDERS] == 8899:
                    update.callback_query.edit_message_text('У вас нет заказов')
                print(111)
                if len(n) > 0:
                    context.user_data[TEXTU] = n[0][0][:10]
                    context.user_data[TEXTU2] = n[0][0][10:]
                # print(len(n))

                for i in n:
                    print(i)

                    text = [
                        f'*Ваш заказ:* #{i[-1][2:]}',
                        f'',
                        f'*Машина:* {i[1]}',
                        f'*Отправление:*{i[2]} с {i[6]} в {i[5]} до {i[-2]}',
                        f'*Оплата:* {i[-1][:2]}р. наличными водителю',
                        f'*Номер водителя для связи:* {i[4]}'
                    ]

                    if 'бесплатно' in i[-1]:
                        print(9999)
                        text = [
                            f'*Ваш заказ:* #{i[-1][-4:]}',
                            f'',
                            f'*Машина:* {i[1]}',
                            f'*Отправление:*{i[2]} с {i[6]} в {i[5]} до {i[-2]}',
                            f'*Оплата:* бесплатно',
                            f'*Номер водителя для связи:* {i[4]}'
                        ]
                    # if len(text) < 10:
                    #     print(99999)

                    update.callback_query.edit_message_text(text='\n'.join(text),
                                              reply_markup=markup,
                                              parse_mode=ParseMode.MARKDOWN)

    elif data == 'driv':
        # markup = InlineKeyboardMarkup(
        #     inline_keyboard=[
        #         [
        #             InlineKeyboardButton('Подтвердить заказ', callback_data='ending'),
        #             InlineKeyboardButton('Отменить', callback_data='stop'),
        #         ]
        #     ]
        # )
        # chat_id = update.effective_message.chat_id

        # with sq.connect('driver_data.db') as con:
        #     cur = con.cursor()
        #     cur.execute('SELECT user_id FROM user_data')
        #     g = cur.fetchall()
        #
        #     for i in g:
        #         if i[0] == str(chat_id):
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton('Подтвердить заказ', callback_data='ending2'),
                    InlineKeyboardButton('Отменить', callback_data='stop2'),
                ]
            ]
        )

        chat_id = update.effective_message.chat_id
        print(chat_id)

        with sq.connect('orders_database.db') as con:

            cur = con.cursor()

            cur.execute(f'SELECT * from ordersa WHERE user_id LIKE "{chat_id}%" and valid = 0')

            n = cur.fetchall()

            if len(n) == 0:
                context.user_data[MYORDERS] = 8899
            if len(n) != 0:
                context.user_data[MYORDERS] = 88998
            if len(n) > 0:
                context.user_data[TEXTU] = n[0][0][:10]
                context.user_data[TEXTU2] = n[0][0][10:]
            # print(n)

            for i in n:
                print(i)

                text = [
                    f'*Ваш  Заказ:* #{i[-1][2:]}',
                    f'',
                    f'*Машина:* {i[1]}',
                    f'*Отправление:*{i[2]} с {i[6]} в {i[5]} до {i[-2]}',
                    f'*Оплата:* {i[-1][:2]}р. наличными с пассажира',
                ]

                if 'бесплатно' in i[-1]:
                    print(888)
                    text = [
                        f'*Ваш  Заказ:* #{i[-1][-4:]}',
                        f'',
                        f'*Машина:* {i[1]}',
                        f'*Отправление:*{i[2]} с {i[6]} в {i[5]} до {i[-2]}',
                        f'*Оплата:* бесплатно',
                    ]

                update.callback_query.edit_message_text(text='\n'.join(text),
                                                        reply_markup=markup,
                                                        parse_mode=ParseMode.MARKDOWN)

            with sq.connect('orders_database_tomr.db') as con:

                cur = con.cursor()

                cur.execute(f'SELECT * from ordersa WHERE user_id LIKE "{chat_id}%" and valid = 0')

                n = cur.fetchall()

                if len(n) == 0 and context.user_data[MYORDERS] == 8899:
                    update.callback_query.edit_message_text('У вас нет заказов\n\n📌Заказ появится, когда пассажир выберет вашу заявку')
                print(111)
                if len(n) > 0:
                    context.user_data[TEXTU] = n[0][0][:10]
                    context.user_data[TEXTU2] = n[0][0][10:]

                for i in n:
                    print(i)

                    text = [
                        f'*Ваш заказ:* #{i[-1][2:]}',
                        f'',
                        f'*Машина:* {i[1]}',
                        f'*Отправление:*{i[2]} с {i[6]} в {i[5]} до {i[-2]}',
                        f'*Оплата:* {i[-1][:2]}р. наличными с пассажира',
                    ]

                    if 'бесплатно' in i[-1]:
                        text = [
                            f'*Ваш заказ:* #{i[-1][-4:]}',
                            f'',
                            f'*Машина:* {i[1]}',
                            f'*Отправление:*{i[2]} с {i[6]} в {i[5]} до {i[-2]}',
                            f'*Оплата:* бесплатно',
                        ]
                    # if len(text) < 10:
                    #     print(99999)

                    update.callback_query.edit_message_text(text='\n'.join(text),
                                                            reply_markup=markup,
                                                            parse_mode=ParseMode.MARKDOWN)

# ***************Ветка callback-ов для пассажиров*********
    if data == 'ending':

        true_text = update.effective_message.text

        markup = InlineKeyboardMarkup(
            inline_keyboard= [
                [
                    InlineKeyboardButton('Да', callback_data='yes1'),
                    InlineKeyboardButton('Назад', callback_data='back1')
                ]
            ]
        )


        update.callback_query.edit_message_text(text = true_text + '\n\n' + '*Поездка прошла успешно?*',
                                                reply_markup=markup,
                                                parse_mode=ParseMode.MARKDOWN)
        return callback_for_order

    elif data == 'stop':

        true_text = update.effective_message.text

        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton('Да', callback_data='yes1_2'),
                    InlineKeyboardButton('Назад', callback_data='back1_2')
                ]
            ]
        )

        update.callback_query.edit_message_text(text = true_text + '\n\n' +
                                                       '*Отменить заказ?  Мы оповестим об этом водителя*',
                                                reply_markup=markup,
                                                parse_mode=ParseMode.MARKDOWN)

    elif data == 'back1':

        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton('Подтвердить заказ', callback_data='ending'),
                    InlineKeyboardButton('Отменить', callback_data='stop'),
                ]
            ]
        )

        true_text = update.effective_message.text

        update.callback_query.edit_message_text(text=true_text[:-24], reply_markup=markup)
        return callback_for_order

    elif data == 'back1_2':

        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton('Подтвердить заказ', callback_data='ending'),
                    InlineKeyboardButton('Отменить', callback_data='stop'),
                ]
            ]
        )

        true_text = update.effective_message.text

        update.callback_query.edit_message_text(text=true_text[:-47], reply_markup=markup)
        return callback_for_order

    elif data == 'yes1':

        this_yext = update.effective_message.text

        truly_text = update.effective_message.text
        print(truly_text[12:16])
        ll = truly_text.split('Отправление:')
        print(ll)

        update.callback_query.edit_message_text('Спасибо, ждем вас еще ☺️')

        if truly_text[4] == ' ':
            with sq.connect('orders_database.db') as con:
                cur = con.cursor()
                cur.execute(f'DELETE FROM ordersa WHERE price LIKE "%{truly_text[13:17]}"')
        if truly_text[4] == 'з':
            with sq.connect('orders_database_tomr.db') as con:
                cur = con.cursor()
                cur.execute(f'DELETE FROM ordersa WHERE price LIKE "%{truly_text[12:16]}"')

    elif data == 'yes1_2':

        truly_text = update.effective_message.text
        ll = truly_text.split('Отправление:')
        tt = ll[1].split(' ')
        text_for_driver = ''

        for i in range(6):
            text_for_driver = text_for_driver + tt[i] + ' '


        truly_text = update.effective_message.text
        print(truly_text[12:16])

        update.callback_query.edit_message_text('Спасибо, ждем вас еще ☺️')

        if truly_text[4] == ' ':
            with sq.connect('orders_database.db') as con:
                cur = con.cursor()
                cur.execute(f'DELETE FROM ordersa WHERE price LIKE "%{truly_text[13:17]}"')

        if truly_text[4] == 'з':
            with sq.connect('orders_database_tomr.db') as con:
                cur = con.cursor()
                cur.execute(f'DELETE FROM ordersa WHERE price LIKE "%{truly_text[12:16]}"')

        context.bot.send_message(text=f'Пассажир только что отменил заказ ({text_for_driver}), поездка не состоится.',
                                 chat_id=context.user_data[TEXTU])

# ***************Ветка callback-ов для водителей*********
    if data == 'ending2':

        true_text = update.effective_message.text

        markup = InlineKeyboardMarkup(
            inline_keyboard= [
                [
                    InlineKeyboardButton('Да', callback_data='yes2'),
                    InlineKeyboardButton('Назад', callback_data='back2')
                ]
            ]
        )


        update.callback_query.edit_message_text(text = true_text + '\n\n' + '*Поездка прошла успешно?*',
                                                reply_markup=markup,
                                                parse_mode=ParseMode.MARKDOWN)
        return callback_for_order

    elif data == 'stop2':

        true_text = update.effective_message.text

        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton('Да', callback_data='yes2_2'),
                    InlineKeyboardButton('Назад', callback_data='back2_2')
                ]
            ]
        )

        update.callback_query.edit_message_text(text = true_text + '\n\n' +
                                                       '*Отменить заказ?  Мы оповестим об этом пассажира*',
                                                reply_markup=markup,
                                                parse_mode=ParseMode.MARKDOWN)

    elif data == 'back2':

        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton('Подтвердить заказ', callback_data='ending2'),
                    InlineKeyboardButton('Отменить', callback_data='stop2'),
                ]
            ]
        )

        true_text = update.effective_message.text

        update.callback_query.edit_message_text(text=true_text[:-24], reply_markup=markup)
        return callback_for_order

    elif data == 'back2_2':

        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton('Подтвердить заказ', callback_data='ending2'),
                    InlineKeyboardButton('Отменить', callback_data='stop2'),
                ]
            ]
        )

        true_text = update.effective_message.text

        update.callback_query.edit_message_text(text=true_text[:-47], reply_markup=markup)
        return callback_for_order

    elif data == 'yes2':

        this_yext = update.effective_message.text

        truly_text = update.effective_message.text
        print(truly_text[12:16])
        ll = truly_text.split('Отправление:')
        print(ll)

        update.callback_query.edit_message_text('Спасибо, ждем вас еще ☺️')

        if truly_text[4] == ' ':
            with sq.connect('orders_database.db') as con:
                cur = con.cursor()
                cur.execute(f'DELETE FROM ordersa WHERE price LIKE "%{truly_text[13:17]}"')
        if truly_text[4] == 'з':
            with sq.connect('orders_database_tomr.db') as con:
                cur = con.cursor()
                cur.execute(f'DELETE FROM ordersa WHERE price LIKE "%{truly_text[12:16]}"')

    elif data == 'yes2_2':

        truly_text = update.effective_message.text
        ll = truly_text.split('Отправление:')
        tt = ll[1].split(' ')
        text_for_driver = ''

        for i in range(6):
            text_for_driver = text_for_driver + tt[i] + ' '


        truly_text = update.effective_message.text
        print(truly_text[12:16])

        update.callback_query.edit_message_text('Спасибо, ждем вас еще ☺️')

        if truly_text[4] == ' ':
            with sq.connect('orders_database.db') as con:
                cur = con.cursor()
                cur.execute(f'DELETE FROM ordersa WHERE price LIKE "%{truly_text[13:17]}"')

        if truly_text[4] == 'з':
            with sq.connect('orders_database_tomr.db') as con:
                cur = con.cursor()
                cur.execute(f'DELETE FROM ordersa WHERE price LIKE "%{truly_text[12:16]}"')

        context.bot.send_message(text=f'Водитель только что отменил заказ ({text_for_driver}), поездка не состоится.',
                                 chat_id=context.user_data[TEXTU2])

# Ветка для регистрации водителя\пассажира

def start_conv(update:Update, context: CallbackContext):


    # Cинхронизация БД со временем
    sinc()

    markup = InlineKeyboardMarkup(
        inline_keyboard= [
            [
                InlineKeyboardButton("Водитель 🚘", callback_data='driver'),
                InlineKeyboardButton("Пассажир 🙎‍♀️", callback_data='passanger')
            ]
        ]
    )

    update.message.reply_text('Вы совершате поездку как:',
                              reply_markup=markup)

    return DAY


def tomorrow(update:Update, context:CallbackContext):

    data = update.callback_query.data

    context.user_data[WHO] = data

    markup = InlineKeyboardMarkup(
        inline_keyboard= [
            [
                InlineKeyboardButton('Cегодня', callback_data='today'),
                InlineKeyboardButton('Завтра', callback_data='tomorrow')
            ]
        ]
    )

    update.callback_query.edit_message_text('Вы планируете поездку 🏄‍♂️',
                              reply_markup=markup)

    return WHERE1

def where_p (update:Update, context:CallbackContext):

    data = update.callback_query.data
    context.user_data[DAY] = data

    if context.user_data[WHO] == 'driver':
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton('Бесплатно', callback_data='free'),
                    InlineKeyboardButton('Платно', callback_data='paid')
                ]
            ]
        )

        update.callback_query.edit_message_text('Как собираетесь везти пассажира? 🤔\n'
                                                '*Примечание:* За поездку до магнита вы получите 50р,'
                                                ' до города 80р.',
                                                reply_markup=markup,
                                                parse_mode=ParseMode.MARKDOWN)

        return WHERE2


    markup = InlineKeyboardMarkup(
        inline_keyboard= [
            [
                InlineKeyboardButton('Магнит ', callback_data='magnit'),
                InlineKeyboardButton('Город ', callback_data='city')
            ]
        ]
    )

    update.callback_query.edit_message_text('Какой ваш конечный пункт? 📌'
                                            '\n'
                                            '🔻*Примечание:*'
                                            ' до города - (минимум до ул. Жуковского), дальше - на усмотрение водителя',
                                            reply_markup=markup,
                                            parse_mode=ParseMode.MARKDOWN)

    return TIME1

def time_p(update:Update, context:CallbackContext):

    data = update.callback_query.data
    context.user_data[WHERE1] = data

    markup = InlineKeyboardMarkup(
        inline_keyboard= [
            [
                InlineKeyboardButton('В точное время', callback_data='one'),
                InlineKeyboardButton('Промежуток', callback_data='two')
            ],
            [
                InlineKeyboardButton('Приостановить заказ', callback_data='stopall')
            ]
        ]
    )

    update.callback_query.edit_message_text('*Вам нужно выехать?* ⏳'
                                            '\n'
                                            '*Примечание:* Если вы не едете в город или в магазин к определенному времени, выберите "в промежуток"',

                                            reply_markup=markup,
                                            parse_mode=ParseMode.MARKDOWN)

    return TIME1_1

def time_p1(update:Update, context:CallbackContext):

    data = update.callback_query.data

    if data == 'stopall':
        return fallbacks_end(update=update, context=context)

    if data == 'one':

        list_time = ['06:00', '06:30', '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', '10:00', '10:30',
                     '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30'
                     , '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30']

        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(f'{i}', callback_data=f'time{i}') for i in list_time[:5]
                ],
                [
                    InlineKeyboardButton(f'{i}', callback_data=f'time{i}') for i in list_time[5:10]
                ],
                [
                    InlineKeyboardButton(f'{i}', callback_data=f'time{i}') for i in list_time[10:15]
                ],
                [
                    InlineKeyboardButton(f'{i}', callback_data=f'time{i}') for i in list_time[15:20]
                ],
                [
                    InlineKeyboardButton(f'{i}', callback_data=f'time{i}') for i in list_time[20:25]
                ],
                [
                    InlineKeyboardButton(f'{i}', callback_data=f'time{i}') for i in list_time[25:30]
                ],
                [
                    InlineKeyboardButton('Приостановить заказ', callback_data='stopall')
                ]
            ]
        )

        update.callback_query.edit_message_text('🕗 Выберите время (с расчетом +-15 минут)', reply_markup=markup)

    elif data == 'two':
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton('Утром', callback_data='morning'),
                    InlineKeyboardButton('Днем', callback_data='daytime'),
                    InlineKeyboardButton('Вечером', callback_data='evening')
                ],
                [
                    InlineKeyboardButton('Приостановить заказ', callback_data='stopall')
                ]

            ]
        )

        text = [
            '*Выберите промежуток времени:*',
            '💈 утро - с 8:00 до 12:00',
            '💈 день - с 12:00 до 16:00',
            '💈 вечер - с 16:00 до 20:00',
            '',
        ]

        update.callback_query.edit_message_text(text='\n'.join(text),
                                                reply_markup=markup,
                                                parse_mode=ParseMode.MARKDOWN)

    return FROM1

def from_p(update:Update, context:CallbackContext):

    data = update.callback_query.data
    context.user_data[TIME1] = data

    if data == 'stopall':
        return fallbacks_end(update=update, context=context)

    chat_id = update.effective_message.chat_id
    id = update.effective_message.message_id

    mark_up = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('1: МАГНИТ', callback_data='маг.Магнит'),
                InlineKeyboardButton('5: ул. Янтарная', callback_data="ул.Янтарная")

            ],
            [
                InlineKeyboardButton('2: ул. Стартовая', callback_data="ул.Стартовая"),
                InlineKeyboardButton("6: ул. Снежная", callback_data="ул.Снежная")
            ],
            [
                InlineKeyboardButton("3: ул. Майская", callback_data="ул.Майская"),
                InlineKeyboardButton("7: ул. Ягодная", callback_data="ул.Ягодная")
            ],
            [
                InlineKeyboardButton('4: ул. Семейная', callback_data="ул.Семейная"),
                InlineKeyboardButton("8: ул. Байкальская", callback_data="ул.Байкальская")
            ],
            [
                InlineKeyboardButton("Назад", callback_data="back"),
                InlineKeyboardButton("Дальше", callback_data="next")
            ],

        ],

    )

    context.bot.delete_message(chat_id=chat_id, message_id = id )

    context.bot.send_photo(chat_id=chat_id, photo=open("sad_1.JPG", "rb"),
                           caption='Выберите улицу отправления:',
                           reply_markup=mark_up)
    context.user_data[fps] = 2

    return OFFER1

def offer_p(update:Update, context:CallbackContext):

    data = update.callback_query.data

    if data[:4] == 'next':

        if data == 'next':

            chat_id = update.effective_message.chat_id
            id = update.effective_message.message_id

            mark_up = InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton('9: ул. Веселая', callback_data='ул.Веселая'),
                        InlineKeyboardButton('13: ул. Учительская', callback_data="ул.Учительская"),
                    ],
                    [
                        InlineKeyboardButton('10: ул. Новосибирская', callback_data="ул.Новосибирская"),
                        InlineKeyboardButton("14: ул. Жемчужная", callback_data="ул.Жемчужная")
                    ],
                    [
                        InlineKeyboardButton("11: ул. Спортивная", callback_data="ул.Спортивная"),
                        InlineKeyboardButton("15: ул. Славянская", callback_data="ул.Славянская"),
                    ],
                    [
                        InlineKeyboardButton('12: ул. Торговая', callback_data="ул.Торговая"),
                        InlineKeyboardButton("16: ул. Красивая", callback_data="ул.Красивая")
                    ],
                    [
                        InlineKeyboardButton("Назад", callback_data="back2"),
                        InlineKeyboardButton("Дальше", callback_data="next2")
                    ]
                ],

            )

            context.bot.delete_message(chat_id=chat_id, message_id=id)

            context.bot.send_photo(chat_id=chat_id, photo=open("sad_2.JPG", "rb"),
                                   caption='Выберите улицу отправления:',
                                   reply_markup=mark_up)

            return OFFER1
        elif data == 'next2':
            chat_id = update.effective_message.chat_id
            id = update.effective_message.message_id

            mark_up = InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton('17: ул. Луговая', callback_data='ул.Луговая'),
                        InlineKeyboardButton("24: ул. Дружбы", callback_data="ул.Дружбы")
                    ],
                    [
                        InlineKeyboardButton('18: ул. Транспортная', callback_data="ул.Транспортная"),
                        InlineKeyboardButton('25: ул. Русская', callback_data='ул.Русская'),
                    ],
                    [
                        InlineKeyboardButton("19: ул. Калиновая", callback_data="ул.Калиновая"),
                        InlineKeyboardButton('26: ул. Линейная', callback_data="ул.Линейная")
                    ],
                    [
                        InlineKeyboardButton('20: ул. Душистая', callback_data="ул.Душистая"),
                        InlineKeyboardButton("27: ул. Рабочая", callback_data="ул.Рабочая"),
                    ],
                    [
                        InlineKeyboardButton('21: ул. Праздничная', callback_data="ул.Праздничная"),
                        InlineKeyboardButton('28: ул. Речная', callback_data="ул.Речная")
                    ],
                    [
                        InlineKeyboardButton("22: ул. Некрасова", callback_data="ул.Некрасова"),
                        InlineKeyboardButton('29: ул. Обская', callback_data="ул.Обская"),
                    ],
                    [
                        InlineKeyboardButton("23: ул. Геодезическая", callback_data="ул.Геодезическая"),
                        InlineKeyboardButton('30: ул. Областная', callback_data="ул.Областная")

                    ],
                    [
                        InlineKeyboardButton("Назад", callback_data="back3"),
                        InlineKeyboardButton("Дальше", callback_data="next3")
                    ]
                ],

            )

            context.bot.delete_message(chat_id=chat_id, message_id=id)

            context.bot.send_photo(chat_id=chat_id, photo=open("sad_3.JPG", "rb"),
                                   caption='Выберите улицу отправления:',
                                   reply_markup=mark_up)

            return OFFER1

        elif data == 'next3':
            chat_id = update.effective_message.chat_id
            id = update.effective_message.message_id

            mark_up = InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton('1: МАГНИТ', callback_data='маг.Магнит'),
                        InlineKeyboardButton('5: ул. Янтарная', callback_data="ул.Янтарная")

                    ],
                    [
                        InlineKeyboardButton('2: ул. Стартовая', callback_data="ул.Стартовая"),
                        InlineKeyboardButton("6: ул. Снежная", callback_data="ул.Снежная")
                    ],
                    [
                        InlineKeyboardButton("3: ул. Майская", callback_data="ул.Майская"),
                        InlineKeyboardButton("7: ул. Ягодная", callback_data="ул.Ягодная")
                    ],
                    [
                        InlineKeyboardButton('4: ул. Семейная', callback_data="ул.Семейная"),
                        InlineKeyboardButton("8: ул. Байкальская", callback_data="ул.Байкальская")
                    ],
                    [
                        InlineKeyboardButton("Назад", callback_data="back"),
                        InlineKeyboardButton("Дальше", callback_data="next")
                    ]
                ],

            )

            context.bot.delete_message(chat_id=chat_id, message_id=id)

            context.bot.send_photo(chat_id=chat_id, photo=open("sad_1.JPG", "rb"),
                                   caption='Выберите улицу отправления:',
                                   reply_markup=mark_up)

            return OFFER1

    if data[:4] == 'back':

        if data == 'back':
            chat_id = update.effective_message.chat_id
            id = update.effective_message.message_id

            mark_up = InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton('17: ул. Луговая', callback_data='ул.Луговая'),
                        InlineKeyboardButton("24: ул. Дружбы", callback_data="ул.Дружбы")
                    ],
                    [
                        InlineKeyboardButton('18: ул. Транспортная', callback_data="ул.Транспортная"),
                        InlineKeyboardButton('25: ул. Русская', callback_data='ул.Русская'),
                    ],
                    [
                        InlineKeyboardButton("19: ул. Калиновая", callback_data="ул.Калиновая"),
                        InlineKeyboardButton('26: ул. Линейная', callback_data="ул.Линейная")
                    ],
                    [
                        InlineKeyboardButton('20: ул. Душистая', callback_data="ул.Душистая"),
                        InlineKeyboardButton("27: ул. Рабочая", callback_data="ул.Рабочая"),
                    ],
                    [
                        InlineKeyboardButton('21: ул. Праздничная', callback_data="ул.Праздничная"),
                        InlineKeyboardButton('28: ул. Речная', callback_data="ул.Речная")
                    ],
                    [
                        InlineKeyboardButton("22: ул. Некрасова", callback_data="ул.Некрасова"),
                        InlineKeyboardButton('29: ул. Обская', callback_data="ул.Обская"),
                    ],
                    [
                        InlineKeyboardButton("23: ул. Геодезическая", callback_data="ул.Геодезическая"),
                        InlineKeyboardButton('30: ул. Областная', callback_data="ул.Областная")

                    ],
                    [
                        InlineKeyboardButton("Назад", callback_data="back3"),
                        InlineKeyboardButton("Дальше", callback_data="next3")
                    ]
                ],

            )

            context.bot.delete_message(chat_id=chat_id, message_id=id)

            context.bot.send_photo(chat_id=chat_id, photo=open("sad_3.JPG", "rb"),
                                   caption='Выберите улицу отправления:',
                                   reply_markup=mark_up)

            return OFFER1
        elif data == 'back2':
            chat_id = update.effective_message.chat_id
            id = update.effective_message.message_id

            mark_up = InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton('1: МАГНИТ', callback_data='маг.Магнит'),
                        InlineKeyboardButton('5: ул. Янтарная', callback_data="ул.Янтарная")

                    ],
                    [
                        InlineKeyboardButton('2: ул. Стартовая', callback_data="ул.Стартовая"),
                        InlineKeyboardButton("6: ул. Снежная", callback_data="ул.Снежная")
                    ],
                    [
                        InlineKeyboardButton("3: ул. Майская", callback_data="ул.Майская"),
                        InlineKeyboardButton("7: ул. Ягодная", callback_data="ул.Ягодная")
                    ],
                    [
                        InlineKeyboardButton('4: ул. Семейная', callback_data="ул.Семейная"),
                        InlineKeyboardButton("8: ул. Байкальская", callback_data="ул.Байкальская")
                    ],
                    [
                        InlineKeyboardButton("Назад", callback_data="back"),
                        InlineKeyboardButton("Дальше", callback_data="next")
                    ]
                ],

            )

            context.bot.delete_message(chat_id=chat_id, message_id=id)

            context.bot.send_photo(chat_id=chat_id, photo=open("sad_1.JPG", "rb"),
                                   caption='Выберите улицу отправления:',
                                   reply_markup=mark_up)

            return OFFER1
        elif data == 'back3':
            chat_id = update.effective_message.chat_id
            id = update.effective_message.message_id

            mark_up = InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton('9: ул. Веселая', callback_data='ул.Веселая'),
                        InlineKeyboardButton('13: ул. Учительская', callback_data="ул.Учительская"),
                    ],
                    [
                        InlineKeyboardButton('10: ул. Новосибирская', callback_data="ул.Новосибирская"),
                        InlineKeyboardButton("14: ул. Жемчужная", callback_data="ул.Жемчужная")
                    ],
                    [
                        InlineKeyboardButton("11: ул. Спортивная", callback_data="ул.Спортивная"),
                        InlineKeyboardButton("15: ул. Славянская", callback_data="ул.Славянская"),
                    ],
                    [
                        InlineKeyboardButton('12: ул. Торговая', callback_data="ул.Торговая"),
                        InlineKeyboardButton("16: ул. Красивая", callback_data="ул.Красивая")
                    ],
                    [
                        InlineKeyboardButton("Назад", callback_data="back2"),
                        InlineKeyboardButton("Дальше", callback_data="next2")
                    ]
                ],

            )

            context.bot.delete_message(chat_id=chat_id, message_id=id)

            context.bot.send_photo(chat_id=chat_id, photo=open("sad_2.JPG", "rb"),
                                   caption='Выберите улицу отправления:',
                                   reply_markup=mark_up)

            return OFFER1

    update.callback_query.delete_message()

    context.user_data[FROM1] = data

    # переменная для выборки водителей из колбека "точное время"
    a = context.user_data[TIME1][-5:]


    list_time = ['06:00', '06:30', '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', '10:00', '10:30',
                     '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30'
                     , '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30']

    list_street = ['маг.Магнит', "ул.Стартовая", "ул.Майская", "ул.Семейная", "ул.Янтарная",
                   "ул.Снежная", "ул.Ягодная", "ул.Байкальская", 'ул.Веселая', "ул.Новосибирская",
                   "ул.Спортивная", "ул.Торговая", "ул.Учительская", "ул.Жемчужная",
                   "ул.Славянская", "ул.Красивая", 'ул.Луговая', "ул.Транспортная",
                   "ул.Калиновая", "ул.Душистая", "ул.Праздничная", "ул.Некрасова", "ул.Геодезическая",
                   "ул.Дружбы", 'ул.Русская', "ул.Линейная", "ул.Рабочая", "ул.Речная", "ул.Обская",
                   "ул.Областная"]

    # Иницилизация для открытия правильной БД (сегодня\завтра)
    if context.user_data[DAY] == 'today':
        this_DB = 'driver_database.db'
    elif context.user_data[DAY] == 'tomorrow':
        this_DB = 'driver_database_tomr.db'

    # Выборка из колбека "Точное время"

    if context.user_data[TIME1] not in ('morning', 'daytime', 'evening'):

        # ВЫборка из списка временит
        f = list_time.index(a)
        b = list_time[f - 2]
        c = list_time[f - 1]
        d = list_time[f + 1]
        e = list_time[f + 2]


        # ВЫборка из списка улиц
        p = context.user_data[FROM1]
        print(p)
        o = list_street.index(p)
        print(o)

        # if context.user_data[DAY] == 'today':
        #     this_DB = 'driver_database.db'
        # elif context.user_data[DAY] == 'tomorrow':
        #     this_DB = 'driver_database_tomr.db'


        with sq.connect(this_DB) as con:
            cur = con.cursor()
            print(b)

            cur.execute(f"SELECT name, car, number, from_1, time, where_1, sale, rowid FROM user WHERE time in "
                        f"('{b}', '{c}' , '{a}', '{d}', '{e}') ")

            n = cur.fetchall()
            print(n)

    # Выборка из колбека "Промежуток"
    if context.user_data[TIME1] in ('morning', 'daytime', 'evening'):

        # Для ограничения выборки (тех, кто впрошлом)
        t = time.asctime()[11:13]
        t = t + ':30'
        if t[:2] in ('01','02','03','04','05'):
            t = '06:00'


        if context.user_data[TIME1] == 'morning':
            a = list_time.index(t)
            if context.user_data[DAY] == 'tomorrow':
                a = 0

            listik = list_time[a:14]
            # print(tuple(listik))

        elif context.user_data[TIME1] == 'daytime':
            a = list_time.index(t)
            if context.user_data[DAY] == 'tomorrow':
                a = 12
            listik = list_time[a:22]
            # print(listik)
        else:
            listik = list_time[19:]
            # print(listik)

        with sq.connect(this_DB) as con:
            cur = con.cursor()

            cur.execute(f"SELECT name, car, number, from_1, time, where_1, sale, rowid FROM user WHERE time in {tuple(listik)}")

            n = cur.fetchall()

            # Переменная для выборка из списка улиц
            p = context.user_data[FROM1]
            # print(p)
            o = list_street.index(p)
            print(o)


    te = 'Ближайшие варианты к вашему времени 📋'
    l = 1

    for i in n:
        print(i)
        k = f'{i[-3]}а'
        # if context.user_data[WHERE1] == 'magnit':
        #     pay = "50р."
        # elif context.user_data[WHERE1] == 'city':
        #     pay = "80р."
        if context.user_data[WHERE1] == 'city' and i[-3] == 'город':
            pay = "80р."
        else:
            pay = "50р."


        if list_street[o] == i[3]:
            if i[-2] == 'free':
                pay = 'бесплатно'
            if i[-3] == 'город':
                k = 'города (магнит)'
            text_1 = f'*{l}. {i[1]}*, отвозит с {i[3]} в *{i[-4]}* до {k}. *Поездка:* {pay}'

        else:
            if i[-2] == 'free':
                pay = 'бесплатно'
            if i[-3] == 'город':
                k = 'города (магнит)'


            if 0 

            # Выборка улиц на расстоянии +- 900м от пассажира
            o_1 = list_street.index(i[3])
            # print(o_1)
            o_2 = o - o_1
            o_3 = (o_2 * o_2)**0.5
            # print(o_3)
            o_m = o_3 * 90
            # print(o_m)

            if (o < 16 and o_1 > 16) or (o > 16 and o_1 < 16):
                o_m += 500

            if o_m > 990:
                continue

            text_1 = f'*{l}. {i[1]}*, отвозит с {i[3]} ({int(o_m)}м от ваc) в *{i[-4]}* до {k}. *Поездка:* {pay}'

        te = te + '\n' + text_1


        #Запись колбэков чтобы удалить выбранного водителя из БД

        if l == 1:
            context.user_data[ROWID1] = i[-1],i[-2]
            context.user_data[WHERE_1] = i[-3]
        elif l == 2:
            context.user_data[ROWID2] = i[-1],i[-2]
            context.user_data[WHERE_2] = i[-3]
        elif l == 3:
            context.user_data[ROWID3] = i[-1],i[-2]
            context.user_data[WHERE_3] = i[-3]
        elif l == 4:
            context.user_data[ROWID4] = i[-1],i[-2]
            context.user_data[WHERE_4] = i[-3]

        l += 1
        if l == 5:
            break

#--->>>>>ошибка: message to edit not found
    # от бага если не нашлось ни одного водителя
    if len(te) < 42:
        c = context.user_data[TIME1]
        s = ['morning', 'daytime', 'evening']

        if context.user_data[fps] == 7:

            markup = InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton('Отправить', callback_data='send'),
                        InlineKeyboardButton("Не надо", callback_data='nosend')
                    ]
                ]
            )

            update.callback_query.edit_message_text('К сожалению, водителей пока нет 😌 нам отправить вам'
                                                    ' уведомление, когда появятся?',
                                                    reply_markup=markup)
            return SPARE1

        if c in s:
            if c == 'morning':
                context.user_data[TIME1] = 'daytime'
            elif c == 'daytime':
                context.user_data[TIME1] = 'morning'
            elif c == 'evening':
                context.user_data[TIME1] = 'daytime'

        context.user_data[fps] = 7

        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton('Смотреть остальное время', callback_data=f'{context.user_data[FROM1]}'),

                ],
            ]
        )

        update.callback_query.message.reply_text(text='К сожалению пока нет подходящих водителей 😮‍💨',
                                                 reply_markup=markup,
                                                 parse_mode=ParseMode.MARKDOWN)

        return OFFER1

    #  Переменная для подсчета кол-ва выдвнных водителей, чтобы дат нужное кол-во Reply кнопок
    io = te.count(':')

    if io/2 == 1:
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton('1', callback_data=f'{context.user_data[ROWID1][0]}'),
                ],
                [
                    InlineKeyboardButton('Приостановить заказ', callback_data='stopall')
                ]
            ]
        )
    elif io/2 ==  2:
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton('1', callback_data=f'{context.user_data[ROWID1][0]}'),
                    InlineKeyboardButton('2', callback_data=f'{context.user_data[ROWID2][0]}')
                ],
                [
                    InlineKeyboardButton('Приостановить заказ', callback_data='stopall')
                ]
            ]
        )
    elif io/2 == 3:
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton('1', callback_data=f'{context.user_data[ROWID1][0]}'),
                    InlineKeyboardButton('2', callback_data=f'{context.user_data[ROWID2][0]}')
                ],
                [
                    InlineKeyboardButton('3', callback_data=f'{context.user_data[ROWID3][0]}')
                ],
                [
                    InlineKeyboardButton('Приостановить заказ', callback_data='stopall')
                ]
            ]
        )
    elif io/2 == 4:
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton('1', callback_data=f'{context.user_data[ROWID1][0]}'),
                    InlineKeyboardButton('2', callback_data=f'{context.user_data[ROWID2][0]}')
                ],
                [
                    InlineKeyboardButton('3', callback_data=f'{context.user_data[ROWID3][0]}'),
                    InlineKeyboardButton('4', callback_data=f'{context.user_data[ROWID4][0]}')
                ],
                [
                    InlineKeyboardButton('Приостановить заказ', callback_data='stopall')
                ]
            ]
        )

    update.callback_query.message.reply_text(text = te,
                                             reply_markup=markup,
                                             parse_mode=ParseMode.MARKDOWN)

    return PAYMENT1

def  spare_1(update:Update, context:CallbackContext):
    data = update.callback_query.data

    if data == 'stopall':
        return fallbacks_end(update=update, context=context)

    update.callback_query.edit_message_text('Хорошего дня 🤗 до скорого!')

    return ConversationHandler.END

def pay_p(update:Update, context:CallbackContext):

    data = update.callback_query.data
    context.user_data[THIS_IS] = data

    if data == 'stopall':
        return fallbacks_end(update=update, context=context)

    chat_id = update.effective_message.chat_id
    name = update.callback_query.from_user.name

    # Иницилизация для работы с правильной БД (сегодня\завтра)
    if context.user_data[DAY] == 'today':
        this_DB = 'driver_database.db'
        this_order_DB = 'orders_database.db'
    elif context.user_data[DAY] == 'tomorrow':
        this_DB = 'driver_database_tomr.db'
        this_order_DB = 'orders_database_tomr.db'

    with sq.connect(this_DB) as con:
        cur = con.cursor()

        cur.execute(f"SELECT sale, user_id, name"
                    f", car, number, time, from_1, where_1 FROM user WHERE rowid = {data} ")
        n = cur.fetchall()



        if n[0][-1] == 'город' and context.user_data[WHERE1] == 'city':
            pay = 80
            there = 'города'
        else:
            pay = 50
            there = 'магнита'

    # Если поездка бесплатная, пропустить процесс оплатыыуз
    if n[0][0] == 'free':
        update.callback_query.edit_message_text(
        'Заказ сформирован 📦 управлять своими заказами можете по команде /myorder')

        # Записываем в БД заказов(orders)
        with sq.connect(this_order_DB) as con:
            cur = con.cursor()

        #скрипт для даты
            month_day = {'Sep': '30', 'Oct': '31', 'Nov': '30', 'Dec': '31', 'Jan': '31', 'Feb': '28', 'Mar': '31',
                      'Apr': '30', 'May': '31', 'Jun': '30',
                      'Jul': '31', 'Aug': '31'}
            month = {'Sep': 'сен', 'Oct': 'окт', 'Nov': 'нояб', 'Dec': 'дек', 'Jan': 'янв', 'Feb': 'фев', 'Mar': 'мар',
                     'Apr': 'апр', 'May': 'мая', 'Jun': 'июн',
                     'Jul': 'июл', 'Aug': 'авг'}
            month2 = {'Sep': 'окт', 'Oct': 'нояб', 'Nov': 'дек', 'Dec': 'янв', 'Jan': 'фев', 'Feb': 'мар', 'Mar': 'апр',
                      'Apr': 'мая', 'May': 'июн', 'Jun': 'июл',
                      'Jul': 'авг', 'Aug': 'сен'}
            t = time.asctime()
            m_1 = t[4:7]
            t = t[8:10]
            io = t.replace(' ', '')
            t_1 = t.replace(' ', '')
            print(context.user_data[DAY])
            if context.user_data[DAY] == 'tomorrow':
                t_1 = int(t_1) + 1
                t_1 = str(t_1)

            t_m = t_1 + ' ' + month[m_1]
            # print(month_day[m_1])


            if month_day[m_1] == io and context.user_data[DAY] == 'tomorrow':
                t_m = '1 ' + month2[m_1]

            rand = random.randint(1000, 9999)

            cur.execute(f'INSERT INTO ordersa (user_id, car, name, valid, number, time, from_2, where_2'
                        f', price) VALUES ("{n[0][1]}{chat_id}", "{n[0][3]}", "{t_m}", 0, "{n[0][4]}",'
                        f'"{n[0][-3]}", "{n[0][-2]}", "{there}", "бесплатно{rand}") ')

        context.bot.send_message(
            chat_id=n[0][1], text=f'Нашелся пассажир 🥳 Поездка {t_m} в {n[0][-3]} c {n[0][-2]}. Управлять своими '
                                  f'заказами можете по команде /myorder'
        )

        # Удаляем выбранного водителя из БД заявок

        with sq.connect(this_DB) as con:
            cur = con.cursor()

            cur.execute(f'DELETE FROM user WHERE rowid = {data}')

        return ConversationHandler.END

    # Записываем в БД заказов(orders)
    with sq.connect(this_order_DB) as con:
        cur = con.cursor()

        #скрипт для даты
        month_day = {'Sep': '30', 'Oct': '31', 'Nov': '30', 'Dec': '31', 'Jan': '31', 'Feb': '28', 'Mar': '31',
                     'Apr': '30', 'May': '31', 'Jun': '30',
                     'Jul': '31', 'Aug': '31'}
        month = {'Sep': 'сен', 'Oct': 'окт', 'Nov': 'нояб', 'Dec': 'дек', 'Jan': 'янв', 'Feb': 'фев', 'Mar': 'мар',
                 'Apr': 'апр', 'May': 'мая', 'Jun': 'июн',
                 'Jul': 'июл', 'Aug': 'авг'}
        month2 = {'Sep': 'окт', 'Oct': 'нояб', 'Nov': 'дек', 'Dec': 'янв', 'Jan': 'фев', 'Feb': 'мар', 'Mar': 'апр',
                  'Apr': 'мая', 'May': 'июн', 'Jun': 'июл',
                  'Jul': 'авг', 'Aug': 'сен'}
        t = time.asctime()
        m_1 = t[4:7]
        t = t[8:10]
        io = t.replace(' ', '')
        t_1 = t.replace(' ', '')
        print(context.user_data[DAY])
        if context.user_data[DAY] == 'tomorrow':
            t_1 = int(t_1) + 1
            t_1 = str(t_1)

        t_m = t_1 + ' ' + month[m_1]
        # print(month_day[m_1])

        if month_day[m_1] == io and context.user_data[DAY] == 'tomorrow':
            t_m = '1 ' + month2[m_1]

        rand = random.randint(1000, 9999)

        cur.execute(f'INSERT INTO ordersa (user_id, car, name, valid, number, time, from_2, where_2'
                    f', price) VALUES ("{n[0][1]}{chat_id}", "{n[0][3]}", "{t_m}", 0, "{n[0][4]}",'
                    f'"{n[0][-3]}", "{n[0][-2]}", "{there}", "{pay}{rand}") ')

    context.bot.send_message(
        chat_id=n[0][1], text=f'Нашелся пассажир 🥳 Поездка {t_m} в {n[0][-3]} c {n[0][-2]}. Управлять своими заказами '
                              f'можете по команде /myorder'
    )



    # Удаляем выбранного водителя из БД заявок

    with sq.connect(this_DB) as con:
        cur = con.cursor()

        cur.execute(f'DELETE FROM user WHERE rowid = {data}')


    markup = InlineKeyboardMarkup(
        inline_keyboard= [
            [
                InlineKeyboardButton(f'В руки водителя {pay}р.', callback_data="pppp"),
                # InlineKeyboardButton('Оплата онлайн\n(59р.)', callback_data='pppo')
            ]
        ]
    )

    update.callback_query.edit_message_text(text='Выберите способ оплаты 💳\n\n👉🏼Оплата онлай временно не доступна',
                                                 # '\n\n*Примечание:* при оплате онлайн средства поступят на счет водителя только после поездки, если поездка не состоится средства вернуться на ваш счет',
                              reply_markup=markup,
                                            parse_mode=ParseMode.MARKDOWN)

    return END1

def end_p(update:Update, context:CallbackContext):

    update.callback_query.edit_message_text('Заказ сформирован 📦 управлять своими заказами можете по команде - /myorder, экран приветствия - /greet')

    return ConversationHandler.END



# *****************Софт_для_водителей*****************\

def where_d(update: Update, context:CallbackContext):

    data = update.callback_query.data
    context.user_data[PAYMENT2] = data

    markup = InlineKeyboardMarkup(
        inline_keyboard= [
            [
                InlineKeyboardButton('Магнит', callback_data="магнит"),
                InlineKeyboardButton("Город", callback_data="город")
            ],
            [
                InlineKeyboardButton('Приостановить оформление', callback_data='stopall')
            ]
        ]
    )

    update.callback_query.edit_message_text('Куда сможете доставить пассажира? 🔎\n🔻Примечание: до города - (минимум до ул. Жуковского), дальше - на усмотрение водителя',
                                            reply_markup=markup)

    return TIME2

def time_d(update:Update, context:CallbackContext):

    data_where = update.callback_query.data

    if data_where == 'stopall':
        return fallbacks_end(update=update,context=context)

    context.user_data[WHERE2] = data_where

    list_time = ['06:00', '06:30', '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', '10:00', '10:30',
                 '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00',
                 '16:30'
        , '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30']

    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(f'{i}', callback_data=f'{i}') for i in list_time[:5]
            ],
            [
                InlineKeyboardButton(f'{i}', callback_data=f'{i}') for i in list_time[5:10]
            ],
            [
                InlineKeyboardButton(f'{i}', callback_data=f'{i}') for i in list_time[10:15]
            ],
            [
                InlineKeyboardButton(f'{i}', callback_data=f'{i}') for i in list_time[15:20]
            ],
            [
                InlineKeyboardButton(f'{i}', callback_data=f'{i}') for i in list_time[20:25]
            ],
            [
                InlineKeyboardButton(f'{i}', callback_data=f'{i}') for i in list_time[25:30]
            ],
            [
                InlineKeyboardButton('Приостановить оформление', callback_data='stopall')
            ]
        ]
    )

    update.callback_query.edit_message_text('🕗 Выберите время (с расчетом +-15 минут)', reply_markup=markup)


    return FROM2

def from_d(update:Update, context:CallbackContext):

    data = update.callback_query.data

    if data == 'stopall':
        return fallbacks_end(update=update,context=context)

    context.user_data[TIME2] = data

    chat_id = update.effective_message.chat_id
    id = update.effective_message.message_id

    mark_up = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('1: МАГНИТ', callback_data='маг.Магнит'),
                InlineKeyboardButton('2: ул. Стартовая', callback_data="ул.Стартовая")
            ],
            [
                InlineKeyboardButton("3: ул. Майская", callback_data="ул.Майская"),
                InlineKeyboardButton('4: ул. Семейная', callback_data="ул.Семейная")
            ],
            [
                InlineKeyboardButton('5: ул. Янтарная', callback_data="ул.Янтарная"),
                InlineKeyboardButton("6: ул. Снежная", callback_data="ул.Снежная")
            ],
            [
                InlineKeyboardButton("7: ул. Ягодная", callback_data="ул.Ягодная"),
                InlineKeyboardButton("8: ул. Байкальская", callback_data="ул.Байкальская")
            ],
            [
                InlineKeyboardButton("Назад", callback_data="back"),
                InlineKeyboardButton("Дальше", callback_data="next")
            ]
        ],

    )

    context.bot.delete_message(chat_id=chat_id, message_id=id)

    # Если в БД driver_data есть данные пользователя, предлагаем ему сокращенное заполнение
    chat_id = update.effective_message.chat_id
    print(chat_id)
    with sq.connect('driver_data.db') as con:
        cur = con.cursor()
        cur.execute('SELECT user_id from user_data')
        g = cur.fetchall()

        for i in g:
            if i[0] == str(chat_id):
                markup = InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            InlineKeyboardButton('Использовать', callback_data='didit'),
                            InlineKeyboardButton('Ввести новые', callback_data='didnew')
                        ],
                        [
                            InlineKeyboardButton('Приостановить оформление', callback_data='stopall')
                        ]
                    ]
                )
                with sq.connect('driver_data.db') as con:
                    cur = con.cursor()
                    cur.execute(f'SELECT main_data, some from user_data WHERE user_id = "{chat_id}"')
                    g = cur.fetchall()
                    print(g[0][0])
                    pp = g[0][0].split(',')
                    print(pp)
                text = ['*Использовать прежние данные?* 🤔',
                        f'*Машина:* {pp[0]}',
                        f'*Отправление:* с {g[0][1]}',
                        f'*Номер телефона:* {pp[1]}'
                        ]
                context.user_data[BRIEF_MODEL] = pp[0]
                context.user_data[BRIEF_PHONE] = pp[1]
                context.user_data[BRIEF2_FROM2] = g[0][1]
                update.callback_query.message.reply_text(text='\n'.join(text), reply_markup=markup,
                                                         parse_mode=ParseMode.MARKDOWN)
                return BRIEF2

    context.bot.send_photo(chat_id=chat_id, photo=open("sad_1.JPG", "rb"),
                           caption='Выберите улицу отправления:',
                           reply_markup=mark_up)
    return CAR2

def car_d(update:Update, context:CallbackContext):

    data = update.callback_query.data

    if data == 'stopall':
        return fallbacks_end(update=update,context=context)

    if data[:4] == 'next':

        if data == 'next':

            chat_id = update.effective_message.chat_id
            id = update.effective_message.message_id

            mark_up = InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton('9: ул. Веселая', callback_data='ул.Веселая'),
                        InlineKeyboardButton('10: ул. Новосибирская', callback_data="ул.Новосибирская")
                    ],
                    [
                        InlineKeyboardButton("11: ул. Спортивная", callback_data="ул.Спортивная"),
                        InlineKeyboardButton('12: ул. Торговая', callback_data="ул.Торговая")
                    ],
                    [
                        InlineKeyboardButton('13: ул. Учительская', callback_data="ул.Учительская"),
                        InlineKeyboardButton("14: ул. Жемчужная", callback_data="ул.Жемчужная")
                    ],
                    [
                        InlineKeyboardButton("15: ул. Славянская", callback_data="ул.Славянская"),
                        InlineKeyboardButton("16: ул. Красивая", callback_data="ул.Красивая")
                    ],
                    [
                        InlineKeyboardButton("Назад", callback_data="back2"),
                        InlineKeyboardButton("Дальше", callback_data="next2")
                    ]
                ],

            )

            context.bot.delete_message(chat_id=chat_id, message_id=id)

            context.bot.send_photo(chat_id=chat_id, photo=open("sad_2.JPG", "rb"),
                                   caption='Выберите улицу отправления:',
                                   reply_markup=mark_up)

            return CAR2

        elif data == 'next2':
            chat_id = update.effective_message.chat_id
            id = update.effective_message.message_id

            mark_up = InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton('17: ул. Луговая', callback_data='ул.Луговая'),
                        InlineKeyboardButton('18: ул. Транспортная', callback_data="ул.Транспортная")
                    ],
                    [
                        InlineKeyboardButton("19: ул. Калиновая", callback_data="ул.Калиновая"),
                        InlineKeyboardButton('20: ул. Душистая', callback_data="ул.Душистая")
                    ],
                    [
                        InlineKeyboardButton('21: ул. Праздничная', callback_data="ул.Праздничная"),
                        InlineKeyboardButton("22: ул. Некрасова", callback_data="ул.Некрасова")
                    ],
                    [
                        InlineKeyboardButton("23: ул. Геодезическая", callback_data="ул.Геодезическая"),
                        InlineKeyboardButton("24: ул. Дружбы", callback_data="ул.Дружбы")
                    ],
                    [
                        InlineKeyboardButton('25: ул. Русская', callback_data='ул.Русская'),
                        InlineKeyboardButton('26: ул. Линейная', callback_data="ул.Линейная")
                    ],
                    [
                        InlineKeyboardButton("27: ул. Рабочая", callback_data="ул.Рабочая"),
                        InlineKeyboardButton('28: ул. Речная', callback_data="ул.Речная")
                    ],
                    [
                        InlineKeyboardButton('29: ул. Обская', callback_data="ул.Обская"),
                        InlineKeyboardButton("30: ул. Областная", callback_data="ул.Областная")
                    ],
                    [
                        InlineKeyboardButton("23: ул. Геодезическая", callback_data="ул.Геодезическая"),
                        InlineKeyboardButton("24: ул. Дружбы", callback_data="ул.Дружбы")
                    ],
                    [
                        InlineKeyboardButton("Назад", callback_data="back3"),
                        InlineKeyboardButton("Дальше", callback_data="next3")
                    ]
                ],

            )

            context.bot.delete_message(chat_id=chat_id, message_id=id)

            context.bot.send_photo(chat_id=chat_id, photo=open("sad_3.JPG", "rb"),
                                   caption='Выберите улицу отправления:',
                                   reply_markup=mark_up)

            return CAR2

        elif data == 'next3':
            chat_id = update.effective_message.chat_id
            id = update.effective_message.message_id

            mark_up = InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton('1: МАГНИТ', callback_data='маг.Магнит'),
                        InlineKeyboardButton('2: ул. Стартовая', callback_data="ул.Стартовая")
                    ],
                    [
                        InlineKeyboardButton("3: ул. Майская", callback_data="ул.Майская"),
                        InlineKeyboardButton('4: ул. Семейная', callback_data="ул.Семейная")
                    ],
                    [
                        InlineKeyboardButton('5: ул. Янтарная', callback_data="ул.Янтарная"),
                        InlineKeyboardButton("6: ул. Снежная", callback_data="ул.Снежная")
                    ],
                    [
                        InlineKeyboardButton("7: ул. Ягодная", callback_data="ул.Ягодная"),
                        InlineKeyboardButton("8: ул. Байкальская", callback_data="ул.Байкальская")
                    ],
                    [
                        InlineKeyboardButton("Назад", callback_data="back"),
                        InlineKeyboardButton("Дальше", callback_data="next")
                    ]
                ],

            )

            context.bot.delete_message(chat_id=chat_id, message_id=id)

            context.bot.send_photo(chat_id=chat_id, photo=open("sad_1.JPG", "rb"),
                                   caption='Выберите улицу отправления:',
                                   reply_markup=mark_up)

            return CAR2

    if data[:4] == 'back':

        if data == 'back':
            chat_id = update.effective_message.chat_id
            id = update.effective_message.message_id

            mark_up = InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton('17: ул. Луговая', callback_data='ул.Луговая'),
                        InlineKeyboardButton('18: ул. Транспортная', callback_data="ул.Транспортная")
                    ],
                    [
                        InlineKeyboardButton("19: ул. Калиновая", callback_data="ул.Калиновая"),
                        InlineKeyboardButton('20: ул. Душистая', callback_data="ул.Душистая")
                    ],
                    [
                        InlineKeyboardButton('21: ул. Праздничная', callback_data="ул.Праздничная"),
                        InlineKeyboardButton("22: ул. Некрасова", callback_data="ул.Некрасова")
                    ],
                    [
                        InlineKeyboardButton("23: ул. Геодезическая", callback_data="ул.Геодезическая"),
                        InlineKeyboardButton("24: ул. Дружбы", callback_data="ул.Дружбы")
                    ],
                    [
                        InlineKeyboardButton('25: ул. Русская', callback_data='ул.Русская'),
                        InlineKeyboardButton('26: ул. Линейная', callback_data="ул.Линейная")
                    ],
                    [
                        InlineKeyboardButton("27: ул. Рабочая", callback_data="ул.Рабочая"),
                        InlineKeyboardButton('28: ул. Речная', callback_data="ул.Речная")
                    ],
                    [
                        InlineKeyboardButton('29: ул. Обская', callback_data="ул.Обская"),
                        InlineKeyboardButton("30: ул. Областная", callback_data="ул.Областная")
                    ],
                    [
                        InlineKeyboardButton("23: ул. Геодезическая", callback_data="ул.Геодезическая"),
                        InlineKeyboardButton("24: ул. Дружбы", callback_data="ул.Дружбы")
                    ],
                    [
                        InlineKeyboardButton("Назад", callback_data="back3"),
                        InlineKeyboardButton("Дальше", callback_data="next3")
                    ]
                ],

            )

            context.bot.delete_message(chat_id=chat_id, message_id=id)

            context.bot.send_photo(chat_id=chat_id, photo=open("sad_3.JPG", "rb"),
                                   caption='Выберите улицу отправления:',
                                   reply_markup=mark_up)

            return CAR2

        elif data == 'back2':
            chat_id = update.effective_message.chat_id
            id = update.effective_message.message_id

            mark_up = InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton('1: МАГНИТ', callback_data='маг.Магнит'),
                        InlineKeyboardButton('2: ул. Стартовая', callback_data="ул.Стартовая")
                    ],
                    [
                        InlineKeyboardButton("3: ул. Майская", callback_data="ул.Майская"),
                        InlineKeyboardButton('4: ул. Семейная', callback_data="ул.Семейная")
                    ],
                    [
                        InlineKeyboardButton('5: ул. Янтарная', callback_data="ул.Янтарная"),
                        InlineKeyboardButton("6: ул. Снежная", callback_data="ул.Снежная")
                    ],
                    [
                        InlineKeyboardButton("7: ул. Ягодная", callback_data="ул.Ягодная"),
                        InlineKeyboardButton("8: ул. Байкальская", callback_data="ул.Байкальская")
                    ],
                    [
                        InlineKeyboardButton("Назад", callback_data="back"),
                        InlineKeyboardButton("Дальше", callback_data="next")
                    ]
                ],

            )

            context.bot.delete_message(chat_id=chat_id, message_id=id)

            context.bot.send_photo(chat_id=chat_id, photo=open("sad_1.JPG", "rb"),
                                   caption='Выберите улицу отправления:',
                                   reply_markup=mark_up)

            return CAR2

        elif data == 'back3':
            chat_id = update.effective_message.chat_id
            id = update.effective_message.message_id

            mark_up = InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton('9: ул. Веселая', callback_data='ул.Веселая'),
                        InlineKeyboardButton('10: ул. Новосибирская', callback_data="ул.Новосибирская")
                    ],
                    [
                        InlineKeyboardButton("11: ул. Спортивная", callback_data="ул.Спортивная"),
                        InlineKeyboardButton('12: ул. Торговая', callback_data="ул.Торговая")
                    ],
                    [
                        InlineKeyboardButton('13: ул. Учительская', callback_data="ул.Учительская"),
                        InlineKeyboardButton("14: ул. Жемчужная", callback_data="ул.Жемчужная")
                    ],
                    [
                        InlineKeyboardButton("15: ул. Славянская", callback_data="ул.Славянская"),
                        InlineKeyboardButton("16: ул. Красивая", callback_data="ул.Красивая")
                    ],
                    [
                        InlineKeyboardButton("Назад", callback_data="back2"),
                        InlineKeyboardButton("Дальше", callback_data="next2")
                    ]
                ],

            )

            context.bot.delete_message(chat_id=chat_id, message_id=id)

            context.bot.send_photo(chat_id=chat_id, photo=open("sad_2.JPG", "rb"),
                                   caption='Выберите улицу отправления:',
                                   reply_markup=mark_up)

            return CAR2

    context.user_data[FROM2] = data

    update.callback_query.message.reply_text('🚘 Введите марку своей машины, например: "Тойота" или "Toyota"')

    return CAR2_1

def brief_driver(update:Update, context:CallbackContext):
    data = update.callback_query.data

    if data == 'stopall':
        return fallbacks_end(update=update,context=context)

    if data == 'didit':
        chat_id = update.effective_message.chat_id
        name = update.callback_query.from_user.name

        # Запись заявки в БД

        # Иницилизация для открытия правильной БД (сегодня\завтра)
        if context.user_data[DAY] == 'today':
            this_DB = 'driver_database.db'
        elif context.user_data[DAY] == 'tomorrow':
            this_DB = 'driver_database_tomr.db'

        with sq.connect(this_DB) as con:
            cur = con.cursor()

            cur.execute('INSERT INTO user (user_id, name, car, number, time, from_1, where_1, sale) '
                        f'VALUES ('
                        f'"{chat_id}",'
                        f'"{name}",'
                        f'"{context.user_data[BRIEF_MODEL]}",'
                        f'"{context.user_data[BRIEF_PHONE]}", "{context.user_data[TIME2]}",'
                        f'"{context.user_data[BRIEF2_FROM2]}", "{context.user_data[WHERE2]}", "{context.user_data[PAYMENT2]}")')

        update.callback_query.edit_message_text('Ваша заявка принята 📦 Когда найдется пассажир, мы уведомим вас! Экран приветствия - /greet ')


        return ConversationHandler.END

    elif data == 'didnew':
        chat_id = update.effective_message.chat_id
        id = update.effective_message.message_id

        mark_up = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton('1: МАГНИТ', callback_data='маг.Магнит'),
                    InlineKeyboardButton('2: ул. Стартовая', callback_data="ул.Стартовая")
                ],
                [
                    InlineKeyboardButton("3: ул. Майская", callback_data="ул.Майская"),
                    InlineKeyboardButton('4: ул. Семейная', callback_data="ул.Семейная")
                ],
                [
                    InlineKeyboardButton('5: ул. Янтарная', callback_data="ул.Янтарная"),
                    InlineKeyboardButton("6: ул. Снежная", callback_data="ул.Снежная")
                ],
                [
                    InlineKeyboardButton("7: ул. Ягодная", callback_data="ул.Ягодная"),
                    InlineKeyboardButton("8: ул. Байкальская", callback_data="ул.Байкальская")
                ],
                [
                    InlineKeyboardButton("Назад", callback_data="back"),
                    InlineKeyboardButton("Дальше", callback_data="next")
                ]
            ],

        )

        context.bot.delete_message(chat_id=chat_id, message_id=id)

        context.bot.send_photo(chat_id=chat_id, photo=open("sad_1.JPG", "rb"),
                               caption='Выберите улицу отправления:',
                               reply_markup=mark_up)
        with sq.connect('driver_data.db') as con:
            cur = con.cursor()
            cur.execute(f'DELETE FROM user_data WHERE user_id = "{chat_id}"')
        return CAR2

def car_d_1(update:Update, context:CallbackContext):

    data_model_car = update.message.text
    new_type = data_model_car.title()
    context.user_data[MODEL] = new_type

    update.message.reply_text('🎱 Теперь введите номер машины, например: "e245pн"')

    return CAR2_2

def car_d_2(update:Update, context:CallbackContext):

    data_car_number = update.message.text
    new_type = data_car_number.upper()
    context.user_data[NUMBER_CAR] = new_type

    update.message.reply_text('☎️Оставьте номер для оперативной связи:')

    return END2

def end_d(update:Update, context:CallbackContext):

    data_phone_number = update.message.text
    context.user_data[PHONE] = data_phone_number

    markup = InlineKeyboardMarkup(
        inline_keyboard= [
            [
                InlineKeyboardButton('Все верно', callback_data="right"),
                InlineKeyboardButton("Исправить", callback_data="fix")
            ]
        ]
    )

    text = f'''
*Машина:* {context.user_data[MODEL]} {context.user_data[NUMBER_CAR]}
*Ваш номер телефона:* {context.user_data[PHONE]}'''


    update.message.reply_text(f'Проверьте ваши заполненные данные:{text}',
                              reply_markup=markup,
                              parse_mode=ParseMode.MARKDOWN)
    return END2_2

def end_d_2(update:Update, context:CallbackContext):

    data = update.callback_query.data

    if data == 'fix':

        update.callback_query.message.reply_text('🚘 Введите марку своей машины, например: "Тойота" или "Toyota"')

        return CAR2_1

    chat_id = update.effective_message.chat_id
    # print(chat_id)
    name = update.callback_query.from_user.name
    # print(name)


    # Запись заявки в БД

    # Иницилизация для открытия правильной БД (сегодня\завтра)
    if context.user_data[DAY] == 'today':
        this_DB = 'driver_database.db'
    elif context.user_data[DAY] == 'tomorrow':
        this_DB = 'driver_database_tomr.db'

    with sq.connect(this_DB) as con:
        cur = con.cursor()

        cur.execute('INSERT INTO user (user_id, name, car, number, time, from_1, where_1, sale) '
                    f'VALUES ('
                    f'"{chat_id}",'
                    f'"{name}",'
                    f'"{context.user_data[MODEL]} {context.user_data[NUMBER_CAR]}",'
                    f'"{context.user_data[PHONE]}", "{context.user_data[TIME2]}",'
                    f'"{context.user_data[FROM2]}", "{context.user_data[WHERE2]}", "{context.user_data[PAYMENT2]}")')

    update.callback_query.edit_message_text('Ваша заявка принята 📦 Когда найдется пассажир, мы уведомим вас! Экран приветствия - /greet ')

    # Сохранение данных водителя, чтобы в будущем экономить ему время
    with sq.connect('driver_data.db') as con:
        cur = con.cursor()
        cur.execute('SELECT user_id from user_data')
        g = cur.fetchall()
        print(g)

    list_id  = []
    for i in g:
        list_id.append(i[0])

    if str(chat_id) not in list_id:
        with sq.connect('driver_data.db') as con:
            cur = con.cursor()

            cur.execute(
                'INSERT INTO user_data (main_data, user_id, who_data, some) VALUES ('
                f'"{context.user_data[MODEL]} {context.user_data[NUMBER_CAR]},{context.user_data[PHONE]}","{chat_id}", "driver",'
                f'"{context.user_data[FROM2]}")')


    return ConversationHandler.END


def fallbacks_end(update:Update, context:CallbackContext):

    update.callback_query.edit_message_text('Оформление заявки приостановлено!')
    return ConversationHandler.END


def main():

    updater = Updater(
        token='1940112781:AAFapfgmszNYUYFGLOITgshBLgAF5hSG1SA'
    )

    conv_han_drive = ConversationHandler(
        entry_points= [
            CommandHandler('drive', start_conv)
        ],
        states= {
            DAY: [
                CallbackQueryHandler(tomorrow)
            ],
            WHERE1: [
                CallbackQueryHandler(where_p)
            ],
            TIME1: [
                CallbackQueryHandler(time_p)
            ],
            TIME1_1: [
                CallbackQueryHandler(time_p1)
            ],
            FROM1: [
                CallbackQueryHandler(from_p)
            ],
            FROM1_2:[
                CallbackQueryHandler
            ],
            OFFER1: [
                CallbackQueryHandler(offer_p)
            ],
            SPARE1: [
                CallbackQueryHandler(spare_1)
            ],
            PAYMENT1: [
                CallbackQueryHandler(pay_p)
            ],
            END1: [
                CallbackQueryHandler(end_p)
            ],

            WHERE2: [
                CallbackQueryHandler(where_d)
            ],
            TIME2: [
                CallbackQueryHandler(time_d)
            ],
            FROM2: [
                CallbackQueryHandler(from_d)
            ],
            BRIEF2: [
                CallbackQueryHandler(brief_driver)
            ],
            CAR2: [
                CallbackQueryHandler(car_d)
            ],
            CAR2_1: [
                MessageHandler(Filters.all, car_d_1)
            ],
            CAR2_2: [
                MessageHandler(Filters.all, car_d_2)
            ],
            END2: [
                MessageHandler(Filters.all, end_d)
            ],
            END2_2: [
                CallbackQueryHandler(end_d_2)
            ]

        },
        fallbacks= [
            CommandHandler('cancel', fallbacks_end)
        ]
    )


    updater.dispatcher.add_handler(conv_han_drive)
    updater.dispatcher.add_handler(CallbackQueryHandler(callback_for_order))
    updater.dispatcher.add_handler(CommandHandler('donations', donat))
    updater.dispatcher.add_handler(CommandHandler('myorder', my_order_main))
    updater.dispatcher.add_handler(CommandHandler('help', helping))

    updater.dispatcher.add_handler(MessageHandler(Filters.all, echo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()