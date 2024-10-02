from __future__ import annotations
from abc import ABC, abstractmethod


class Entity(ABC):
    @staticmethod
    @abstractmethod
    def from_dict(data: dict):
        """
        A static factory for the entity that conforms to the Paddle API.
        """
        pass
