from abc import ABC, abstractmethod

from src.integrations.circleci.dataclasses import Event


class BaseTemplate(ABC):
    def __init__(self, event: Event):
        self.event = event

    @abstractmethod
    def get_message(self):
        pass
