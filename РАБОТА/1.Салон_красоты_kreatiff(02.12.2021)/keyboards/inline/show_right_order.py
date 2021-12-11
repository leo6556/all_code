import time

from states.sighup import *

from aiogram import types, bot
from aiogram.dispatcher import FSMContext

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from DB.db2_manage import *



markup22 = InlineKeyboardMarkup()
but1 = InlineKeyboardButton('Подробнее', callback_data='show_more')
but2 = InlineKeyboardButton('Отменить', callback_data='show_stop')
markup22.row(but1, but2)


markup33 = InlineKeyboardMarkup()
but1 = InlineKeyboardButton('Скрыть', callback_data='show_less')
but2 = InlineKeyboardButton('Отменить', callback_data='show_stop')
markup33.row(but1,but2)


markup44 = InlineKeyboardMarkup()
but1 = InlineKeyboardButton('Удалить', callback_data='show_del')
but2 = InlineKeyboardButton('Вернуться', callback_data='show_less_back')
markup44.row(but1,but2)