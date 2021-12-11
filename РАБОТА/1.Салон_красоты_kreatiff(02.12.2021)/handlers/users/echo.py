from aiogram import types, Dispatcher

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart, CommandHelp
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.panel_price import main_panel_price
from keyboards.inline.panel_state_sighup import main_panel
from loader import dp, bot
from states.sighup import Client


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):

    text = [
        f'*Доброго времени суток*, {message.from_user.first_name} 🤗',
        "Добро пожаловать в салон красоты *'Креатиff'!*",
        '',
        'Буквально за минуту ты можешь посмотреть цены и записаться на необходимую процедуру 🤓',
        '',
        '*Выбери нужную операцию* (можно просто нажать на //команду):',
        '',
        '🖌 /sighup -- записаться на прием',
        '',
        '💳 /price -- цены на наши услуги',
        '',
        '📋 /myorders -- мои заказы',
        '',
        '🤝 /help -- помощь'
    ]

    await message.answer(text='\n'.join(text), parse_mode=ParseMode.MARKDOWN)


# *************************************************************
@dp.message_handler(commands='sighup', state=None)
async def start_state(message : types.Message):
    await Client.service.set()
    await main_panel(message)
#**************************************************************
@dp.message_handler(commands='price')
async def start_price(message : types.Message):
    await main_panel_price(message)
# ************************************************************

@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = (
        ""
        "Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку")
    ter =  '''
    📍 Список команд: /sighup, /price,   
/myordedrs, /help
📍 Для того, чтобы активировать команду можно: или нажать прямо на команду (она выделеяется синим
 шрифтом) или отправить команду обычной клавиатурой.
📍 Пожелания для улучшения сервиса и отладки ошибок можете направлять на контакт: @lielie45
    '''
    await message.answer(text=ter)



@dp.message_handler(state=None)
async def bot_echo(message: types.Message):

    await message.answer('Если хотите записаться в салон красоты, нажмите на команду 👉🏼 "/start"')



# # Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
# @dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
# async def bot_echo_all(message: types.Message, state: FSMContext):
#     state = await state.get_state()
#     await message.answer(f"Эхо в состоянии <code>{state}</code>.\n"
#                          f"\nСодержание сообщения:\n"
#                          f"<code>{message}</code>")


# def reg_echo(dp : Dispatcher):
#     dp.register_message_handler(bot_start, commands='start'),
#     dp.register_message_handler(bot_help, commands='help'),
#     dp.register_message_handler(bot_echo)