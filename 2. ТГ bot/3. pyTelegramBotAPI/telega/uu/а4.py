import requests
from datetime import datetime
import telebot

bot = telebot.TeleBot('1996839593:AAEYgxFoy7DOaTTOcXojsvDvmx_hPHlSJh0')

@bot.message_handler(commands=['start'])
def tgbot(message):
    bot.send_message(message.chat.id, 'Привет, здесь ты можешь узнать цену на биткоин!')

@bot.message_handler(content_types=['text'])
def send(message):
    if message.text == 'price':
        try:
            req = requests.get('https://yobit.net/api/3/ticker/btc_rur')
            response = req.json()
            sell_price = int(response['btc_rur']['sell'])

            bot.send_message(message.chat.id,
                             f'{datetime.now()}\nSell BTC Price: {sell_price} рублей 😱')
        except Exception as ex:
            print(ex)
            bot.send_message(message.chat.id, 'Что=то пошло не так')

    else:
        bot.send_message(message.chat.id, 'Если хочешь узнать цену вводи: "price"')



bot.polling()
