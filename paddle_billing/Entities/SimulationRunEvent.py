from __future__ import annotations
from abc import ABC
from dataclasses import dataclass
from datetime import datetime

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Events import EventTypeName
from paddle_billing.Entities.SimulationRunEvents import (
    SimulationRunEventStatus,
    SimulationRunEventRequest,
    SimulationRunEventResponse,
)

from paddle_billing.Notifications.Entities.Entity import Entity as NotificationEntity
from paddle_billing.Notifications.Entities.UndefinedEntity import UndefinedEntity


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
    def from_dict(data: dict) -> SimulationRunEvent:
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
