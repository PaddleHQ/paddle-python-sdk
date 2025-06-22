from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Shared.Card import Card
from paddle_billing.Entities.Shared.PaymentMethodType import PaymentMethodType
from paddle_billing.Entities.Shared.PaymentMethodUnderlyingDetails import PaymentMethodUnderlyingDetails


@dataclass
class MethodDetails:
    type: PaymentMethodType
    card: Card | None
    underlying_details: PaymentMethodUnderlyingDetails | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> MethodDetails:
        return MethodDetails(
            PaymentMethodType(data["type"]),
            Card.from_dict(data["card"]) if data.get("card") else None,
            (
                PaymentMethodUnderlyingDetails.from_dict(data["underlying_details"])
                if data.get("underlying_details")
                else None
            ),
        )
