from src.integrations.circleci.dataclasses import Event
from src.integrations.telegram.client import TelegramClient
from src.factories.template_factory import TemplateFactory


class NotifierService:
    telegram_client = TelegramClient()

    @classmethod
    def notify_users(cls, event: Event) -> None:
        template = TemplateFactory(event).get_template()
        message = template.get_message()

        cls.telegram_client.send_pipeline_update(message)
