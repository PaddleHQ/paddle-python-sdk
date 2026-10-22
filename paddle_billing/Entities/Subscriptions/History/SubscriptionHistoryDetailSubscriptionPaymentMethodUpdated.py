from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryAction import SubscriptionHistoryAction


@dataclass
class SubscriptionHistoryDetailSubscriptionPaymentMethodUpdated:
    action: SubscriptionHistoryAction

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionHistoryDetailSubscriptionPaymentMethodUpdated:
        return SubscriptionHistoryDetailSubscriptionPaymentMethodUpdated(
            action=SubscriptionHistoryAction(data["action"]),
        )
