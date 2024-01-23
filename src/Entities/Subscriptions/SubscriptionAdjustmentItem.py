from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Adjustments.AdjustmentType import AdjustmentType

from src.Entities.Shared.AdjustmentItemTotals  import AdjustmentItemTotals

from src.Entities.Subscriptions.SubscriptionProration import SubscriptionProration


@dataclass
class SubscriptionAdjustmentItem:
    itemId:    str
    type:      AdjustmentType
    amount:    str | None
    proration: SubscriptionProration
    totals:    AdjustmentItemTotals


    @staticmethod
    def from_dict(data: dict) -> SubscriptionAdjustmentItem:
        return SubscriptionAdjustmentItem(
            itemId    = data['itemId'],
            type      = AdjustmentType(data['type']),
            amount    = data.get('amount'),
            proration = SubscriptionProration.from_dict(data['proration']),
            totals    = AdjustmentItemTotals.from_dict(data['totals']),
        )
