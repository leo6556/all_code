import telebot
from telebot import types
import random
bot = telebot.TeleBot('1996839593:AAEYgxFoy7DOaTTOcXojsvDvmx_hPHlSJh0')


@bot.message_handler(commands=['start'])

def welc(message):
    sti = open('poi/sticker.webp.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('😃 как дела?')
    but2 = types.KeyboardButton('🎱 рандомное число')

    markup.add(but1, but2)

    bot.send_message(message.chat.id, 'Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот, созданный, чтобы быть подопытным кроликом.'.format(message.from_user, bot.get_me()), parse_mode='html',
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def echo(message):
    if message.chat.type == 'private':
        if message.text == '🎱 рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0, 300)))
        elif message.text == '😃 как дела?':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Хорощо', callback_data='good')
            item2 = types.InlineKeyboardButton('Не очинь', callback_data='bad')
            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)

        else:
            bot.send_message(message.chat.id, 'я не знаю, что ответить 😢 😰😱😨🤯 аааааа-а')

@bot.callback_query_handler(func=lambda call:True)
def call_work(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и славно')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Хм... я могу чем=то помочь?')

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='😃 как дела?',
                                  reply_markup=None)

            bot.answer_callback_query(chat_id = call.message.chat.id, show_alert=True, text='Это тестовое уведомление!!!111')

    except Exception as e:
        print(repr(e))

bot.polling(none_stop=True)