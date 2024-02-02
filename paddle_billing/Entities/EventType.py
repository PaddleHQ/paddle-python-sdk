from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Events import EventTypeName


@dataclass
class EventType(Entity):
    name:               EventTypeName
    description:        str
    group:              str
    available_versions: list


    @classmethod
    def from_dict(cls, data: dict) -> EventType:
        return EventType(
            name               = EventTypeName(data['name']),
            description        = data['description'],
            group              = data['group'],
            available_versions = data['available_versions'],
        )
