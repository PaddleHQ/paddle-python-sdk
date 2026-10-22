from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Notifications.Entities.Subscriptions.SubscriptionDiscountType import SubscriptionDiscountType


@dataclass
class SubscriptionDiscount:
    id: str
    starts_at: datetime | None
    ends_at: datetime | None
    type: SubscriptionDiscountType | None = None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionDiscount:
        return SubscriptionDiscount(
            id=data["id"],
            starts_at=datetime.fromisoformat(data["starts_at"]) if data.get("starts_at") else None,
            ends_at=datetime.fromisoformat(data["ends_at"]) if data.get("ends_at") else None,
            type=SubscriptionDiscountType(data["type"]) if data.get("type") else None,
        )
