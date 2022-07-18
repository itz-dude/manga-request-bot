from pyrogram import Client
from dotenv import load_dotenv

import os

load_dotenv()

# Setting up Telethon Client
# API_ID = os.getenv('API_ID')
# API_HASH = os.getenv('API_HASH')
# BOT_TOKEN = os.getenv('BOT_TOKEN')
API_ID = os.environ.get('API_ID')
API_HASH = os.environ.get('API_HASH')
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)