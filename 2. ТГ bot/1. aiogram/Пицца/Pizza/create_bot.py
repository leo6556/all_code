from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher

from aiogram.contrib.fsm_storage.memory import MemoryStorage
storage=MemoryStorage()

bot = Bot(token='2023366758:AAFObAUVQaFss1A7FpvRRKHWX2zrCfDNyhM')
dp = Dispatcher(bot, storage=storage)