from __future__ import annotations

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator import Paginator
from paddle_billing.Entities.Price import Price


class PriceCollection(Collection[Price]):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator | None = None) -> PriceCollection:
        items: list[Price] = [Price.from_dict(item) for item in items_data]

        return PriceCollection(items, paginator)
