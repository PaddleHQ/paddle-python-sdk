from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Business import Business

from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryAction import SubscriptionHistoryAction


@dataclass
class SubscriptionHistoryDetailSubscriptionBusinessAdded:
    action: SubscriptionHistoryAction
    business: Business

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionHistoryDetailSubscriptionBusinessAdded:
        return SubscriptionHistoryDetailSubscriptionBusinessAdded(
            action=SubscriptionHistoryAction(data["action"]),
            business=Business.from_dict(data["business"]),
        )
