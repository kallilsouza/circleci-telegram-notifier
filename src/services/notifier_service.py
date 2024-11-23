from src.integrations.circleci.dataclasses import Event
from src.integrations.telegram.client import TelegramClient


class NotifierService:
    telegram_client = TelegramClient()

    @classmethod
    def notify_users(cls, event: Event) -> None:
        message = f"""
            New {event.type} event received.
        """

        cls.telegram_client.send_pipeline_update(message)
