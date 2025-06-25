from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Shared import (
    Card,
    PaymentMethodUnderlyingDetails,
    Paypal,
    SavedPaymentMethodOrigin,
    SavedPaymentMethodType,
)


@dataclass
class PaymentMethod(Entity):
    id: str
    customer_id: str
    address_id: str
    type: SavedPaymentMethodType
    card: Card | None
    paypal: Paypal | None
    origin: SavedPaymentMethodOrigin
    saved_at: datetime
    updated_at: datetime
    underlying_details: PaymentMethodUnderlyingDetails | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> PaymentMethod:
        return PaymentMethod(
            id=data["id"],
            customer_id=data["customer_id"],
            address_id=data["address_id"],
            type=SavedPaymentMethodType(data["type"]),
            card=Card.from_dict(data["card"]) if data.get("card") else None,
            paypal=Paypal.from_dict(data["paypal"]) if data.get("paypal") else None,
            underlying_details=(
                PaymentMethodUnderlyingDetails.from_dict(data["underlying_details"])
                if data.get("underlying_details")
                else None
            ),
            origin=SavedPaymentMethodOrigin(data["origin"]),
            saved_at=datetime.fromisoformat(data["saved_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
        )
