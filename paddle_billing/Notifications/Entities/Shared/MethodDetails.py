from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Notifications.Entities.Shared.Card import Card
from paddle_billing.Notifications.Entities.Shared.PaymentMethodType import PaymentMethodType
from paddle_billing.Notifications.Entities.Shared.PaymentMethodUnderlyingDetails import PaymentMethodUnderlyingDetails
from paddle_billing.Notifications.Entities.Shared.SouthKoreaLocalCard import SouthKoreaLocalCard


@dataclass
class MethodDetails:
    type: PaymentMethodType
    card: Card | None
    underlying_details: PaymentMethodUnderlyingDetails | None  # deprecated
    south_korea_local_card: SouthKoreaLocalCard | None

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
            (
                SouthKoreaLocalCard.from_dict(data["south_korea_local_card"])
                if data.get("south_korea_local_card")
                else None
            ),
        )
