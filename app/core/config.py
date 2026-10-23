import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")
ADMIN_IDS = {int(id) for id in os.getenv("ADMIN_IDS").split(",")}
