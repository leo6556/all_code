from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

but_load = KeyboardButton('/load')
but_delete = KeyboardButton('/удалить')

button_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(but_load).add(but_delete)