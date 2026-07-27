from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Entities.Shared import TimePeriod

from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryAction import SubscriptionHistoryAction


@dataclass
class SubscriptionHistoryDetailSubscriptionRenewed:
    action: SubscriptionHistoryAction
    next_billed_at: datetime
    current_billing_period: TimePeriod
    transaction_id: str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionHistoryDetailSubscriptionRenewed:
        return SubscriptionHistoryDetailSubscriptionRenewed(
            action=SubscriptionHistoryAction(data["action"]),
            next_billed_at=datetime.fromisoformat(data["next_billed_at"]),
            current_billing_period=TimePeriod.from_dict(data["current_billing_period"]),
            transaction_id=data["transaction_id"],
        )
