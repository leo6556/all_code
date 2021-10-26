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

def echo(update: Update, context: CallbackContext):
    update.message.reply_text('Чтобы заполнить анкету введите команду /start')

def start(update: Update, context: CallbackContext):


def main():
    updater = Updater(
        token='1927368703:AAFL5cNCFbkmxKYoGCQZXybrB_I49SdQbOA'
    )

    updater.dispatcher.add_hundler(MessageHandler(Filters.all, echo))




    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()