from string import Template

from src.integrations.circleci.dataclasses import Event
from src.integrations.telegram.client import TelegramClient


class NotifierService:
    telegram_client = TelegramClient()

    @classmethod
    def notify_users(cls, event: Event) -> None:
        template = Template(
            "New <b>${event_type}</b> event received.\n\n"
            "Project: <b>${project_name}</b>\n"
            "Organization: <b>${org_name}</b>"
        )
        message = template.substitute(
            event_type=event.type,
            project_name=event.project.name,
            org_name=event.organization.name,
        )

        cls.telegram_client.send_pipeline_update(message)
