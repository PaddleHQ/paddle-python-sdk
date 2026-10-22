from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Entities.Discount import Discount
from paddle_billing.Entities.Subscriptions.SubscriptionDiscountType import SubscriptionDiscountType


@dataclass
class SubscriptionHistoryDiscount:
    discount: Discount
    type: SubscriptionDiscountType
    starts_at: datetime
    ends_at: datetime | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionHistoryDiscount:
        return SubscriptionHistoryDiscount(
            discount=Discount.from_dict(data["discount"]),
            type=SubscriptionDiscountType(data["type"]),
            starts_at=datetime.fromisoformat(data["starts_at"]),
            ends_at=datetime.fromisoformat(data["ends_at"]) if data.get("ends_at") else None,
        )
