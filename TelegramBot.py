from telegram import Update
from telegram.ext import CallbackContext
import logging

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
updater = Updater(token='TOKEN', use_context=True)
dispatcher = updater.dispatcher