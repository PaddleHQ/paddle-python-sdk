from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Shared.TransactionDetailsPreview import TransactionDetailsPreview

from src.Entities.Subscriptions.SubscriptionTimePeriod        import SubscriptionTimePeriod
from src.Entities.Subscriptions.SubscriptionAdjustmentPreview import SubscriptionAdjustmentPreview


@dataclass
class SubscriptionNextTransaction:
    billingPeriod: SubscriptionTimePeriod
    details:       TransactionDetailsPreview
    adjustments:   list[SubscriptionAdjustmentPreview]


    @staticmethod
    def from_dict(data: dict) -> SubscriptionNextTransaction:
        return SubscriptionNextTransaction(
            billingPeriod = SubscriptionTimePeriod.from_dict(data['billing_period']),
            details       = TransactionDetailsPreview.from_dict(data['details']),
            adjustments   = [SubscriptionAdjustmentPreview.from_dict(adj) for adj in data.get('adjustments', [])],
        )
