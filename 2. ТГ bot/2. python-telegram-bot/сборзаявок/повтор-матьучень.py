from telegram import Update
from telegram import ParseMode
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup

from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import MessageHandler
from telegram.ext import ConversationHandler
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import CallbackQueryHandler
import time

from pprint import pprint
import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials

CRED_FILE = 'creds.json'
spreadsheets_id = '1DjGp4T1w_ChKieeLKbrNJVFkP6MTwlBbSHiT5u6zeik'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CRED_FILE,
    [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

DATE, POINT, GENDER, TIME = 0,1,2,4

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(text='привет, если хочешь записаться в салон красоты, вбей команду "/start"')

def start(update: Update, context: CallbackContext):

    text = [
        'Доброго времени суток)',
        "Добро пожаловать в салон красоты 'Beauty Girls'! 😁 ",
        '',
        'Буквально за минуту ты можешь записаться на нужную тебе процедуру, а также посмотреть цены 🤓',
        "",
        'Выбери нужную операцию:',
        '/sigh_up -- записаться на прием',
        '/price -- цены на наши услуги',
        "/my_orders -- мои заказы",
        "/help -- помощь"

    ]

    update.message.reply_text(text='\n'.join(text),
                              parse_mode=ParseMode.MARKDOWN)

def markup_base():
    keyboard = [
        [
            InlineKeyboardButton('Стрижка', callback_data='haircut'),
            InlineKeyboardButton('Окрашивание', callback_data='hair')
        ],
        [
            InlineKeyboardButton('Лицо', callback_data='face'),
            InlineKeyboardButton('Маникюр', callback_data='manicure')
        ],
        [
            InlineKeyboardButton('Педикюр', callback_data='pedicure')
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

def markup_base2():
    keyboard = [
        [
            InlineKeyboardButton('Стрижка', callback_data='haircut2'),
            InlineKeyboardButton('Окрашивание', callback_data='hair2')
        ],
        [
            InlineKeyboardButton('Лицо', callback_data='face2'),
            InlineKeyboardButton('Маникюр', callback_data='manicure2')
        ],
        [
            InlineKeyboardButton('Педикюр', callback_data='pedicure2')
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

def markupDate():
    b = time.asctime()
    c = int(b[7:10])
    k = b[4:7]


    # f = values['values'][0].index(str(c))
    # print(f)

    month = {'Sep':'сен', 'Oct':'окт', 'Nov':'нояб', 'Dec':'дек', 'Jan':'янв', 'Feb':'фев', 'Mar':'мар','Apr':'апр', 'May':'мая', 'Jun':'июн',
             'Jul':'июл','Aug':'авг'}
    month2 = {'Sep': 'окт', 'Oct': 'нояб', 'Nov': 'дек', 'Dec': 'янв', 'Jan': 'фев', 'Feb': 'мар', 'Mar': 'апр',
             'Apr': 'мая', 'May': 'июн', 'Jun': 'июл',
             'Jul': 'авг', 'Aug': 'сен'}
    values = [5,6,7,5,4,3,2,2,4,5,6,7,8,9,0,8,7,6,4,5,56,76,7,8,8,8,7,7,6,5,5,45,4,9]

    if c <= 23:
        keyboard = [
            [
                InlineKeyboardButton(f"{b} {month[k]}", callback_data=f'{b}') for b in values[c:c + 4]
            ],
            [
                InlineKeyboardButton(f"{b} {month[k]}", callback_data=f'{b}') for b in values[c + 4:c + 8]
            ],

        ]
    elif c >= 27:

        keyboard = [
            [
                InlineKeyboardButton(f"{b} {month[k]}", callback_data=f'{b}') for b in values['values'][0][c:]

            ],
            [
                InlineKeyboardButton(f"{p} {month2[k]}", callback_data=f'{b}') for p in values['values'][0][:4]
            ],

        ]
    else:

        keyboard = [
            [
                InlineKeyboardButton(f"{b} {month2[k]}", callback_data=f'{b}') for b in values['values'][0][c:c+4]

            ],
            [
                InlineKeyboardButton(f"{p} окт", callback_data=f'{p}') for p in values['values'][0][c+6:]
            ],
        ]


    return InlineKeyboardMarkup(keyboard)

def markup_back():
    keyboard = [
        [
            InlineKeyboardButton('Назад', callback_data='back')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


def price_list(update: Update, context: CallbackContext):
    update.message.reply_text('Что тебя интересует? 😊',
                              reply_markup=markup_base())

def callback(update:Update, context:CallbackContext):
    query = update.callback_query
    data = query.data
    current_text = update.effective_message.text

    if data == 'haircut':

        query.edit_message_text('''
Стрижка -- 2400,
Стрижка челки -- 800,
Подровнять кончики -- 1200,

Модельная укладка -- 1800''',
                                reply_markup=markup_back())
    elif data == 'back':
        query.edit_message_text('Что тебя интересует? 😊',
                              reply_markup=markup_base())
    elif data == 'hair':
        query.edit_message_text('''
        Окрашивание в один тон -- 4500,
*Окраши*вание корней -- 3200,
Тонирование -- 2000''',
                                reply_markup=markup_back(),
                                parse_mode=ParseMode.MARKDOWN)
    elif data == 'face':
        query.edit_message_text('''
        Классический макияж -- 2500,
Механическая чистка лица - 3000,
Пилинг -- 1800''',
                                reply_markup=markup_back())
    elif data == 'manicure':
        query.edit_message_text('''
        Маникюр классичкеский - 850,
Маникюр аппаратный -- 1250,
покрытие - 900,
снятие - 150''',
                                reply_markup=markup_back())
    elif data == 'pedicure':
        query.edit_message_text('''
        Педикюр классический -- 1600,
Педикюр аппаратный -- 1800,
Обработка вросшего ногтя -- 1300''',
                                reply_markup=markup_back())

    if data[-3:] == 'end':
        b = time.asctime()
        c = int(b[7:10])

        query.edit_message_text('Выберте удобную вам дату:',
                                  reply_markup=markupDate())



def start_conv(update:Update, context:CallbackContext):

    update.message.reply_text(
        text='Выберите нужную услугу',
        reply_markup=markup_base2()
    )
    return POINT

def date_han(update:Update, context:CallbackContext):

    point = update.callback_query.data
    print(point)

    context.user_data[POINT] = point

    chat_id = update.callback_query.message.chat_id

    update.callback_query.edit_message_text(
        text='Выберите удобныйц для вас день:',
        reply_markup=markupDate()
    )
    return TIME


def time_han(update:Update, context:CallbackContext):
    callback_data = update.callback_query.data
    print(callback_data)
    context.user_data[DATE] = callback_data


def cancel_han(update:Update, context:CallbackContext):
    pass

def main():
    updater = Updater(
        token='1927368703:AAFL5cNCFbkmxKYoGCQZXybrB_I49SdQbOA')

#1932460705:AAGmuy7377SjrfKuner8vFt4PLbktHktzWA

    conv_han = ConversationHandler(
        entry_points= [
            CommandHandler('sighup', start_conv)
        ],
        states= {
            POINT: [
                CallbackQueryHandler(date_han)
            ],
            TIME: [
                CallbackQueryHandler(time_han)
            ]
        },
        fallbacks= [
            CommandHandler('cancel', cancel_han)
        ]

    )

    updater.dispatcher.add_handler(conv_han)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('price', price_list))

    updater.dispatcher.add_handler(MessageHandler(Filters.all, echo))
    updater.dispatcher.add_handler(CallbackQueryHandler(callback=callback))

    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    main()