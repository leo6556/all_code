import datetime

from telegram import Bot
from telegram import Update
from telegram import ParseMode
from  telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler
from telegram.ext import Updater
from  telegram.ext import  CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters


from Inlinekeyboard.config import TToken

def base_mark_up():

    keyboard = [
        [
            InlineKeyboardButton('новое сообщение', callback_data='new'),
            InlineKeyboardButton('отредактировтаь', callback_data='edit'),
        ],
        [
            InlineKeyboardButton('еще', callback_data='else')
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

def base_2():

        keyboard = [
            [
              InlineKeyboardButton('Время', callback_data='time')
            ],
            [
                InlineKeyboardButton('rub', callback_data='y'),
                InlineKeyboardButton('dol', callback_data='e'),
                InlineKeyboardButton('btc', callback_data='l'),
            ],
            [
                InlineKeyboardButton('назад', callback_data='back')
            ]
        ]
        return InlineKeyboardMarkup(keyboard)


def call_han(update: Update, context: CallbackContext):

    query = update.callback_query
    data = query.data
    now = datetime.datetime.now()

    chat_id = update.effective_message.chat_id
    current_text = update.effective_message.text

    if data == 'new':
        query.edit_message_text(
            text=current_text,
            parse_mode=ParseMode.MARKDOWN,
        )
    elif data == 'edit':
     query.edit_message_text('Учпешно отредактировано в {}'.format(now),
                             reply_markup=base_mark_up())
    elif data == 'else':
        query.edit_message_text(
            current_text,
            reply_markup=base_2(),
        )
    elif data == 'back':
        query.edit_message_text(
            current_text,
            reply_markup=base_mark_up()
        )
    elif data == 'time':
        text = 'точное время: {}'.format(now)
        query.edit_message_text(
            text=text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=base_2()
        )


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='отправь мне что-нибудь...'
    )

def help(update: Update, context: CallbackContext):
    text = 'это учебный бот,\nCписок командд можешь поспотреть в меню...'
    update.message.reply_text(text)



def echo(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    text = 'Ваш ID = {}\n\n {}'.format(chat_id, update.message.text)
    update.message.reply_text(text=text,
                              reply_markup=base_mark_up())

def main():
    bot = Bot(
        token=TToken,
    )
    updater = Updater(
        bot=bot,
    )

    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CallbackQueryHandler(callback=call_han, pass_chat_data=True))


    start_handler = CommandHandler('start', start)
    mes_handler = MessageHandler(filters=Filters.text, callback=echo)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(mes_handler)


    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()



