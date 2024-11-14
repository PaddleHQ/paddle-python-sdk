from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Shared import (
    Card,
    Paypal,
    SavedPaymentMethodOrigin,
    SavedPaymentMethodType,
)


@dataclass
class PaymentMethod(Entity):
    id: str
    customer_id: str
    address_id: str
    type: SavedPaymentMethodType | None
    card: Card | None
    paypal: Paypal | None
    origin: SavedPaymentMethodOrigin
    saved_at: datetime
    updated_at: datetime

    @staticmethod
    def from_dict(data: dict) -> PaymentMethod:
        return PaymentMethod(
            id=data["id"],
            customer_id=data["customer_id"],
            address_id=data["address_id"],
            type=SavedPaymentMethodType(data["type"]),
            card=Card.from_dict(data["card"]) if data.get("card") else None,
            paypal=Paypal.from_dict(data["paypal"]) if data.get("paypal") else None,
            origin=SavedPaymentMethodOrigin(data["origin"]),
            saved_at=datetime.fromisoformat(data["saved_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
        )
