from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Shared import AdjustmentTotals

from paddle_billing.Entities.Subscriptions.SubscriptionAdjustmentItem import SubscriptionAdjustmentItem


@dataclass
class SubscriptionAdjustmentPreview:
    transaction_id: str
    items:          list[SubscriptionAdjustmentItem]
    totals:         AdjustmentTotals


    @staticmethod
    def from_dict(data: dict) -> SubscriptionAdjustmentPreview:
        return SubscriptionAdjustmentPreview(
            transaction_id = data['transaction_id'],
            items          = [SubscriptionAdjustmentItem.from_dict(item) for item in data['items']],
            totals         = AdjustmentTotals.from_dict(data['totals']),
        )
