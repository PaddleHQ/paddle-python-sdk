from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Shared import BillingDetails

from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryAction import SubscriptionHistoryAction


@dataclass
class SubscriptionHistoryDetailSubscriptionBillingDetailsUpdated:
    action: SubscriptionHistoryAction
    billing_details: BillingDetails

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionHistoryDetailSubscriptionBillingDetailsUpdated:
        return SubscriptionHistoryDetailSubscriptionBillingDetailsUpdated(
            action=SubscriptionHistoryAction(data["action"]),
            billing_details=BillingDetails.from_dict(data["billing_details"]),
        )
