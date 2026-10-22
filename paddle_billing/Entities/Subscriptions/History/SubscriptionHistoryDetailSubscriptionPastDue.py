from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryAction import SubscriptionHistoryAction
from paddle_billing.Entities.Subscriptions.SubscriptionStatus import SubscriptionStatus


@dataclass
class SubscriptionHistoryDetailSubscriptionPastDue:
    action: SubscriptionHistoryAction
    status: SubscriptionStatus
    transaction_id: str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionHistoryDetailSubscriptionPastDue:
        return SubscriptionHistoryDetailSubscriptionPastDue(
            action=SubscriptionHistoryAction(data["action"]),
            status=SubscriptionStatus(data["status"]),
            transaction_id=data["transaction_id"],
        )
