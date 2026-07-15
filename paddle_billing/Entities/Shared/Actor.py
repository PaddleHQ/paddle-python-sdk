from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Shared.ActorType import ActorType


@dataclass
class Actor:
    type: ActorType
    id: str | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> Actor:
        return Actor(
            type=ActorType(data["type"]),
            id=data.get("id"),
        )
