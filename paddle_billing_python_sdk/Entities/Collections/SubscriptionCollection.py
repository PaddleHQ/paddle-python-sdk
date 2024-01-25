from __future__ import annotations

from paddle_billing_python_sdk.Entities.Collections.Collection import Collection
from paddle_billing_python_sdk.Entities.Collections.Paginator  import Paginator


class SubscriptionCollection(Collection):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator = None) -> SubscriptionCollection:
        from paddle_billing_python_sdk.Entities.Subscription import Subscription

        items = [Subscription.from_dict(item) for item in items_data]

        return SubscriptionCollection(items, paginator)


    def __next__(self):
        return super().__next__()