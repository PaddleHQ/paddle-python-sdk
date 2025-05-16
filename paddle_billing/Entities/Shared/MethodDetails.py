from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Shared.Card import Card
from paddle_billing.Entities.Shared.PaymentMethodType import PaymentMethodType


@dataclass
class MethodDetails:
    type: PaymentMethodType
    card: Card | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> MethodDetails:
        return MethodDetails(
            PaymentMethodType(data["type"]),
            Card.from_dict(data["card"]) if data.get("card") else None,
        )
