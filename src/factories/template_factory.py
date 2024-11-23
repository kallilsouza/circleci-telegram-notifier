from src.templates.base import BaseTemplate
from src.templates.workflow import WorkflowTemplate
from src.integrations.circleci.dataclasses import Event
from src.integrations.circleci.enums import EventTypes


EVENT_TYPE_TEMPLATE_MAPPING = {EventTypes.WORKFLOW_COMPLETED.value: WorkflowTemplate}


class TemplateFactory:
    def __init__(self, event: Event):
        self.event = event

    def get_template(self) -> BaseTemplate:
        return EVENT_TYPE_TEMPLATE_MAPPING.get(self.event.type)(self.event)
