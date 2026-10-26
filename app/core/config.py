import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")
ADMIN_IDS = {int(id) for id in os.getenv("ADMIN_IDS").split(",")}
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
