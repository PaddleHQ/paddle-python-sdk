from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Shared import AdjustmentItemTotals, AdjustmentProration, AdjustmentType


@dataclass
class SubscriptionAdjustmentItem:
    item_id:   str
    type:      AdjustmentType
    amount:    str | None
    proration: AdjustmentProration
    totals:    AdjustmentItemTotals


    @staticmethod
    def from_dict(data: dict) -> SubscriptionAdjustmentItem:
        return SubscriptionAdjustmentItem(
            item_id   = data['item_id'],
            type      = AdjustmentType(data['type']),
            amount    = data.get('amount'),
            proration = AdjustmentProration.from_dict(data['proration']),
            totals    = AdjustmentItemTotals.from_dict(data['totals']),
        )
