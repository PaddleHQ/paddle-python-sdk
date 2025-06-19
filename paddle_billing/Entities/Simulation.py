from __future__ import annotations
from abc import ABC
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Events import EventTypeName
from paddle_billing.Entities.Simulations import SimulationScenarioType, SimulationStatus

from paddle_billing.Entities.Simulations.Config import SimulationConfig
from paddle_billing.Notifications.Entities.Simulations.SimulationEntity import SimulationEntity
from paddle_billing.Notifications.Entities.UndefinedEntity import UndefinedEntity


@dataclass
class Simulation(Entity, ABC):
    id: str
    status: SimulationStatus
    notification_setting_id: str
    name: str
    type: EventTypeName | SimulationScenarioType
    payload: SimulationEntity | UndefinedEntity | None
    last_run_at: datetime | None
    created_at: datetime
    updated_at: datetime
    config: SimulationConfig | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> Simulation:
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
                SimulationEntity.from_dict_for_event_type(data["payload"], type.value)
                if isinstance(type, EventTypeName) and data.get("payload")
                else None
            ),
            last_run_at=datetime.fromisoformat(data["last_run_at"]) if data.get("last_run_at") else None,
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
            config=(SimulationConfig.from_dict(data["config"]) if data.get("config") else None),
        )
