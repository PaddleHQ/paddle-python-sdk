from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Notifications.Entities.Entity import Entity
from paddle_billing.Notifications.Entities.Shared import (
    SavedPaymentMethodOrigin,
    SavedPaymentMethodType,
)


@dataclass
class PaymentMethod(Entity):
    id: str
    customer_id: str
    address_id: str
    type: SavedPaymentMethodType
    origin: SavedPaymentMethodOrigin
    saved_at: datetime
    updated_at: datetime

    @staticmethod
    def from_dict(data: dict[str, Any]) -> PaymentMethod:
        return PaymentMethod(
            id=data["id"],
            customer_id=data["customer_id"],
            address_id=data["address_id"],
            type=SavedPaymentMethodType(data["type"]),
            origin=SavedPaymentMethodOrigin(data["origin"]),
            saved_at=datetime.fromisoformat(data["saved_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
        )
