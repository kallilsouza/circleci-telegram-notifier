from jinja2 import Template
from src.template.base import BaseTemplate


class PingTemplate(BaseTemplate):
    template_str = """
New <b>CircleCI</b> event received

<b>Event details:</b>
| Type: <b>{{ event_type }}</b>
| Happened at: <b>{{ event_happened_at }}</b>
    """

    def get_message(self):
        template = Template(self.template_str)

        return template.render(
            event_type=self.event.type.upper(),
            event_happened_at=self.event.happened_at,
        )
