from __future__ import annotations
from abc import ABC
from dataclasses import dataclass
from datetime import datetime
import json

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Events import EventTypeName

from paddle_billing.Notifications.Entities.Entity import Entity as NotificationEntity
from paddle_billing.Notifications.Entities.UndefinedEntity import UndefinedEntity

from paddle_billing.Notifications.Requests import Request


@dataclass
class NotificationEvent(Entity, ABC):
    notification_id: str
    event_id: str
    event_type: EventTypeName
    occurred_at: datetime
    data: NotificationEntity | UndefinedEntity

    @staticmethod
    def from_dict(data: dict) -> NotificationEvent:
        return NotificationEvent(
            data["notification_id"],
            data["event_id"],
            EventTypeName(data["event_type"]),
            datetime.fromisoformat(data["occurred_at"]),
            NotificationEntity.from_dict_for_event_type(data["data"], data["event_type"]),
        )

    @staticmethod
    def from_request(request: Request) -> NotificationEvent:
        raw_body = None
        if hasattr(request, "body"):
            raw_body = request.body.decode("utf-8")
        elif hasattr(request, "content"):
            raw_body = request.content.decode("utf-8")
        elif hasattr(request, "data"):
            raw_body = request.data.decode("utf-8")

        return NotificationEvent.from_dict(json.loads(raw_body))
