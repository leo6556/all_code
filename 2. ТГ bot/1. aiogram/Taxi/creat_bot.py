from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher

storage = MemoryStorage()
bot = Bot(token='2023366758:AAFObAUVQaFss1A7FpvRRKHWX2zrCfDNyhM')
dp = Dispatcher(bot, storage=storage)