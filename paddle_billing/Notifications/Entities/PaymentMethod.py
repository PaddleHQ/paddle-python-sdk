from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime

from paddle_billing.Notifications.Entities.Entity import Entity
from paddle_billing.Notifications.Entities.Shared import (
    Card,
    Paypal,
    CustomerPaymentMethodOrigin,
    CustomerPaymentMethodType,
)


@dataclass
class PaymentMethod(Entity):
    id: str
    customer_id: str
    address_id: str
    type: CustomerPaymentMethodType | None
    card: Card | None
    paypal: Paypal | None
    origin: CustomerPaymentMethodOrigin
    saved_at: datetime
    updated_at: datetime

    @staticmethod
    def from_dict(data: dict) -> PaymentMethod:
        return PaymentMethod(
            id=data["id"],
            customer_id=data["customer_id"],
            address_id=data["address_id"],
            type=CustomerPaymentMethodType(data["type"]),
            card=Card.from_dict(data["card"]) if data.get("card") else None,
            paypal=Paypal.from_dict(data["paypal"]) if data.get("paypal") else None,
            origin=CustomerPaymentMethodOrigin(data["origin"]),
            saved_at=datetime.fromisoformat(data["saved_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
        )
