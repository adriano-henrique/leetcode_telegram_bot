import telegram
from scrapper_lc import LCScrapper
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler,Filters
import logging
from variables import TOKEN
from messages import default_message, start_message, help_message
from functions import sendMessage

print(TOKEN)
bot = telegram.Bot(token = TOKEN)
print(bot.get_me())

handler_list = []

updater = Updater(token=TOKEN,use_context=True)

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def start(update, context):
    sendMessage(context,update.effective_chat.id, start_message)

start_handler = CommandHandler('start',start)
dispatcher.add_handler(start_handler)

def help(update, context):
    sendMessage(context, update.effective_chat.id, help_message)

help_handler = CommandHandler('help',help)
dispatcher.add_handler(help_handler)

def default(update,context):
    sendMessage(context,update.effective_chat.id, default_message)

default_handler = MessageHandler(Filters.text,default)
dispatcher.add_handler(default_handler)

def easy(update, context):
    scrapper = LCScrapper()
    message = scrapper.getEasyQuestion()

    sendMessage(context, update.effective_chat.id, message)

easy_handler = CommandHandler('easy',easy)
dispatcher.add_handler(easy_handler)

def medium(update, context):
    scrapper = LCScrapper()
    message = scrapper.getMediumQuestion()

    sendMessage(context, update.effective_chat.id, message)

medium_handler = CommandHandler('medium', medium)
dispatcher.add_handler(medium_handler)


def hard(update, context):
    scrapper = LCScrapper()
    message = scrapper.getHardQuestion()

    sendMessage(context, update.effective_chat.id, message)

hard_handler = CommandHandler('hard', hard)
dispatcher.add_handler(hard_handler)


def daily(update, context):
    scrapper = LCScrapper()
    message = scrapper.getDesiredQuestions(1,1,1)

    sendMessage(context, update.effective_chat.id, message)

daily_handler = CommandHandler('daily', daily)
dispatcher.add_handler(daily_handler)


def weekly(update, context):
    scrapper = LCScrapper()
    message = scrapper.getDesiredQuestions(5,3,2)

    sendMessage(context, update.effective_chat.id, message)

weekly_handler = CommandHandler('weekly', weekly)
dispatcher.add_handler(weekly_handler)

updater.start_polling()



