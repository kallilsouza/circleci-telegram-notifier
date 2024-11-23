from string import Template

from src.templates.base import BaseTemplate


class WorkflowTemplate(BaseTemplate):
    template = Template(
        "New <b>CircleCI</b> event received\n\n"
        "Type: <b>${event_type}</b>\n"
        "Workflow status: <b>${event_workflow_status}</b>\n\n"
        "Project: <b>${project_name}</b>\n"
        "Organization: <b>${org_name}</b>\n"
    )

    def get_message(self):
        return self.template.substitute(
            event_type=self.event.type.upper(),
            event_workflow_status=self.event.workflow.status.upper(),
            project_name=self.event.project.name,
            org_name=self.event.organization.name,
        )
