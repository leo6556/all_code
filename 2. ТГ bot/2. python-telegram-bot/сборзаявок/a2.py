from telegram import Bot
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CallbackQueryHandler
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import CommandHandler
from telegram.ext import ConversationHandler
from telegram.ext import Filters
from telegram.utils.request import Request

from validator import GENDER_MAP
from validator import gender_hru
from validator import valid_age
from validator import valid_gender


NAME, GENDER, AGE = range(3)

CALLBACK_BEGIN = 'x1'


def start_buttons_handler(update: Update, context: CallbackContext):
    """ Не относится к сценарию диалога, но создаёт начальные inline-кнопки
    """
    inline_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Начать', callback_data=CALLBACK_BEGIN),
            ],
        ],
    )
    update.message.reply_text(
        'Нажми на кнопку:',
        reply_markup=inline_buttons,
    )

def start_handler(update: Update, context: CallbackContext):
    """ Начало взаимодействия по клику на inline-кнопку
    """
    init = update.callback_query.data
    chat_id = update.callback_query.message.chat.id

    if init != CALLBACK_BEGIN:


        update.callback_query.bot.send_message(
            chat_id=chat_id,
            text='Что-то пошло не так, обратитесь к администратору бота',
        )
        return ConversationHandler.END

    update.callback_query.answer()

    # Спросить имя
    update.callback_query.bot.send_message(
        chat_id=chat_id,
        text='Введи своё имя чтобы продолжить:',
    )
    return NAME


def name_handler(update: Update, context: CallbackContext):
    # Получить имя
    context.user_data[NAME] = update.message.text

    # Спросить пол
    inline_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=value, callback_data=key) for key, value in GENDER_MAP.items()],
        ],
    )
    update.message.reply_text(
        text='Выберите свой пол чтобы продолжить',
        reply_markup=inline_buttons,
    )
    return GENDER


def age_handler(update: Update, context: CallbackContext):
    # Получить пол
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


def finish_handler(update: Update, context: CallbackContext):
    # Получить возраст
    age = valid_age(text=update.message.text)
    if age is None:
        update.message.reply_text('Пожалуйста, введите корректный возраст!')
        return AGE

    context.user_data[AGE] = age


    # Завершить диалог
    update.message.reply_text(f'''
Все данные успешно сохранены! 
Вы: {context.user_data[NAME]}, пол: {gender_hru(context.user_data[GENDER])}, возраст: {context.user_data[AGE]} 
''')
    return ConversationHandler.END


def cancel_handler(update: Update, context: CallbackContext):
    """ Отменить весь процесс диалога. Данные будут утеряны
    """
    update.message.reply_text('Отмена. Для начала с нуля нажмите /start')
    return ConversationHandler.END


def echo_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Нажмите /start для заполнения анкеты!',
    )


def main():

    updater = Updater(
        token='1927368703:AAFL5cNCFbkmxKYoGCQZXybrB_I49SdQbOA'
    )


    # Навесить обработчики команд
    conv_handler = ConversationHandler(
        entry_points=[
            CallbackQueryHandler(start_handler, pass_user_data=True),
        ],
        states={
            NAME: [
                MessageHandler(Filters.all, name_handler, pass_user_data=True),
            ],
            GENDER: [
                CallbackQueryHandler(age_handler, pass_user_data=True),
            ],
            AGE: [
                MessageHandler(Filters.all, finish_handler, pass_user_data=True),
            ],
        },
        fallbacks=[
            CommandHandler('cancel', cancel_handler),
        ],
    )
    updater.dispatcher.add_handler(conv_handler)
    updater.dispatcher.add_handler(CommandHandler('start', start_buttons_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.all, echo_handler))

    # Начать бесконечную обработку входящих сообщений
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
