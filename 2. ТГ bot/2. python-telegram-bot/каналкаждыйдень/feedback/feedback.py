from telegram import Update
from telegram.ext import MessageHandler
from telegram.ext import CommandHandler
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import CallbackContext

FEEDBACK_USER_ID  = '1790158717'

def do_start(update: Update, context: CallbackContext):
    update.message.reply_text('Привет, любое твое предложение переотправлю "Поиск репетитора"')


def mes_for(update: Update, context: CallbackContext):
    # chat_id = update.message.chat_id
    # print(chat_id)
    update.effective_message.bot.forward_message(
        chat_id='1790158717',
        from_chat_id=chat_id,
        message_id=update.effective_message.message_id

    )
    chat_id = update.message.chat_id
    #
    # if chat_id == FEEDBACK_USER_ID:
    #     error_message = None
    #     reply = update.message.reply_to_message
    #     if reply:
    #         forward_from = reply.forward_from
    #         if forward_from:
    #             text = 'Сообщение от автора канала:\n\n' + update.message.text
    #             context.bot.send_message(chat_id=forward_from.id,
    #                                      text=text)
    #             update.message.reply_text('Сообщение было отправлено')
    #         else:
    #             error_message = 'Нельзя ответить самому себе'
    #     else:
    #         error_message = 'Можете сделать reply, чтобы ответить пользователю'
    #
    #     if error_message is not None:
    #         update.message.reply_text(text=error_message)
    #
    #     return
    #
    #
    #
    # else:
    update.message.forward(
        chat_id=FEEDBACK_USER_ID,
        )
    update.message.reply_text(
        text='Сообщение было отправлено'
        )

def main():

    updater = Updater(
        token='1996839593:AAEYgxFoy7DOaTTOcXojsvDvmx_hPHlSJh0'
    )

    updater.dispatcher.add_handler(CommandHandler('start', do_start))
    updater.dispatcher.add_handler(MessageHandler(Filters.all, mes_for))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()