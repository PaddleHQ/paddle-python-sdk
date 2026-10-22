from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryAction import SubscriptionHistoryAction
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryDiscount import SubscriptionHistoryDiscount


@dataclass
class SubscriptionHistoryDetailSubscriptionDiscountRemoved:
    action: SubscriptionHistoryAction
    discount: SubscriptionHistoryDiscount

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionHistoryDetailSubscriptionDiscountRemoved:
        return SubscriptionHistoryDetailSubscriptionDiscountRemoved(
            action=SubscriptionHistoryAction(data["action"]),
            discount=SubscriptionHistoryDiscount.from_dict(data["discount"]),
        )
