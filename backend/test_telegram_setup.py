import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Bot token
TOKEN = "7540371289:AAENVwsDnn9IReOA4VOAx3Ko9a7ykR4bm4U"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text('Hey, welcome to Fastlance AI!')

async def test(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /test is issued."""
    try:
        user = update.effective_user
        chat_id = update.effective_chat.id
        
        # Send test message
        message = f"""
✅ Test Successful!

Your Info:
- Username: @{user.username}
- Chat ID: {chat_id}
"""
        await update.message.reply_text(message)
    except Exception as e:
        logger.error(f"Error in test command: {str(e)}")
        await update.message.reply_text("❌ Error during test. Please try again.")

async def main() -> None:
    """Start the bot."""
    try:
        # Create the Application
        application = Application.builder().token(TOKEN).build()

        # Add command handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("test", test))

        # Start the Bot
        logger.info("Bot is starting...")
        print("Starting Telegram bot...")
        print("Send /start or /test to your bot to verify the connection")
        
        # Start the bot and run until Ctrl+C is pressed
        await application.run_polling(allowed_updates=Update.ALL_TYPES)

    except Exception as e:
        logger.error(f"Error starting bot: {str(e)}")
        print(f"Error: {str(e)}")

if __name__ == '__main__':
    import asyncio
    asyncio.run(main()) 