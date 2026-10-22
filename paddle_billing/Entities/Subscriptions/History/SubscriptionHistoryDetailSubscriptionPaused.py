from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryAction import SubscriptionHistoryAction
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryPausedEffectiveFrom import (
    SubscriptionHistoryPausedEffectiveFrom,
)
from paddle_billing.Entities.Subscriptions.SubscriptionStatus import SubscriptionStatus


@dataclass
class SubscriptionHistoryDetailSubscriptionPaused:
    action: SubscriptionHistoryAction
    effective_from: SubscriptionHistoryPausedEffectiveFrom
    status: SubscriptionStatus

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionHistoryDetailSubscriptionPaused:
        return SubscriptionHistoryDetailSubscriptionPaused(
            action=SubscriptionHistoryAction(data["action"]),
            effective_from=SubscriptionHistoryPausedEffectiveFrom(data["effective_from"]),
            status=SubscriptionStatus(data["status"]),
        )
