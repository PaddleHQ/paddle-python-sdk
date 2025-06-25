from __future__ import annotations
from typing import Any

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator import Paginator
from paddle_billing.Entities.Discount import Discount


class DiscountCollection(Collection[Discount]):
    @classmethod
    def from_list(cls, items_data: list[dict[str, Any]], paginator: Paginator | None = None) -> DiscountCollection:
        items: list[Discount] = [Discount.from_dict(item) for item in items_data]

        return DiscountCollection(items, paginator)
