from telegram import Bot
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters

from Inlinekeyboard.config import TToken

FEEDBACK_USER_ID = '1790158717'


def do_echo(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id







# закомментрованнлое внизу не работает!



    # if chat_id == FEEDBACK_USER_ID:
    #     # Смотрим на реплаи
    #     error_message = None
    #     reply = update.message.reply_to_message
    # #     if reply:
    # #         forward_from = reply.forward_from
    # #         if forward_from:
    # #             text = 'Сообщение от автора канала:\n\n' + update.message.text
    # #             context.bot.send_message(
    # #                 chat_id=forward_from.id,
    # #                 text=text,
    # #             )
    # #             update.message.reply_text(
    # #                 text='Сообщение было отправлено',
    # #             )
    # #         else:
    # #             error_message = 'Нельзя ответить самому себе'
    # #     else:
    # #         error_message = 'Сделайте reply чтобы ответить автору сообщения'
    # #
    # #     # Отправить сообщение об ошибке если оно есть
    # #     if error_message is not None:
    # #         update.message.reply_text(
    # #             text=error_message,
    #         )
    # else:
    #     # Пересылать всё как есть
    #     update.message.forward(
    #         chat_id=FEEDBACK_USER_ID,
    #     )
    #     update.message.reply_text(
    #         text='Сообщение было отправлено',
    #     )
    #
    #


def main():
    bot = Bot(
        token=TToken,
    )
    updater = Updater(
        bot=bot,
    )

    mes_handler = MessageHandler(filters=Filters.text, callback=do_echo)
    updater.dispatcher.add_handler(mes_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()