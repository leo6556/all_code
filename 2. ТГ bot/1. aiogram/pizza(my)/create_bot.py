from aiogram import Bot
from aiogram.dispatcher import Dispatcher

# Для корректной работы машины состояний (сохранение данных в ОП)
from aiogram.contrib.fsm_storage.memory import MemoryStorage
storage=MemoryStorage()


bot = Bot(token='2023366758:AAFObAUVQaFss1A7FpvRRKHWX2zrCfDNyhM')
dp = Dispatcher(bot, storage=storage)
