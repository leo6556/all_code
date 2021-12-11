from aiogram.dispatcher.filters.state import State, StatesGroup

from loader import dp


class Client(StatesGroup):
    service = State()
    master = State()
    date = State()
    time = State()
    contact = State()

