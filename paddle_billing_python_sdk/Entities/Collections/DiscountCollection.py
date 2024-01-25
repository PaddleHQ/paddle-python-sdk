from __future__ import annotations

from paddle_billing_python_sdk.Entities.Collections.Collection import Collection
from paddle_billing_python_sdk.Entities.Collections.Paginator  import Paginator


class DiscountCollection(Collection):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator = None) -> DiscountCollection:
        from paddle_billing_python_sdk.Entities.Discount import Discount

        items = [Discount.from_dict(item) for item in items_data]

        return DiscountCollection(items, paginator)


    def __next__(self):
        return super().__next__()
