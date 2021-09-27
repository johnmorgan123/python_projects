from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler
import random


class QPRBot:

    def __init__(self, stories):
        self.updater = Updater(token='2031135982:AAFs8QOzmeyuy8IluYfXUeDGV7EE-CkCbDU', use_context=True)
        self.dispatcher = self.updater.dispatcher
        self.stories = stories

    def start_bot(self):

        start_handler = CommandHandler('start', self.start)
        self.dispatcher.add_handler(start_handler)

        echo_handler = MessageHandler(Filters.text & (~Filters.command), self.echo)
        self.dispatcher.add_handler(echo_handler)

        caps_handler = CommandHandler('caps', self.caps)
        self.dispatcher.add_handler(caps_handler)

        noah_handler = CommandHandler('noah', self.noah)
        self.dispatcher.add_handler(noah_handler)

        qpr_handler = CommandHandler('qpr', self.qpr)
        self.dispatcher.add_handler(qpr_handler)

        unknown_handler = MessageHandler(Filters.command, self.unknown)
        self.dispatcher.add_handler(unknown_handler)

        inline_caps_handler = InlineQueryHandler(self.inline_caps)
        self.dispatcher.add_handler(inline_caps_handler)

        print("starting bot")

        self.updater.start_polling()

    def start(self, update, context):
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Hello, you have reached John Morgan's awesome bot!\nIf you try acting cheeky and misuse me, i'll throw it back in your face. Okay.\n\nCommands:\n/start\n/caps *text*\n/noah\n/qpr")

    def echo(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

    def caps(self, update, context):
        text_caps = ' '.join(context.args).upper()
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

    def noah(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="❤I love you!️❤"*80)

    def qpr(self, update, context):
        story = self.get_a_story()
        context.bot.send_message(chat_id=update.effective_chat.id, text=story.content[:4095])

    def unknown(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="WOW, look at this cheeky cunt trying bullshit commands🤡")


    def get_a_story(self):
        story = random.choice(self.stories)
        print(f"selected a store {len(story.content)} characters long")
        return story

    def inline_caps(self, update, context):
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
