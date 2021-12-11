from aiogram import executor

from loader import dp
import handlers # middlewares, filters,
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands

# from handlers.users.price import reg_price
# from handlers.users.echo import reg_echo


async def on_startup(dispatcher):
    pass
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)



if __name__ == '__main__':

    # reg_price(dp)
    # reg_echo(dp)
    executor.start_polling(dp, on_startup=on_startup)

