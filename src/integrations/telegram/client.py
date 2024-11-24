import asyncio
from telegram import Bot
from telegram.request import HTTPXRequest
import src.settings as settings


class TelegramClient:
    def __init__(self):
        trequest = HTTPXRequest(connection_pool_size=20)
        self.bot = Bot(token=settings.TELEGRAM_BOT_TOKEN, request=trequest)
        self.chat_ids = settings.TELEGRAM_CHAT_IDS

    async def _send_message(self, chat_id, message):
        await self.bot.send_message(chat_id, message, parse_mode="HTML")

    def send_pipeline_update(self, message: str) -> None:
        loop = asyncio.get_event_loop()
        tasks = [self._send_message(chat_id, message) for chat_id in self.chat_ids]

        if loop.is_running():
            asyncio.ensure_future(asyncio.gather(*tasks))
        else:
            loop.run_until_complete(asyncio.gather(*tasks))
