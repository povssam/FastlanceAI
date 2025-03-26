import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey, welcome to Fastlance AI!")

async def test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Test successful!")

if __name__ == "__main__":
    app = ApplicationBuilder().token("7540371289:AAENVwsDnn9IReOA4VOAx3Ko9a7ykR4bm4U").build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('test', test))

    app.run_polling()