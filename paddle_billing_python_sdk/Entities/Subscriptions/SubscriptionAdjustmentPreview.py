from __future__  import annotations
from dataclasses import dataclass

from paddle_billing_python_sdk.Entities.Shared.TotalAdjustments import TotalAdjustments

from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionAdjustmentItem import SubscriptionAdjustmentItem


@dataclass
class SubscriptionAdjustmentPreview:
    transaction_id: str
    items:          list[SubscriptionAdjustmentItem]
    totals:         TotalAdjustments


    @staticmethod
    def from_dict(data: dict) -> SubscriptionAdjustmentPreview:
        return SubscriptionAdjustmentPreview(
            transaction_id = data['transaction_id'],
            items          = [SubscriptionAdjustmentItem.from_dict(item) for item in data['items']],
            totals         = TotalAdjustments.from_dict(data['totals']),
        )
