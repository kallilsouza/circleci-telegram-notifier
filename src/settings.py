import os
from dotenv import load_dotenv

load_dotenv()

CIRCLECI_SECRET = os.getenv("CIRCLECI_SECRET")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_IDS = os.getenv("TELEGRAM_CHAT_IDS", "").split(",")
