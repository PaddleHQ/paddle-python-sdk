from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Business import Business

from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryAction import SubscriptionHistoryAction


@dataclass
class SubscriptionHistoryDetailSubscriptionBusinessRemoved:
    action: SubscriptionHistoryAction
    business: Business

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionHistoryDetailSubscriptionBusinessRemoved:
        return SubscriptionHistoryDetailSubscriptionBusinessRemoved(
            action=SubscriptionHistoryAction(data["action"]),
            business=Business.from_dict(data["business"]),
        )
