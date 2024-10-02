from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime

from paddle_billing.Notifications.Entities.Shared.TimePeriod import TimePeriod

from paddle_billing.Notifications.Entities.Product import Product
from paddle_billing.Notifications.Entities.Subscriptions.SubscriptionItemStatus import SubscriptionItemStatus
from paddle_billing.Notifications.Entities.Subscriptions.SubscriptionPrice import SubscriptionPrice


@dataclass
class SubscriptionItem:
    status: SubscriptionItemStatus
    quantity: int
    recurring: bool
    created_at: datetime
    updated_at: datetime
    previously_billed_at: datetime | None
    next_billed_at: datetime | None
    trial_dates: TimePeriod | None
    price: SubscriptionPrice
    product: Product | None

    @staticmethod
    def from_dict(data: dict) -> SubscriptionItem:
        return SubscriptionItem(
            status=SubscriptionItemStatus(data["status"]),
            quantity=data["quantity"],
            recurring=data["recurring"],
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
            price=SubscriptionPrice.from_dict(data["price"]),
            previously_billed_at=(
                datetime.fromisoformat(data["previously_billed_at"]) if data.get("previously_billed_at") else None
            ),
            next_billed_at=datetime.fromisoformat(data["next_billed_at"]) if data.get("next_billed_at") else None,
            trial_dates=TimePeriod.from_dict(data["trial_dates"]) if data.get("trial_dates") else None,
            product=Product.from_dict(data["product"]) if data.get("product") else None,
        )
