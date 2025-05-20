from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Events import EventTypeName


@dataclass
class EventType(Entity):
    name: EventTypeName
    description: str
    group: str
    available_versions: list[Any]

    @staticmethod
    def from_dict(data: dict[str, Any]) -> EventType:
        return EventType(
            name=EventTypeName(data["name"]),
            description=data["description"],
            group=data["group"],
            available_versions=data["available_versions"],
        )
