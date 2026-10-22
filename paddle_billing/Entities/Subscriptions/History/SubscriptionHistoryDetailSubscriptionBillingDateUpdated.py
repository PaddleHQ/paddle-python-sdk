from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Entities.Shared import TimePeriod

from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryAction import SubscriptionHistoryAction
from paddle_billing.Entities.Subscriptions.SubscriptionProrationBillingMode import SubscriptionProrationBillingMode


@dataclass
class SubscriptionHistoryDetailSubscriptionBillingDateUpdated:
    action: SubscriptionHistoryAction
    next_billed_at: datetime | None
    current_billing_period: TimePeriod
    transaction_id: str | None
    proration_billing_mode: SubscriptionProrationBillingMode

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionHistoryDetailSubscriptionBillingDateUpdated:
        return SubscriptionHistoryDetailSubscriptionBillingDateUpdated(
            action=SubscriptionHistoryAction(data["action"]),
            next_billed_at=datetime.fromisoformat(data["next_billed_at"]) if data.get("next_billed_at") else None,
            current_billing_period=TimePeriod.from_dict(data["current_billing_period"]),
            transaction_id=data.get("transaction_id"),
            proration_billing_mode=SubscriptionProrationBillingMode(data["proration_billing_mode"]),
        )
