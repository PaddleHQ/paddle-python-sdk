from __future__ import annotations

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator  import Paginator


class SubscriptionsTransactionCollection(Collection):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator | None = None) -> SubscriptionsTransactionCollection:
        from paddle_billing.Entities.SubscriptionTransaction import SubscriptionTransaction

        items: list[SubscriptionTransaction] = [SubscriptionTransaction.from_dict(item) for item in items_data]

        return SubscriptionsTransactionCollection(items, paginator)


    def __next__(self):
        return super().__next__()
