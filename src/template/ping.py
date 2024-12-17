from string import Template

from src.template.base import BaseTemplate


class PingTemplate(BaseTemplate):
    template = Template(
        "New <b>CircleCI</b> event received\n\n"
        "<b>Event details:</b>\n"
        "| Type: <b>${event_type}</b>\n"
        "| Happened at: <b>${event_happened_at}</b>\n\n"
    )

    def get_message(self):
        return self.template.substitute(
            event_type=self.event.type.upper(),
            event_happened_at=self.event.happened_at,
        )
