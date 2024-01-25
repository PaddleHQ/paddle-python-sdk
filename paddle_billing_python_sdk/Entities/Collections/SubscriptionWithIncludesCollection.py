from __future__ import annotations

from paddle_billing_python_sdk.Entities.Collections.Collection import Collection
from paddle_billing_python_sdk.Entities.Collections.Paginator  import Paginator


class SubscriptionWithIncludesCollection(Collection):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator = None) -> SubscriptionWithIncludesCollection:
        from paddle_billing_python_sdk.Entities.SubscriptionWithIncludes import SubscriptionWithIncludes

        items = [SubscriptionWithIncludes.from_dict(item) for item in items_data]

        return SubscriptionWithIncludesCollection(items, paginator)


    def __next__(self):
        return super().__next__()
