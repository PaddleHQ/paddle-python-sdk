from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryAction import SubscriptionHistoryAction
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryCanceledEffectiveFrom import (
    SubscriptionHistoryCanceledEffectiveFrom,
)


@dataclass
class SubscriptionHistoryDetailSubscriptionCanceled:
    action: SubscriptionHistoryAction
    effective_from: SubscriptionHistoryCanceledEffectiveFrom | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionHistoryDetailSubscriptionCanceled:
        return SubscriptionHistoryDetailSubscriptionCanceled(
            action=SubscriptionHistoryAction(data["action"]),
            effective_from=(
                SubscriptionHistoryCanceledEffectiveFrom(data["effective_from"]) if data.get("effective_from") else None
            ),
        )
