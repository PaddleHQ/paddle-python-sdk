from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Shared import CustomData

from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryAction import SubscriptionHistoryAction


@dataclass
class SubscriptionHistoryDetailSubscriptionCustomDataUpdated:
    action: SubscriptionHistoryAction
    custom_data: CustomData | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionHistoryDetailSubscriptionCustomDataUpdated:
        return SubscriptionHistoryDetailSubscriptionCustomDataUpdated(
            action=SubscriptionHistoryAction(data["action"]),
            custom_data=CustomData(data["custom_data"]) if data.get("custom_data") else None,
        )
