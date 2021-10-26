from telegram import Bot
from telegram import Update
from  telegram import InlineKeyboardMarkup
from telegram import InlineKeyboardButton
from telegram.ext import CallbackQueryHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import CommandHandler
from telegram.ext import CallbackContext
from telegram.ext import Updater


TToken = '1996839593:AAEYgxFoy7DOaTTOcXojsvDvmx_hPHlSJh0'

def markup():
    keyboard = [
        [
            InlineKeyboardButton('кроссовки 👟', callback_data='snik'),
            InlineKeyboardButton('смоккинги 👨🏼‍', callback_data='sm'),

        ],
        [
            InlineKeyboardButton('другое (аксесуары) 🎩', callback_data='else')
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

def markup2():
    keyboard = [
        [
            InlineKeyboardButton('галстуки', callback_data='tie'),
            InlineKeyboardButton('бабочки', callback_data='fly'),
            InlineKeyboardButton('запонки', callback_data='po'),
        ],
        [
            InlineKeyboardButton('оружие', callback_data='gun'),
            InlineKeyboardButton('назад', callback_data='back'),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)



def callback(update: Update, context: CallbackContext):

    query = update.callback_query
    data = query.data
    current_text = update.effective_message.text

    if data == 'snik':
        query.edit_message_text('В наличии 412 пар кроссовок nike\nИ 284 пары adidas',
                                reply_markup=markup())
    elif data == 'sm':
        query.edit_message_text('В наличии 40 костюмов наилучшего качества в 6 классических стилях',
                                reply_markup=markup())
    elif data == 'else':
        query.edit_message_text(current_text,
                                reply_markup=markup2())
    elif data == 'back':
        query.edit_message_text('Добро пожаловать в наш магазин, перед тем как попасть в страну чудес',
                                reply_markup=markup())
    elif data == 'gun':
        query.edit_message_text(
            'Glock 6.4mm,\nDisert Eagl 12mm,\nBMG 50mm,\nгранаты 4500Дж.,',
            reply_markup=markup2()
        )

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Добро пожаловать в учебный бот)))')

def shop(update: Update, context: CallbackContext):
    update.message.reply_text('Добро пожаловать в наш магазин, перед тем как попасть в страну чудес',
                              reply_markup=markup())

def echo(update: Update, context: CallbackContext):
    text = update.message.text
    update.message.reply_text(
        'Если хотите зайти к нам в магазин отправьте команду"/shop"')


def main():
    bot = Bot(
        token=TToken,
    )

    updater = Updater(
        bot=bot,
    )

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('shop', shop))
    updater.dispatcher.add_handler(CallbackQueryHandler(callback=callback, pass_chat_data=True))
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()