from main import bot, dp
from aiogram.types import Message

# async def send_to_admin(dp):
#     print('Бот запущен')
#     await bot.send_message(chat_id='мой айди', text='Бот запущен')

@dp.message_handler()
async def echo(message: Message):
    text = f"привет ты написал {message.text}"
    await message.reply(text)
    await message.answer(text)