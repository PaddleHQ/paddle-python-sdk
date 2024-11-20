from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Entity import Entity


@dataclass
class SimulationRunEventRequest(Entity):
    body: str

    @staticmethod
    def from_dict(data: dict) -> SimulationRunEventRequest:
        return SimulationRunEventRequest(
            body=data["body"],
        )
