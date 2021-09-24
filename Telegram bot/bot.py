from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler

updater = Updater(token='2031135982:AAFs8QOzmeyuy8IluYfXUeDGV7EE-CkCbDU', use_context=True)

dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, you have reached John Morgan's awesome bot!\nIf you try acting cheeky and misuse me, i'll throw it back in your face. Okay.\n\nCommands:\n/start\n/caps *text*\n/noah")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

def noah(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="❤I love you!️❤"*80)

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="WOW, look at this cheeky cunt trying bullshit commands🤡")


def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)



start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

noah_handler = CommandHandler('noah', noah)
dispatcher.add_handler(noah_handler)

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)



updater.start_polling()



