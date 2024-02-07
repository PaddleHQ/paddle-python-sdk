from __future__ import annotations

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator  import Paginator


class PriceCollection(Collection):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator | None = None) -> PriceCollection:
        from paddle_billing.Entities.Price import Price

        items: list[Price] = [Price.from_dict(item) for item in items_data]

        return PriceCollection(items, paginator)


    def __next__(self):
        return super().__next__()
