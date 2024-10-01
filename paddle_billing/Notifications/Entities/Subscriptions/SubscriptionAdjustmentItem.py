from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.Notifications.Entities.Shared import AdjustmentItemTotals, AdjustmentType, Proration


@dataclass
class SubscriptionAdjustmentItem:
    item_id: str
    type: AdjustmentType
    amount: str | None
    proration: Proration
    totals: AdjustmentItemTotals

    @staticmethod
    def from_dict(data: dict) -> SubscriptionAdjustmentItem:
        return SubscriptionAdjustmentItem(
            item_id=data["item_id"],
            type=AdjustmentType(data["type"]),
            amount=data.get("amount"),
            proration=Proration.from_dict(data["proration"]),
            totals=AdjustmentItemTotals.from_dict(data["totals"]),
        )
