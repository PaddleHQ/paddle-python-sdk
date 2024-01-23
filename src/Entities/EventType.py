from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Entity import Entity

from src.Entities.Events.EventTypeName import EventTypeName


@dataclass
class EventType(Entity):
    name:              EventTypeName
    description:       str
    group:             str
    availableVersions: list


    @classmethod
    def from_dict(cls, data: dict) -> EventType:
        return EventType(
            name             = EventTypeName(data['name']),
            description      = data['description'],
            group            = data['group'],
            availableVersions= data['available_versions'],
        )
