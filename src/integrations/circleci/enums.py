from enum import Enum


class EventTypes(Enum):
    WORKFLOW_COMPLETED = "workflow-completed"
    JOB_COMPLETED = "job-completed"
    PING = "ping"
