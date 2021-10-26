import os

import telebot
import time
import config


#AwACAgIAAxkDAAMhYSBXiRnBs5b4-ESfnRgAARe06YzBAAImDwAC4_QJScCzYfscuBbUIAQ
#AwACAgIAAxkDAAMjYSBXir4GsZXZhdhfNZULBHEqPikAAicPAALj9AlJJDoorIAdDbcgBA
#AwACAgIAAxkDAAMlYSBXjM_Nonwhvpxtwi65Rlx84aYAAigPAALj9AlJ1W3uLtMutLQgBA


bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['test'])
def find_ids(message):
    for file in os.listdir('music/'):
        if file.split('.')[-1] == 'ogg':
            f = open('music/' + file, 'rb')
            msg = bot.send_voice(message.chat.id, f, None)
            bot.send_message(message.chat.id, msg.voice.file_id, reply_to_message_id=msg.message_id)
        time.sleep(1)

if __name__ == '__main__':
    bot.infinity_polling()
