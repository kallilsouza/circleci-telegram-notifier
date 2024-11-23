import asyncio

import src.settings as settings
from telegram import Bot


class TelegramClient:
    def __init__(self):
        self.bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
        self.chat_ids = settings.TELEGRAM_CHAT_IDS

    def send_pipeline_update(self) -> None:
        for chat_id in self.chat_ids:
            asyncio.run(self.bot.send_message(chat_id, "test"))
