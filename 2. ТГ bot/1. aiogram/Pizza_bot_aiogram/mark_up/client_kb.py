from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Расположение')
b3 = KeyboardButton('/меню')

b4 = KeyboardButton('Поделиться номером', request_contact=True)
b5 = KeyboardButton('поделиться местоположением', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)   #<-----, one_time_keyboard=True)
# one_time_kb - клавиатура исчезает после 1-ого нажатия (она просто свертывается)

kb_client.add(b1).add(b2).insert(b3).row(b4,b5)
# kb_client.row(b1,b2,b3)
