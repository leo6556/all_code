from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import CommandHandler
from telegram.ext import ConversationHandler
from telegram.ext import Filters
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler

from validator import GENDER_MAP
from validator import gender_hru
from validator import valid_age
from validator import valid_gender

NAME, GENDER, AGE = range(3)

def echo(update: Update, context: CallbackContext):
    update.message.reply_text('Чтобы заполнить анкету введите команду /start')

def start(update: Update, context: CallbackContext):

    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('начать', callback_data='1')
            ],

        ],
    )
    update.message.reply_text(
        'Нажми на кнопку',
        reply_markup=markup,
    )

def start_han(update: Update, context: CallbackContext):
    init = update.callback_query.data

    chat_id = update.callback_query.message.chat.id
    update.callback_query.answer()

    update.callback_query.bot.send_message(
         chat_id=chat_id,
         text='Введите свое имя:'
     )
    return NAME

def name_han(update: Update, context: CallbackContext):
    context.user_data[NAME] = update.message.text

    markup2 = InlineKeyboardMarkup(
        inline_keyboard= [
            [InlineKeyboardButton(text=value, callback_data=key) for key, value in GENDER_MAP.items()]
        ]
    )
    update.message.reply_text('Выберите свой гендер',
                              reply_markup=markup2)
    return GENDER

def age_han(update: Update, context: CallbackContext):
    gender = update.callback_query.data
    gender = int(gender)
    if gender not in GENDER_MAP:
        # Этой ситуации не должно быть для пользователя! То есть какое-то значение
        # в кнопках есть, но оно не включено в список гендеров
        update.effective_message.reply_text('Что-то пошло не так, обратитесь к администратору бота')
        return GENDER

    context.user_data[GENDER] = gender

    # Спросить возраст
    update.effective_message.reply_text(
        text='Введите свой возраст:',
    )
    return AGE

def gender_han(update: Update, context: CallbackContext):
    age = valid_age(text=update.message.text)



    context.user_data[AGE] = age

    update.message.reply_text(f'''
    Все данные успешно сохранены!
    Вы - {context.user_data[NAME]}, пол: {context.user_data[GENDER]}, возраст: {context.user_data[AGE]}''')

    return ConversationHandler.END




def cancel_han(update: Update, context: CallbackContext):
    """ Отменить весь процесс диалога. Данные будут утеряны
    """
    update.message.reply_text('Отмена. Для начала с нуля нажмите /start')
    return ConversationHandler.END

def main():
    updater = Updater(
        token='1927368703:AAFL5cNCFbkmxKYoGCQZXybrB_I49SdQbOA'
    )

    conv_handler = ConversationHandler(
        entry_points=[
            CallbackQueryHandler(start_han, pass_user_data=True),
        ],
        states={
            NAME: [
                MessageHandler(Filters.all, name_han, pass_user_data=True),
            ],
            GENDER: [
                CallbackQueryHandler(age_han, pass_user_data=True),
            ],
            AGE: [
                MessageHandler(Filters.all, gender_han, pass_user_data=True),
            ],
        },
        fallbacks=[
            CommandHandler('cancel', cancel_han),
        ],
    )
    updater.dispatcher.add_handler(conv_handler)

    updater.dispatcher.add_handler(CommandHandler('start', start))

    updater.dispatcher.add_handler(MessageHandler(Filters.all, echo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()