from src.template.base import BaseTemplate
from src.template.ping import PingTemplate
from src.template.job import JobTemplate
from src.template.workflow import WorkflowTemplate
from src.integrations.circleci.dataclasses import Event
from src.integrations.circleci.enums import EventTypes


EVENT_TYPE_TEMPLATE_MAPPING = {
    EventTypes.WORKFLOW_COMPLETED.value: WorkflowTemplate,
    EventTypes.PING.value: PingTemplate,
    EventTypes.JOB_COMPLETED.value: JobTemplate,
}


class TemplateFactory:
    def __init__(self, event: Event):
        self.event = event

    def get_template(self) -> BaseTemplate:
        return EVENT_TYPE_TEMPLATE_MAPPING.get(self.event.type)(self.event)
