from __future__ import annotations
from typing import Any

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator import Paginator
from paddle_billing.Entities.Subscriptions.History.SubscriptionHistory import SubscriptionHistory


class SubscriptionHistoryCollection(Collection[SubscriptionHistory]):
    @classmethod
    def from_list(
        cls, items_data: list[dict[str, Any]], paginator: Paginator | None = None
    ) -> SubscriptionHistoryCollection:
        items: list[SubscriptionHistory] = [SubscriptionHistory.from_dict(item) for item in items_data]

        return SubscriptionHistoryCollection(items, paginator)
