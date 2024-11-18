from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Entity import Entity


@dataclass
class SimulationRunEventResponse(Entity):
    body: str
    status_code: int

    @staticmethod
    def from_dict(data: dict) -> SimulationRunEventResponse:
        return SimulationRunEventResponse(
            body=data["body"],
            status_code=data["status_code"],
        )
