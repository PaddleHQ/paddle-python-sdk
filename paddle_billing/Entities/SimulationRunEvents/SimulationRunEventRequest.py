from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Entity import Entity


@dataclass
class SimulationRunEventRequest(Entity):
    body: str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SimulationRunEventRequest:
        return SimulationRunEventRequest(
            body=data["body"],
        )
