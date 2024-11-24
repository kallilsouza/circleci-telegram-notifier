import json

from src.integrations.circleci.dataclasses import (
    Event,
    Job,
    Workflow,
    Organization,
    Project,
)
from src.services.notifier_service import NotifierService


def lambda_handler(event, context):
    event_data = json.loads(event["Records"][0]["Sns"]["Message"])

    service = NotifierService()

    if project_data := event_data.pop("project", None):
        event_data["project"] = Project(**project_data)

    if organization_data := event_data.pop("organization", None):
        event_data["organization"] = Organization(**organization_data)

    if job_data := event_data.pop("job", None):
        event_data["job"] = Job(**job_data)

    if workflow_data := event_data.pop("workflow", None):
        event_data["workflow"] = Workflow(**workflow_data)

    event = Event(**event_data)
    service.notify_users(event)
