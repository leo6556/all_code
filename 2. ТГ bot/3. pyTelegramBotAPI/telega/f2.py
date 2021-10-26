import telebot
from  telebot import types

# 1996839593:AAEYgxFoy7DOaTTOcXojsvDvmx_hPHlSJh0

name = ''
age = 0

bot = telebot.TeleBot('1996839593:AAEYgxFoy7DOaTTOcXojsvDvmx_hPHlSJh0')

@bot.message_handler(commands = ['start', 'help'])
def bot_reply(message):
    bot.reply_to(message, 'Привет, чем могу помочь?')

@bot.message_handler(func=lambda mess: True)
def faq(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, 'привет, как тебя зовут?')
        bot.register_next_step_handler(message, name_p)

def name_p(message):

    global name
    name = message.text
    bot.send_message(message.from_user.id, 'хорошо, спасибо, а какой у тебя возраст?')
    bot.register_next_step_handler(message, age_i)

def age_i(message):
    global age
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Вводите цифрами')

    keyboard = types.InlineKeyboardMarkup()

    k_yes = types.InlineKeyboardButton(text = 'да', callback_data='yes')
    keyboard.add(k_yes)
    k_no = types.InlineKeyboardButton(text = 'нет', callback_data='no')
    keyboard.add(k_no)
    k_maybe = types.InlineKeyboardButton(text='не знаю, я шизофреник и забыл свое имя', callback_data='maybe')
    keyboard.add(k_maybe)

    question = 'Проверь, правильно ли я записал, что тебе ' + str(age) + ' лет и тебя зовут ' + name + '?'
    bot.send_message(message.from_user.id, question, reply_markup=keyboard)

@bot.callback_query_handler(func= lambda call:True)

def callback_work(call):
    if call.data == 'yes':
        bot.send_message(call.message.chat.id, f'Приятно с тобой познакомиться {name}')
    if call.data == 'no':
        bot.send_message(call.message.chat.id, 'Давай тогда попробуем еще раз...')
        bot.send_message(call.message.chat.id, 'привет, как тебя зовут?')
        bot.register_next_step_handler(call.message, name_p)
    if call.data == 'maybe':
        bot.send_message(call.message.chat.id, 'Оу, это серьезно, вот номер психиатрической помощи, держи: 056-27-85')



bot.polling()
