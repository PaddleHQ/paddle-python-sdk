from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Entities.Shared import Duration, TimePeriod

from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryAction import SubscriptionHistoryAction


@dataclass
class SubscriptionHistoryDetailSubscriptionBillingCycleUpdated:
    action: SubscriptionHistoryAction
    billing_cycle: Duration
    current_billing_period: TimePeriod
    next_billed_at: datetime | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionHistoryDetailSubscriptionBillingCycleUpdated:
        return SubscriptionHistoryDetailSubscriptionBillingCycleUpdated(
            action=SubscriptionHistoryAction(data["action"]),
            billing_cycle=Duration.from_dict(data["billing_cycle"]),
            current_billing_period=TimePeriod.from_dict(data["current_billing_period"]),
            next_billed_at=datetime.fromisoformat(data["next_billed_at"]) if data.get("next_billed_at") else None,
        )
