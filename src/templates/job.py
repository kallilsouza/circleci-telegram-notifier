from string import Template

from src.templates.base import BaseTemplate


class JobTemplate(BaseTemplate):
    template = Template(
        "New <b>CircleCI</b> event received\n\n"
        "<b>From:</b>\n"
        "| Project: <b>${project_name}</b>\n"
        "| Org: <b>${org_name}</b>\n\n"
        "<b>Event details:</b>\n"
        "| Type: <b>${event_type}</b>\n"
        "| Happened at: <b>${event_happened_at}</b>\n\n"
        "<b>Job details:</b>\n"
        "| Name: <b>${event_job_name}</b>\n"
        "| Status: <b>${event_job_status}</b>\n"
        "| Created at: <b>${event_job_started_at}</b>\n"
        "| Stopped at: <b>${event_job_stopped_at}</b>\n\n"
        "<b>Workflow details:</b>\n"
        "| Name: <b>${event_workflow_name}</b>\n"
        "| URL: <b>${event_workflow_url}</b>\n\n"
    )

    def get_message(self):
        return self.template.substitute(
            project_name=self.event.project.name,
            org_name=self.event.organization.name,
            event_type=self.event.type.upper(),
            event_happened_at=self.event.happened_at,
            event_job_name=self.event.job.name,
            event_job_status=self.event.job.status.upper(),
            event_job_started_at=self.event.job.started_at,
            event_job_stopped_at=self.event.job.stopped_at,
            event_workflow_name=self.event.workflow.name,
            event_workflow_url=self.event.workflow.url,
        )
