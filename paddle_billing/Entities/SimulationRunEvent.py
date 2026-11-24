from __future__ import annotations
from abc import ABC
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Entities.Entity import Entity as Entity
from paddle_billing.Entities.Events import EventTypeName as EventTypeName
from paddle_billing.Entities.SimulationRunEvents import (
    SimulationRunEventStatus as SimulationRunEventStatus,
    SimulationRunEventRequest as SimulationRunEventRequest,
    SimulationRunEventResponse as SimulationRunEventResponse,
)

from paddle_billing.Notifications.Entities.Entity import Entity as _NotificationEntity
from paddle_billing.Notifications.Entities.UndefinedEntity import UndefinedEntity as UndefinedEntity

# Assigned rather than imported under this name, because type checkers don't treat renamed imports as public.
NotificationEntity = _NotificationEntity


@dataclass
class SimulationRunEvent(Entity, ABC):
    id: str
    status: SimulationRunEventStatus
    event_type: EventTypeName
    payload: NotificationEntity | UndefinedEntity
    request: SimulationRunEventRequest | None
    response: SimulationRunEventResponse | None
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SimulationRunEvent:
        return SimulationRunEvent(
            id=data["id"],
            status=SimulationRunEventStatus(data["status"]),
            event_type=EventTypeName(data["event_type"]),
            payload=NotificationEntity.from_dict_for_event_type(data["payload"], data["event_type"]),
            request=SimulationRunEventRequest.from_dict(data["request"]) if data.get("request") else None,
            response=SimulationRunEventResponse.from_dict(data["response"]) if data.get("response") else None,
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
        )
