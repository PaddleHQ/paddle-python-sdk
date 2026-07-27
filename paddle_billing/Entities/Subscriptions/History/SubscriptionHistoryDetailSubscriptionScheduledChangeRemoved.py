from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryAction import SubscriptionHistoryAction
from paddle_billing.Entities.Subscriptions.SubscriptionScheduledChange import SubscriptionScheduledChange


@dataclass
class SubscriptionHistoryDetailSubscriptionScheduledChangeRemoved:
    action: SubscriptionHistoryAction
    scheduled_change: SubscriptionScheduledChange

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionHistoryDetailSubscriptionScheduledChangeRemoved:
        return SubscriptionHistoryDetailSubscriptionScheduledChangeRemoved(
            action=SubscriptionHistoryAction(data["action"]),
            scheduled_change=SubscriptionScheduledChange.from_dict(data["scheduled_change"]),
        )
