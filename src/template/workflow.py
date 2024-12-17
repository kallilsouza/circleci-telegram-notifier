from string import Template

from src.template.base import BaseTemplate


class WorkflowTemplate(BaseTemplate):
    template = Template(
        "New <b>CircleCI</b> event received\n\n"
        "<b>From:</b>\n"
        "| Project: <b>${project_name}</b>\n"
        "| Org: <b>${org_name}</b>\n\n"
        "<b>Event details:</b>\n"
        "| Type: <b>${event_type}</b>\n"
        "| Happened at: <b>${event_happened_at}</b>\n\n"
        "<b>Workflow details:</b>\n"
        "| Name: <b>${event_workflow_name}</b>\n"
        "| Status: <b>${event_workflow_status}</b>\n"
        "| Created at: <b>${event_workflow_created_at}</b>\n"
        "| Stopped at: <b>${event_workflow_stopped_at}</b>\n"
        "| URL: <b>${event_workflow_url}</b>\n\n"
    )

    def get_message(self):
        return self.template.substitute(
            project_name=self.event.project.name,
            org_name=self.event.organization.name,
            event_type=self.event.type.upper(),
            event_happened_at=self.event.happened_at,
            event_workflow_name=self.event.workflow.name,
            event_workflow_status=self.event.workflow.status.upper(),
            event_workflow_created_at=self.event.workflow.created_at,
            event_workflow_stopped_at=self.event.workflow.stopped_at,
            event_workflow_url=self.event.workflow.url,
        )
