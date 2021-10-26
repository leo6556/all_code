from telegram import ParseMode
from telegram import Update
from telegram.ext import CommandHandler
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater

def echo(update: Update, context: CallbackContext):

    text = [
        'Возможности тг для разметки сообщений:',
        "",
        "*MarkDown*",
        '/bold1 -- жирный шрифт',
        '/italic1 -- наклонный шрифт',
        '/erl1 -- ссылка в тексте',
        '/code1 -- работа с кодом',
        "",
        "*HTML*",
        '/bold2 -- жирный шрифт',
        '/italic2 -- наклонный шрифт',
        '/erl2 -- ссылка в тексте',
        '/code2 -- работа с кодом',
        '/img -- картинка под текстом',
    ]
    update.message.reply_text(text='\n'.join(text),
                              parse_mode=ParseMode.MARKDOWN)

def bold_md(update: Update, context: CallbackContext):
    update.message.reply_text('*Жирный* шрифт',
                              parse_mode=ParseMode.MARKDOWN)

def bold_html(update: Update, context: CallbackContext):
    update.message.reply_text('<b>Жирный</b> шрифт',
                              parse_mode=ParseMode.HTML)

def italic_md(update: Update, context: CallbackContext):
    update.message.reply_text('_наклонный_ шрийт',
                              parse_mode=ParseMode.MARKDOWN)

def italic_html(update: Update, context: CallbackContext):
    update.message.reply_text('<i>Наклонный</i> шрифт',
                              parse_mode=ParseMode.HTML)

def url_md(update: Update, context: CallbackContext):
    update.message.reply_text('Подпишись на мой [канал](https://www.youtube.com/channel/UC5dJGMTX_WDInPPFAyTXt-A), там много интересного!)',
                              parse_mode=ParseMode.MARKDOWN,
                             )

def url_html(update: Update, context: CallbackContext):
    update.message.reply_text('Подпишись на мой <a href="https://www.youtube.com/channel/UC5dJGMTX_WDInPPFAyTXt-A">канал</a>, там много интересного',
                              parse_mode=ParseMode.HTML,
                              disable_web_page_preview=False)

# #def cod_md(update:Update, context:CallbackContext):
#     text = [
#         'Примеры с кодом:',
#         '',
#         'Код на одной строке:update.message.reply_text()',
#         '',
#         'Код на нескольких строках:',
#         "эээ",
#         "update.message.reply_text(",
#         '    "xex",',
#         "    parse_mod=PM.MARDOWN,",
#         ')',
#         "эээ",
#
#     ]
#     update.message.reply_text(text='\n'.join(text),
#                               parse_mode=ParseMode.MARKDOWN)

def cod_html(update: Update, context: CallbackContext):
    text = [
        'Примеры с кодом:',
        '',
        'Код на одной строке:<code>update.message.reply_text()</code>',
        '',
        'Код на нескольких строках:',
        "<pre>",
        "update.message.reply_text(",
        '    "xex",',
        "    parse_mod=PM.MARDOWN,",
        ')',
        "</pre>",

    ]
    update.message.reply_text(text='\n'.join(text),
                              parse_mode=ParseMode.HTML)

def img_html(update: Update, context: CallbackContext):
    text = [
        'bla bla <a href="https://wampi.ru/image/RsZCtyk">&#8205</a>',
        'textttttttttttttttttttttttttttttt',
    ]
    update.message.reply_text(text='\n'.join(text),
                              parse_mode=ParseMode.HTML,
                              disable_web_page_preview=False)


def main():
     updater = Updater(
         token='1927368703:AAFL5cNCFbkmxKYoGCQZXybrB_I49SdQbOA'
     )



     updater.dispatcher.add_handler(CommandHandler('bold1', bold_md))
     updater.dispatcher.add_handler(CommandHandler('bold2', bold_html))
     updater.dispatcher.add_handler(CommandHandler('italic1', italic_md))
     updater.dispatcher.add_handler(CommandHandler('italic2', italic_html))
     updater.dispatcher.add_handler(CommandHandler('erl1', url_md))
     updater.dispatcher.add_handler(CommandHandler('erl2', url_html))
     #updater.dispatcher.add_handler(CommandHandler('code1', cod_md))
     updater.dispatcher.add_handler(CommandHandler('code2', cod_html))
     updater.dispatcher.add_handler(CommandHandler('img', img_html))

     updater.dispatcher.add_handler(MessageHandler(Filters.all, echo))



     updater.start_polling()
     updater.idle()

if __name__ == '__main__':
    main()