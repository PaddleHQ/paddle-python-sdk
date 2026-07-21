from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Shared import CollectionMode

from paddle_billing.Entities.Subscriptions.History.SubscriptionHistoryAction import SubscriptionHistoryAction


@dataclass
class SubscriptionHistoryDetailSubscriptionCollectionModeUpdated:
    action: SubscriptionHistoryAction
    collection_mode: CollectionMode

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SubscriptionHistoryDetailSubscriptionCollectionModeUpdated:
        return SubscriptionHistoryDetailSubscriptionCollectionModeUpdated(
            action=SubscriptionHistoryAction(data["action"]),
            collection_mode=CollectionMode(data["collection_mode"]),
        )
