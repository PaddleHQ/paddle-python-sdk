from __future__ import annotations
from typing import Any

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator import Paginator
from paddle_billing.Entities.DiscountGroup import DiscountGroup


class DiscountGroupCollection(Collection[DiscountGroup]):
    @classmethod
    def from_list(cls, items_data: list[dict[str, Any]], paginator: Paginator | None = None) -> DiscountGroupCollection:
        items: list[DiscountGroup] = [DiscountGroup.from_dict(item) for item in items_data]

        return DiscountGroupCollection(items, paginator)
