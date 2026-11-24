from __future__ import annotations
from abc import ABC
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Entities.Entity import Entity as Entity
from paddle_billing.Entities.Events import EventTypeName as EventTypeName
from paddle_billing.Entities.Simulations import SimulationScenarioType as SimulationScenarioType
from paddle_billing.Entities.SimulationRuns import SimulationRunStatus as SimulationRunStatus
from paddle_billing.Entities.SimulationRunEvent import SimulationRunEvent as SimulationRunEvent


@dataclass
class SimulationRun(Entity, ABC):
    id: str
    status: SimulationRunStatus
    type: EventTypeName | SimulationScenarioType
    created_at: datetime
    updated_at: datetime
    events: list[SimulationRunEvent]

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SimulationRun:
        type: EventTypeName | SimulationScenarioType = EventTypeName(data["type"])
        if not type.is_known():
            type = SimulationScenarioType(data["type"])

        return SimulationRun(
            id=data["id"],
            status=SimulationRunStatus(data["status"]),
            type=type,
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
            events=[SimulationRunEvent.from_dict(event) for event in data.get("events", [])],
        )
