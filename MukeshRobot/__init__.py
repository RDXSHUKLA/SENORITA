import logging
import os
import sys
import time
import asyncio
from telegram.ext import ApplicationBuilder
from aiohttp import ClientSession
from pyrogram import Client
from telethon import TelegramClient

StartTime = time.time()

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

logging.getLogger("apscheduler").setLevel(logging.ERROR)
logging.getLogger("telethon").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)

if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error(
        "You MUST have a python version of at least 3.6! Multiple features depend on this. Bot quitting."
    )
    quit(1)

ENV = bool(os.environ.get("ENV", False))

if ENV:
    # Load configuration from environment variables
    API_ID = int(os.environ.get("API_ID", None))
    API_HASH = os.environ.get("API_HASH", None)
    ALLOW_CHATS = os.environ.get("ALLOW_CHATS", True)
    # ... (other environment variables)
    TOKEN = os.environ.get("TOKEN", None)
    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", None)
else:
    # Load configuration from a configuration file
    from MukeshRobot.config import Development as Config
    API_ID = Config.API_ID
    API_HASH = Config.API_HASH
    # ... (other config variables)
    TOKEN = Config.TOKEN
    MONGO_DB_URI = Config.MONGO_DB_URI

# Initialize bots and clients
application = ApplicationBuilder().token(TOKEN).build()
telethn = TelegramClient("mukesh", API_ID, API_HASH)
pbot = Client("MukeshRobot", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN, in_memory=True)

async def main():
    global aiohttpsession
    aiohttpsession = ClientSession()

    print("[INFO]: Getting Bot Info...")
    bot = application.bot
    BOT_ID = bot.id
    BOT_NAME = bot.first_name
    BOT_USERNAME = bot.username

    # These variables are set here after bot initialization
    from MukeshRobot import BOT_NAME, BOT_USERNAME, BOT_ID

    # Use these variables where necessary
    print(f"Bot Name: {BOT_NAME}")
    print(f"Bot Username: {BOT_USERNAME}")

    # Load handlers dynamically
    from MukeshRobot.modules.helper_funcs.handlers import (
        CustomCommandHandler,
        CustomMessageHandler,
        CustomRegexHandler,
    )

    tg.RegexHandler = CustomRegexHandler
    tg.CommandHandler = CustomCommandHandler
    tg.MessageHandler = CustomMessageHandler

# Run the main function
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
