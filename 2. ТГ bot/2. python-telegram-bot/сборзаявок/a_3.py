from telegram import Update
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import MessageHandler
from telegram.ext import ConversationHandler
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import CallbackQueryHandler

from validators import valid_gender
from validators import valid_age
from validators import GENDER_MAP
from validators import gender_hru

NAME, AGE, GENDER = range(3)

def echo(update: Update, context: CallbackContext):
    update.message.reply_text('Чтобы зарегестрироваться введите команду "/start"')

def start_but(update: Update, context: CallbackContext):

    markup = InlineKeyboardMarkup(
        inline_keyboard= [
            [
                InlineKeyboardButton('Начать', callback_data='1'),
            ],
        ],
    )
    update.message.reply_text(
        'Нажмите начать!',
        reply_markup=markup,
    )

def start_conv(update: Update, context: CallbackContext):
    chat_id = update.callback_query.message.chat_id
    update.callback_query.bot.send_message(
        chat_id=chat_id,
        text='Введите свое имя:'
    )
    return NAME

def name_han(update: Update, context: CallbackContext):
    unit = update.message.text

    if unit.isalpha()==False:
        update.message.reply_text(
            'Введите имя БУКВАМИ!!!!!')
        return AGE

    context.user_data[NAME] = unit

    markup = InlineKeyboardMarkup(
        inline_keyboard= [
            [
                InlineKeyboardButton(text=value,callback_data=key) for key, value in GENDER_MAP.items()
            ],
        ],
    )

    update.message.reply_text('Укажите свой пол:',
                              reply_markup=markup)
    return GENDER

def gender_han(update: Update, context: CallbackContext):

    gender = update.callback_query.data
    gender = int(gender)
    print(gender)


    context.user_data[GENDER] = gender

    chat_id = update.callback_query.message.chat_id
    update.callback_query.bot.send_message(
        chat_id=chat_id,
        text='И какой у вас возраст?'
    )
    return AGE

def age_han(update: Update, context: CallbackContext):

    age = valid_age(update.message.text)
    if age is None:
        update.message.reply_text('Вводите корректные числа')
        return AGE
    context.user_data[AGE] = update.message.text

    update.message.reply_text(
        f'''
Поздравляю, вы зарегестрировались
Вы - {context.user_data[NAME]}, пол: {gender_hru(context.user_data[GENDER])}, возраст:{context.user_data[AGE]}'''
    )
    return ConversationHandler.END



def cancel_han(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Если хотите начать сначала нажмите на /start'
    )
    return ConversationHandler.END



def main():
    updater = Updater(
        token='1927368703:AAFL5cNCFbkmxKYoGCQZXybrB_I49SdQbOA'
    )

    conv_han = ConversationHandler(
        entry_points= [
            CallbackQueryHandler(start_conv, pass_user_data=True)
        ],
        states= {
            NAME: [
                MessageHandler(Filters.all, name_han)
            ],
            GENDER: [
                CallbackQueryHandler(gender_han, pass_user_data=True)
            ],
            AGE: [
                MessageHandler(Filters.all, age_han)
            ],
        },
        fallbacks=[
            CommandHandler('cancel', cancel_han)
        ]
    )
    updater.dispatcher.add_handler(conv_han)

    updater.dispatcher.add_handler(CommandHandler('start', start_but))
    updater.dispatcher.add_handler(MessageHandler(Filters.all, echo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()