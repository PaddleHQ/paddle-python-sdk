from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryAction import SubscriptionHistoryAction


@dataclass
class SubscriptionHistoryDetailSubscriptionPaymentMethodAdded:
    action: SubscriptionHistoryAction

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionHistoryDetailSubscriptionPaymentMethodAdded:
        return SubscriptionHistoryDetailSubscriptionPaymentMethodAdded(
            action=SubscriptionHistoryAction(data["action"]),
        )
