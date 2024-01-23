from abc import ABC, abstractmethod


class Entity(ABC):
    @classmethod
    @abstractmethod
    def make(cls, data):
        """
        A static factory for the entity that confirms to the Paddle API.
        """
        pass
