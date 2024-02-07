from __future__ import annotations

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator  import Paginator


class DiscountCollection(Collection):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator | None = None) -> DiscountCollection:
        from paddle_billing.Entities.Discount import Discount

        items: list[Discount] = [Discount.from_dict(item) for item in items_data]

        return DiscountCollection(items, paginator)


    def __next__(self):
        return super().__next__()
