from __future__ import annotations
from abc import ABC
from dataclasses import dataclass
from datetime import datetime

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Events import EventTypeName
from paddle_billing.Entities.Simulations import SimulationScenarioType, SimulationStatus

from paddle_billing.Notifications.Entities.Entity import Entity as NotificationEntity
from paddle_billing.Notifications.Entities.UndefinedEntity import UndefinedEntity


@dataclass
class Simulation(Entity, ABC):
    id: str
    status: SimulationStatus
    notification_setting_id: str
    name: str
    type: EventTypeName | SimulationScenarioType
    payload: NotificationEntity | UndefinedEntity | None
    last_run_at: datetime | None
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def from_dict(data: dict) -> Simulation:
        type = EventTypeName(data["type"])
        if not type.is_known():
            type = SimulationScenarioType(data["type"])

        return Simulation(
            id=data["id"],
            status=SimulationStatus(data["status"]),
            notification_setting_id=data["notification_setting_id"],
            name=data["name"],
            type=type,
            payload=(
                NotificationEntity.from_dict_for_event_type(data["payload"], type.value)
                if isinstance(type, EventTypeName) and data.get("payload")
                else None
            ),
            last_run_at=datetime.fromisoformat(data["last_run_at"]) if data.get("last_run_at") else None,
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
        )
