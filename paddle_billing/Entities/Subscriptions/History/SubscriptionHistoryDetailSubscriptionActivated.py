from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Entities.Shared.TimePeriod import TimePeriod

from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryAction import SubscriptionHistoryAction
from paddle_billing.Entities.Subscriptions.SubscriptionStatus import SubscriptionStatus


@dataclass
class SubscriptionHistoryDetailSubscriptionActivated:
    action: SubscriptionHistoryAction
    status: SubscriptionStatus
    first_billed_at: datetime | None
    next_billed_at: datetime | None
    current_billing_period: TimePeriod
    transaction_id: str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionHistoryDetailSubscriptionActivated:
        return SubscriptionHistoryDetailSubscriptionActivated(
            action=SubscriptionHistoryAction(data["action"]),
            status=SubscriptionStatus(data["status"]),
            first_billed_at=datetime.fromisoformat(data["first_billed_at"]) if data.get("first_billed_at") else None,
            next_billed_at=datetime.fromisoformat(data["next_billed_at"]) if data.get("next_billed_at") else None,
            current_billing_period=TimePeriod.from_dict(data["current_billing_period"]),
            transaction_id=data["transaction_id"],
        )
