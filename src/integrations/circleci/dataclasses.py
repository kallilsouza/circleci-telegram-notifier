# https://circleci.com/docs/webhooks-reference/
from dataclasses import dataclass

from src.integrations.circleci.enums import EventTypes


@dataclass
class Project:
    """Project associated with the webhook event."""

    id: str
    name: str
    slug: str


@dataclass
class Organization:
    """Organization associated with the webhook event."""

    id: str
    name: str


@dataclass
class Job:
    """
    Job associated with the webhook event.
    A job typically represents one phase in a CircleCI workload (for example, "build", "test", or "deploy") and contains a series of steps.
    """

    id: str
    number: str
    name: str
    status: str
    started_at: str
    stopped_at: str | None


@dataclass
class Workflow:
    """
    Workflow associated with the webhook event.
    Workflows orchestrate jobs.
    """

    id: str
    name: str
    status: str | None
    created_at: str
    stopped_at: str | None
    url: str


@dataclass
class Trigger:
    """Trigger associated with the webhook event."""

    type: str


@dataclass
class CircleCI:
    """Event metadata for trigger."""

    event_time: str
    event_type: str
    trigger_type: str
    actor_id: str | None


@dataclass
class TriggerParameters:
    """Trigger data associated to the pipeline"""

    circleci: CircleCI
    git: dict | None
    gitlab: dict | None


@dataclass
class Pipeline:
    """
    Pipeline associated with the webhook event.

    Pipelines are the most high-level unit of work, and contain zero or more workflows.
    A single git-push always triggers up to one pipeline.
    Pipelines can also be triggered manually through the API.
    """

    id: str
    number: str
    created_at: str
    trigger: Trigger
    trigger_parameters: TriggerParameters | None
    vcs: dict | None


@dataclass
class Event:
    """Webhook event."""

    id: str
    type: EventTypes
    happened_at: str
    webhook: dict
    project: Project
    organization: Organization
    pipeline: Pipeline
    job: Job | None = None
    workflow: Workflow | None = None
