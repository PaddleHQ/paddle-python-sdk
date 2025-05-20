from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Notifications.Entities.Entity import Entity
from paddle_billing.Notifications.Entities.Shared import (
    SavedPaymentMethodDeletionReason,
    SavedPaymentMethodOrigin,
    SavedPaymentMethodType,
)


@dataclass
class PaymentMethodDeleted(Entity):
    id: str
    customer_id: str
    address_id: str
    type: SavedPaymentMethodType
    origin: SavedPaymentMethodOrigin
    saved_at: datetime
    updated_at: datetime
    deletion_reason: SavedPaymentMethodDeletionReason

    @staticmethod
    def from_dict(data: dict[str, Any]) -> PaymentMethodDeleted:
        return PaymentMethodDeleted(
            id=data["id"],
            customer_id=data["customer_id"],
            address_id=data["address_id"],
            type=SavedPaymentMethodType(data["type"]),
            origin=SavedPaymentMethodOrigin(data["origin"]),
            saved_at=datetime.fromisoformat(data["saved_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
            deletion_reason=SavedPaymentMethodDeletionReason(data["deletion_reason"]),
        )
