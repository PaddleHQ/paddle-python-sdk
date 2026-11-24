from __future__ import annotations
from abc import ABC
from dataclasses import dataclass
from datetime import datetime
import json
from typing import TYPE_CHECKING, Any

from paddle_billing.Entities.Entity import Entity as Entity
from paddle_billing.Entities.Events import EventTypeName as EventTypeName

from paddle_billing.Notifications.Entities.Entity import Entity as _NotificationEntity
from paddle_billing.Notifications.Entities.UndefinedEntity import UndefinedEntity as UndefinedEntity

from paddle_billing.Notifications.Requests import Request as Request

# Assigned rather than imported under this name, because type checkers don't treat renamed imports as public.
NotificationEntity = _NotificationEntity

if TYPE_CHECKING:
    from paddle_billing.Notifications.Requests import BodyRequest, ContentRequest, DataRequest


@dataclass
class NotificationEvent(Entity, ABC):
    notification_id: str
    event_id: str
    event_type: EventTypeName
    occurred_at: datetime
    data: NotificationEntity | UndefinedEntity

    @staticmethod
    def from_dict(data: dict[str, Any]) -> NotificationEvent:
        return NotificationEvent(
            data["notification_id"],
            data["event_id"],
            EventTypeName(data["event_type"]),
            datetime.fromisoformat(data["occurred_at"]),
            NotificationEntity.from_dict_for_event_type(data["data"], data["event_type"]),
        )

    @staticmethod
    def from_request(request: Request | BodyRequest | ContentRequest | DataRequest) -> NotificationEvent:
        raw_body = None
        if (body := getattr(request, "body", None)) is not None:
            raw_body = body.decode("utf-8")
        elif (content := getattr(request, "content", None)) is not None:
            raw_body = content.decode("utf-8")
        elif (data := getattr(request, "data", None)) is not None:
            raw_body = data.decode("utf-8")
        else:
            raise ValueError("Request does not have attr body, content, or data.")

        return NotificationEvent.from_dict(json.loads(raw_body))
