from jinja2 import Template
from src.template.base import BaseTemplate


class WorkflowTemplate(BaseTemplate):
    template_str = """
New <b>CircleCI</b> event received

<b>From:</b>
| Project: <b>{{ project_name }}</b>
| Org: <b>{{ org_name }}</b>

<b>Event details:</b>
| Type: <b>{{ event_type }}</b>
| Happened at: <b>{{ event_happened_at }}</b>

<b>Workflow details:</b>
| Name: <b>{{ event_workflow_name }}</b>
| Status: <b>{{ event_workflow_status }}</b>
| Created at: <b>{{ event_workflow_created_at }}</b>
| Stopped at: <b>{{ event_workflow_stopped_at }}</b>
| URL: <b>{{ event_workflow_url }}</b>

{% if event_pipeline %}<b>Pipeline details:</b>
| ID: <b>{{ event_pipeline.id }}</b>
| Number: <b>{{ event_pipeline.number }}</b>
| Created at: <b>{{ event_pipeline.created_at }}</b>{% endif %}
{% if event_pipeline and event_pipeline.trigger_parameters and event_pipeline.trigger_parameters.git %}
<b>Git information details:</b>
| Repo name: <b>{{ event_pipeline.trigger_parameters.git.repo_name }}</b>
| Repo url: <b>{{ event_pipeline.trigger_parameters.git.repo_url }}</b>
| Branch: <b>{{ event_pipeline.trigger_parameters.git.branch }}</b>
| Commit author name: <b>{{ event_pipeline.trigger_parameters.git.commit_author_name }}</b>
| Commit author email: <b>{{ event_pipeline.trigger_parameters.git.commit_author_email }}</b>{% endif %}
    """

    def get_message(self):
        template = Template(self.template_str)

        return template.render(
            project_name=self.event.project.name,
            org_name=self.event.organization.name,
            event_type=self.event.type.upper(),
            event_happened_at=self.event.happened_at,
            event_workflow_name=self.event.workflow.name,
            event_workflow_status=self.event.workflow.status.upper(),
            event_workflow_created_at=self.event.workflow.created_at,
            event_workflow_stopped_at=self.event.workflow.stopped_at,
            event_workflow_url=self.event.workflow.url,
            event_pipeline=getattr(self.event, "pipeline", None),
        )
