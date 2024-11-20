from __future__ import annotations
from abc import ABC
from dataclasses import dataclass

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Events import EventTypeName
from paddle_billing.Entities.Simulations import SimulationKind


@dataclass
class SimulationType(Entity, ABC):
    name: str
    label: str
    description: str
    group: str
    type: SimulationKind
    events: list[EventTypeName]

    @staticmethod
    def from_dict(data: dict) -> SimulationType:
        return SimulationType(
            name=data["name"],
            label=data["label"],
            description=data["description"],
            group=data["group"],
            type=SimulationKind(data["type"]),
            events=[EventTypeName(event) for event in data.get("events", [])],
        )
