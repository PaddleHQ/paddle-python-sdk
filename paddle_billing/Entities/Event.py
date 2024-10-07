from __future__ import annotations
from abc import ABC
from dataclasses import dataclass
from datetime import datetime

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Events import EventTypeName

from paddle_billing.Notifications.Entities.Entity import Entity as NotificationEntity
from paddle_billing.Notifications.Entities.UndefinedEntity import UndefinedEntity


@dataclass
class Event(Entity, ABC):
    event_id: str
    event_type: EventTypeName
    occurred_at: datetime
    data: NotificationEntity | UndefinedEntity

    @staticmethod
    def from_dict(data: dict) -> Event:
        return Event(
            data["event_id"],
            EventTypeName(data["event_type"]),
            datetime.fromisoformat(data["occurred_at"]),
            NotificationEntity.from_dict_for_event_type(data["data"], data["event_type"]),
        )
