from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Shared.TransactionDetailsPreview import TransactionDetailsPreview

from paddle_billing.Entities.Subscriptions.SubscriptionTimePeriod        import SubscriptionTimePeriod
from paddle_billing.Entities.Subscriptions.SubscriptionAdjustmentPreview import SubscriptionAdjustmentPreview


@dataclass
class SubscriptionNextTransaction:
    billing_period: SubscriptionTimePeriod
    details:        TransactionDetailsPreview
    adjustments:    list[SubscriptionAdjustmentPreview]


    @staticmethod
    def from_dict(data: dict) -> SubscriptionNextTransaction:
        return SubscriptionNextTransaction(
            billing_period = SubscriptionTimePeriod.from_dict(data['billing_period']),
            details        = TransactionDetailsPreview.from_dict(data['details']),
            adjustments    = [SubscriptionAdjustmentPreview.from_dict(adj) for adj in data.get('adjustments', [])],
        )
