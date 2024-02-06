from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Subscriptions.SubscriptionCharge import SubscriptionCharge
from paddle_billing.Entities.Subscriptions.SubscriptionCredit import SubscriptionCredit
from paddle_billing.Entities.Subscriptions.SubscriptionResult import SubscriptionResult


@dataclass
class SubscriptionPreviewSubscriptionUpdateSummary:
    credit: SubscriptionCredit
    charge: SubscriptionCharge
    result: SubscriptionResult


    @staticmethod
    def from_dict(data: dict) -> SubscriptionPreviewSubscriptionUpdateSummary:
        return SubscriptionPreviewSubscriptionUpdateSummary(
            credit = SubscriptionCredit.from_dict(data['credit']),
            charge = SubscriptionCharge.from_dict(data['charge']),
            result = SubscriptionResult.from_dict(data['result']),
        )
