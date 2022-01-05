from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode

# Главный каталог

markup_main_panel = InlineKeyboardMarkup()

but1 = InlineKeyboardButton("Косметология", callback_data="pri_cos")
but2 = InlineKeyboardButton("Парикмахерская", callback_data="pri_bar")
but3 = InlineKeyboardButton("Маникюр", callback_data="pri_man")
but4 = InlineKeyboardButton("Педикюр", callback_data="pri_ped")
# but55 = InlineKeyboardButton('Перейти к записи на приём', callback_data="sighup")

markup_main_panel.row(but1, but2).row(but3, but4)

async def main_panel_price(message : types.Message):
    await message.answer('Выберите категорию', reply_markup=markup_main_panel)


# Подкаталоги

markup_main_panel_bar = InlineKeyboardMarkup()
butt1 = InlineKeyboardButton('Женский зал', callback_data='sub_hall_w')
butt2 = InlineKeyboardButton('Мужcкой + детский', callback_data='pri_bar_m')
butt304 = InlineKeyboardButton('Назад', callback_data='back_man')
markup_main_panel_bar.row(butt1, butt2).add(butt304)
async def main_panel_bar_1(callback : types.CallbackQuery):
    await callback.message.edit_text('Выберите необходимый зал 💇🏼‍♀️', reply_markup=markup_main_panel_bar)
    await callback.answer()


markup_main_panel_bar_women = InlineKeyboardMarkup()
butt3 = InlineKeyboardButton('Стрижки', callback_data='pri_cut')
butt4 = InlineKeyboardButton('Укладки-прически', callback_data='pri_laying')
butt5 = InlineKeyboardButton('Наращивание-окрашивание', callback_data='pri_coloring')
butt6 = InlineKeyboardButton('Уход за волосами', callback_data='pri_care')
butt7 = InlineKeyboardButton('Назад', callback_data="back_bar_hall")
markup_main_panel_bar_women.row(butt3, butt4).row(butt6, butt5).add(butt7)
async def main_panel_bar_w(callback : types.CallbackQuery):
    await callback.message.edit_text('Выберите подкатегорию 💆🏼‍♀️', reply_markup=markup_main_panel_bar_women, parse_mode=ParseMode.MARKDOWN)
    await callback.answer()


markup_main_panel_cos = InlineKeyboardMarkup()
butt8 = InlineKeyboardButton('Брови', callback_data='pri_brow')
butt9 = InlineKeyboardButton('Ресницы', callback_data='pri_lash')
butt10 = InlineKeyboardButton('Другое', callback_data='pri_ear')
butt11 = InlineKeyboardButton('Лаз. эпиляция', callback_data='pri_epil')
butt12 = InlineKeyboardButton('Депиляция воском', callback_data='pri_depil')
butt13 = InlineKeyboardButton('Уход за кожей', callback_data='pri_face')
butt14 = InlineKeyboardButton('Назад', callback_data="back_man")
markup_main_panel_cos.row(butt8, butt9).row(butt12, butt13).row(butt11, butt10).add(butt14)
async def main_panel_cos(callback : types.CallbackQuery):
    await callback.message.edit_text('Выберите нужную подкатегорию 💆🏼‍♀️', reply_markup=markup_main_panel_cos, parse_mode=ParseMode.MARKDOWN)
    await callback.answer()

# Перемотка в меню каталога + возвращение в главный каталог

markup_2 = InlineKeyboardMarkup()
but4 = InlineKeyboardButton('  <<  ', callback_data='next_man')
but5 = InlineKeyboardButton('назад', callback_data="back_man")
but6 = InlineKeyboardButton('  >>  ', callback_data='next_man')
markup_2.row(but4, but5, but6)
async def sec_cat_man(callback : types.CallbackQuery, text):
    await callback.message.edit_text(text=text, reply_markup=markup_2, parse_mode=ParseMode.MARKDOWN)
    await callback.answer()

markup_3 = InlineKeyboardMarkup()
but7 = InlineKeyboardButton('  <<  ', callback_data='next_ped')
but8 = InlineKeyboardButton('назад', callback_data="back_ped")
but9 = InlineKeyboardButton('  >>  ', callback_data='next_ped')
markup_3.row(but7, but8, but9)
async def sec_cat_ped(callback : types.CallbackQuery, text):
    await callback.message.edit_text(text=text, reply_markup=markup_3, parse_mode=ParseMode.MARKDOWN)
    await callback.answer()


markup_4 = InlineKeyboardMarkup()
but10 = InlineKeyboardButton('  <<  ', callback_data='next_bar_m')
but11 = InlineKeyboardButton('назад', callback_data="back_bar_hall")
but12 = InlineKeyboardButton('  >>  ', callback_data='next_bar_m')
markup_4.row(but11)
async def third_cat_bar_m(callback : types.CallbackQuery, text):
    await callback.message.edit_text(text=text, reply_markup=markup_4, parse_mode=ParseMode.MARKDOWN)
    await callback.answer()



markup_5 = InlineKeyboardMarkup()
but13 = InlineKeyboardButton('  <<  ', callback_data='next_bar_w')
but14 = InlineKeyboardButton('назад', callback_data="back_panel_bar")
but15 = InlineKeyboardButton('  >>  ', callback_data='next_bar_w')
markup_5.row(but14)
async def third_cat_bar_cut(callback : types.CallbackQuery, text):
    await callback.message.edit_text(text=text, reply_markup=markup_5, parse_mode=ParseMode.MARKDOWN)
    await callback.answer()

markup_6 = InlineKeyboardMarkup()
but16 = InlineKeyboardButton('  <<  ', callback_data='next_bar_w')
but17 = InlineKeyboardButton('назад', callback_data="back_panel_bar")
but18 = InlineKeyboardButton('  >>  ', callback_data='next_bar_w')
markup_6.row(but17)
async def third_cat_bar_laying(callback : types.CallbackQuery, text):
    await callback.message.edit_text(text=text, reply_markup=markup_6, parse_mode=ParseMode.MARKDOWN)
    await callback.answer()

markup_7 = InlineKeyboardMarkup()
but19 = InlineKeyboardButton('  <<  ', callback_data='next_bar_w')
but20 = InlineKeyboardButton('назад', callback_data="back_panel_bar")
but21 = InlineKeyboardButton('  >>  ', callback_data='next_bar_w')
markup_7.row(but20)
async def third_cat_bar_care(callback : types.CallbackQuery, text):
    await callback.message.edit_text(text=text, reply_markup=markup_7, parse_mode=ParseMode.MARKDOWN)
    await callback.answer()

markup_8 = InlineKeyboardMarkup()
but22 = InlineKeyboardButton('  <<  ', callback_data='next_bar_w')
but23 = InlineKeyboardButton('назад', callback_data="back_panel_bar")
but24 = InlineKeyboardButton('  >>  ', callback_data='next_bar_w')
markup_8.row(but23)
async def third_cat_bar_coloring(callback : types.CallbackQuery, text):
    await callback.message.edit_text(text=text, reply_markup=markup_8, parse_mode=ParseMode.MARKDOWN)
    await callback.answer()


# ШАБЛОН ШАБЛОНАМ
async def shablon(callback : types.CallbackQuery, text, nexty, backy):

    markup_sh = InlineKeyboardMarkup()
    but_1 = InlineKeyboardButton('  <<  ', callback_data=f'next_{nexty}')  # next_cos_epil
    but_2 = InlineKeyboardButton('назад', callback_data=f"back_{backy}")   # back_panel_cos
    but_3 = InlineKeyboardButton('  >>  ', callback_data=f'next_{nexty}')
    markup_sh.row(but_2)

    await callback.message.edit_text(text=text, reply_markup=markup_sh, parse_mode=ParseMode.MARKDOWN)
    await callback.answer()