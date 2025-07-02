import os
from telegram.ext import Updater, CommandHandler

TOKEN = os.getenv("BOT_TOKEN", "WSTAW_TUTAJ_TOKEN")  # możesz też ustawić przez Render

def start(update, context):
    update.message.reply_text("Cześć! Działa z GitHub 🎉")

updater = Updater(token=TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
