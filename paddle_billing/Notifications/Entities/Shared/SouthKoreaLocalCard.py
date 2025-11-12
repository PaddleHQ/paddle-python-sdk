from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Notifications.Entities.Shared.SouthKoreaLocalCardType import SouthKoreaLocalCardType


@dataclass
class SouthKoreaLocalCard:
    type: SouthKoreaLocalCardType
    last4: str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SouthKoreaLocalCard:
        return SouthKoreaLocalCard(
            type=SouthKoreaLocalCardType(data["type"]),
            last4=data["last4"],
        )
