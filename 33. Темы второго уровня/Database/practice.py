from telegram import Bot
from telegram import Update
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import CallbackQuery
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.utils.request import Request
from telegram.ext import CallbackQueryHandler

from a1 import init_db
from a1 import add_m
from a1 import count_m
from a1 import list_m

def get_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Кол-во сообщений', callback_data='count')
            ],
            [
                InlineKeyboardButton(text='Мои сообщения', callback_data='list')
            ],
        ]
    )

def echo(update: Update, context: CallbackContext):
    user = update.effective_user
    if user:
       name =  user.first_name
    else:
        name = 'anonim'

    text = update.message.text
    replytext = f'Привет {name}\n\n{text}'
    update.message.reply_text(text=replytext,
                              reply_markup=get_keyboard())

    if text:
        add_m(
            user_id=user.id,
            text=text
        )

def callback_han(update: Update, context: CallbackContext):
    user = update.effective_user
    callback_data = update.callback_query.data

    if callback_data == 'count':
        count = count_m(user_id=user.id)
        text = f'У вас {count} сообщений'
    elif callback_data == 'list':
        mess = list_m(user_id=user.id, limit=5)
        text = '\n\n'.join([f'#{mess_id} - {mess_text}' for mess_id, mess_text in mess])
    else:
        text = 'ошибочка'


    update.effective_message.reply_text(text=text)


def main():
    req = Request(
        connect_timeout=10,
        read_timeout=10,
    )
    bot = Bot(
        token='1927368703:AAFL5cNCFbkmxKYoGCQZXybrB_I49SdQbOA',
        request=req,
    )
    updater = Updater(
        bot=bot,
    )

    init_db()

    updater.dispatcher.add_handler(MessageHandler(Filters.all, echo))
    updater.dispatcher.add_handler(CallbackQueryHandler(callback_han, pass_chat_data=True))


    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()



