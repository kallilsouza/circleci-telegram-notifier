import json

import src.responses.status as status

from src.integrations.circleci.dataclasses import Event, Job, Workflow
from src.responses.classes import HttpResponse
from src.services.notifier_service import NotifierService


def lambda_handler(event, context):
    event_data = json.loads(event.get("body"))

    service = NotifierService()

    if job_data := event_data.pop("job", None):
        event_data["job"] = Job(**job_data)

    if workflow_data := event_data.pop("workflow", None):
        event_data["workflow"] = Workflow(**workflow_data)

    event = Event(**event_data)
    service.notify_users(event)

    return HttpResponse(data={}, status_code=status.HTTP_204_NO_CONTENT).send()
