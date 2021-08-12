from flask import Flask, request
from telegram import Bot, Update, ParseMode, ReplyKeyboardMarkup, ReplyKeyboardRemove, ChatAction
from telegram.ext import *
import consts
import logging
import json
# import messages_parser
import sandbox


def start(update, context):
    update.message.reply_text("start")


def respond(update, context):
    user_input = str(update.message.text).lower()
    response = sandbox.google_reply(user_input)
    if response is not None and response != 1:
        update.message.reply_text(response)


app = Flask(__name__)


def main():
    logging.basicConfig(filename='TesBot.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    bot = Bot(consts.TELEGRAM_TOKEN)
    dp = Dispatcher(bot, None, workers=0, use_context=True)

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, respond))

    bot.delete_webhook()
    url = consts.MY_URL + '/' + consts.TELEGRAM_TOKEN
    bot.set_webhook(url=url)

    @app.route('/' + consts.TELEGRAM_TOKEN, methods=['POST'])
    def webhook():
        json_string = request.stream.read().decode('utf-8')
        update = Update.de_json(json.loads(json_string), bot)
        dp.process_update(update)
        return 'ok', 200


if __name__ == 'main':
    main()

    
# thanks to t.me/yehuda100 for his help in deploying the bot properly to pythonanywhere.com
