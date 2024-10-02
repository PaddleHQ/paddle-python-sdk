from __future__ import annotations

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator import Paginator
from paddle_billing.Entities.Subscription import Subscription


class SubscriptionCollection(Collection[Subscription]):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator | None = None) -> SubscriptionCollection:
        items: list[Subscription] = [Subscription.from_dict(item) for item in items_data]

        return SubscriptionCollection(items, paginator)
