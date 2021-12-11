from aiogram import types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import bot, dp
from aiogram.dispatcher.filters import Text
from database import add_sql, show_menu2, del_sql
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ID = None

class admin(StatesGroup):
    photo = State()
    name = State()
    desc = State()
    price = State()

# Получение доступа к админке (только администраторам группы)
# @dp.message_handler(commands='moderator', is_chat_admin = True)
async def make_access(message : types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Whats you want')
    await message.delete()


# @dp.message_handler(commands='Загрузить', state=None)
async def start(message : types.Message):
    if message.from_user.id == ID:
        await admin.photo.set()
        await message.reply('Загрузи фото')


# @dp.message_handler(content_types=['photo'], state=admin.photo)
async def load_photo(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await admin.next()
    await message.reply('Теперь введите название')

# @dp.message_handler(state=admin.name)
async def load_name(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await admin.next()
    await message.reply('Введите описание')

# @dp.message_handler(state=admin.desc)
async def load_desc(messsage : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['desc'] = messsage.text
    await admin.next()
    await messsage.reply('Теперь укажи цену')

# @dp.message_handler(state= admin.price)
async def load_price(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)

    # async with state.proxy() as data:
    #     await message.reply(str(data))

    await add_sql(state)

    await state.finish()

#Выход из состояний
# @dp.message_handler(state='*', commands='отмена')
# @dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_han(message : types.Message, state = admin):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('OK')

# @dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_call(callback : types.CallbackQuery):
    await del_sql(callback.data.replace('del ', ''))
    await callback.message.answer('Удалено')

# @dp.message_handler(commands='удалить')
async def dell(message : types.Message):
    read = await show_menu2()
    for i in read:
        await bot.send_photo(message.from_user.id, i[0], f'{i[1], i[2]}')
        await bot.send_message(message.from_user.id, text='***', reply_markup=InlineKeyboardMarkup().\
                               add(InlineKeyboardButton(f'Удалить {i[1]}', callback_data=f'del {i[1]}')))

def reg_admin(dp : Dispatcher):
    dp.register_message_handler(make_access, commands='moderator', is_chat_admin=True)
    dp.register_message_handler(start, commands='Загрузить', state=None)
    dp.register_message_handler(load_photo, content_types=['photo'], state=admin.photo)
    dp.register_message_handler(load_name, state=admin.name)
    dp.register_message_handler(load_desc, state=admin.desc)
    dp.register_message_handler(load_price, state= admin.price)
    dp.register_message_handler(cancel_han, state='*', commands='отмена')
    dp.register_message_handler(cancel_han, Text(equals='отмена'), state='*')
    dp.register_message_handler(make_access, commands='moderator', is_chat_admin = True)
