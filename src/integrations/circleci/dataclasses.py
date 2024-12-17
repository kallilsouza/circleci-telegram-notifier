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
    stopped_at: str | None = None


@dataclass
class Workflow:
    """
    Workflow associated with the webhook event.
    Workflows orchestrate jobs.
    """

    id: str
    name: str
    url: str
    created_at: str
    stopped_at: str | None = None
    status: str | None = None


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
    actor_id: str | None = None


@dataclass
class Git:
    commit_author_name: str
    repo_owner: str
    branch: str
    commit_message: str
    repo_url: str
    ref: str
    author_avatar_url: str
    checkout_url: str
    author_login: str
    repo_name: str
    commit_author_email: str
    checkout_sha: str
    default_branch: str


@dataclass
class TriggerParameters:
    """Trigger data associated to the pipeline"""

    circleci: CircleCI
    git: Git | None = None
    gitlab: dict | None = None
    github_app: dict | None = None
    webhook: dict | None = None


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
    trigger_parameters: TriggerParameters | None = None
    vcs: dict | None = None


@dataclass
class Event:
    """Webhook event."""

    id: str
    type: EventTypes
    happened_at: str
    webhook: dict
    project: Project | None = None
    organization: Organization | None = None
    job: Job | None = None
    workflow: Workflow | None = None
    pipeline: Pipeline | None = None
