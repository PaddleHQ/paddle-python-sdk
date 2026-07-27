from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryAction import SubscriptionHistoryAction


@dataclass
class SubscriptionHistoryDetailSubscriptionPaymentMethodRemoved:
    action: SubscriptionHistoryAction

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionHistoryDetailSubscriptionPaymentMethodRemoved:
        return SubscriptionHistoryDetailSubscriptionPaymentMethodRemoved(
            action=SubscriptionHistoryAction(data["action"]),
        )
