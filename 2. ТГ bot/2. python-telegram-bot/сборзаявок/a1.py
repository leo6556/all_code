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
    update.message.reply_text('Чтобы зарегистрироваться введите \старт')

def start(update: Update, context: CallbackContext):
    """ Не относится к сценарию диалога, но создаёт начальные inline-кнопки
    """
    inline_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Начать', callback_data='4'),
            ],
        ],
    )
    update.message.reply_text(
        'Нажми на кнопку:',
        reply_markup=inline_buttons,
    )


def start_han(update: Update, context: CallbackContext):
    """ Начало взаимодействия по клику на inline-кнопку
    """
    init = update.callback_query.data
    chat_id = update.callback_query.message.chat.id

    update.callback_query.answer()

    # Спросить имя
    update.callback_query.bot.send_message(
        chat_id=chat_id,
        text='Введи своё имя чтобы продолжить:',
    )
    return NAME

def name_han(update: Update, context: CallbackContext):
    context.user_data[NAME] = update.message.text

    genders = [f'{key} - {value}' for key, value in GENDER_MAP.items()]
    genders = '\n'.join(genders)
    update.message.reply_text(f'''
    Выберите свой пол, чтобы продолжить:
    {genders}
''')
    return GENDER

def age_han(update: Update, context: CallbackContext):
    gender = valid_gender(text=update.message.text)
    if gender is None:
        update.message.reply_text('Пожалуйста укажите корректный пол!')
        return GENDER

    context.user_data[GENDER] = gender
    update.message.reply_text('''
    Введите свой возраст:
    ''')
    return AGE

def finish_han(update: Update, context: CallbackContext):
    age = valid_age(text=update.message.text)

    if age is None:
        update.message.reply_text('Пожалуйста, введите корректный возраст!')
        return AGE

    context.user_data[AGE] = age
    update.message.reply_text(f'''
Все данные сохранены!
Вы: {context.user_data[NAME]}, пол: {gender_hru(context.user_data[GENDER])}, возраст: {context.user_data[AGE]}''')
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
                MessageHandler(Filters.all, age_han, pass_user_data=True),
            ],
            AGE: [
                MessageHandler(Filters.all, finish_han, pass_user_data=True),
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