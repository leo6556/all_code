from aiogram import Bot, Dispatcher, executor, types
from aiogram.bot import api

bot = Bot(
    token='1940112781:AAFapfgmszNYUYFGLOITgshBLgAF5hSG1SA'
)

dp = Dispatcher(
    bot=bot
)

@dp.message_handler(commands=['help'])
async def send_menu(message: types.Message):
    await message.reply(
        text='''
        Это мой первый бот на айограмм''',
        reply=False,
    )

@dp.message_handler(commands=['start'])
async def send_welcom(message: types.Message):
    await message.reply('HELLOMLOY')

    await send_menu(message=message)


@dp.message_handler(content_types=types.ContentType.TEXT)
async def do_echo(message: types.Message):
    text = message.text
    if text:
        await message.reply(text=text)

def main():
    executor.start_polling(
        dispatcher=dp
    )

if __name__ == '__main__':
    main()



