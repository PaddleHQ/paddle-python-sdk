from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Customer import Customer

from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryAction import SubscriptionHistoryAction


@dataclass
class SubscriptionHistoryDetailSubscriptionCustomerUpdated:
    action: SubscriptionHistoryAction
    customer: Customer

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionHistoryDetailSubscriptionCustomerUpdated:
        return SubscriptionHistoryDetailSubscriptionCustomerUpdated(
            action=SubscriptionHistoryAction(data["action"]),
            customer=Customer.from_dict(data["customer"]),
        )
