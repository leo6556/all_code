
import telebot
from telebot import types

# 1996839593:AAEYgxFoy7DOaTTOcXojsvDvmx_hPHlSJh0
# t.me/ts_lion_bot

bot = telebot.TeleBot('1996839593:AAEYgxFoy7DOaTTOcXojsvDvmx_hPHlSJh0')

name = ''
surname = ''
age = 0

@bot.message_handler(commands = ['start', 'help'])
def bot_reply(message):
    bot.reply_to(message, 'привет пупсик)')

@bot.message_handler(func=lambda message: True)
def echo(message):
    #bot.reply_to(message, message.text)
    if message.text == '/reg':
        bot.send_message(message.from_user.id, 'Привет, как тебя зовут?')
        bot.register_next_step_handler(message, reg_name)

def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у вас фамилия?')
    bot.register_next_step_handler(message, reg_surname)

def reg_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'А какой возраст?')
    bot.register_next_step_handler(message, reg_age)

def reg_age(message):
    global age
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Вводите цифры')

    keyboard = types.InlineKeyboardMarkup()
    key_yes =types.InlineKeyboardButton(text='да', callback_data = 'yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='нет', callback_data='no')
    keyboard.add(key_no)

    qw = 'тебе ' + str(age) + 'лет? И тябя зовут ' + surname + name
    bot.send_message(message.from_user.id, text=qw, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call : True)
def callback_worker(call):
    if call.data == 'yes':
        bot.send_message(call.message.chat.id, 'приятно познакомиться')
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, 'попробуем еще раз')
        bot.send_message(call.message.chat.id, 'Привет, как тебя зовут?')
        bot.register_next_step_handler(call.message, reg_name)



bot.polling()