import asyncio

from telegram import Bot
from telegram.request import HTTPXRequest

import src.settings as settings


class TelegramClient:
    def __init__(self):
        trequest = HTTPXRequest(connection_pool_size=20)
        self.bot = Bot(token=settings.TELEGRAM_BOT_TOKEN, request=trequest)
        self.chat_ids = settings.TELEGRAM_CHAT_IDS

    def send_pipeline_update(self, message: str) -> None:
        for chat_id in self.chat_ids:
            asyncio.run(self.bot.send_message(chat_id, message, parse_mode="HTML"))
