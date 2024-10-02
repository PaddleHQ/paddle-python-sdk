from __future__ import annotations

from paddle_billing.Entities.Adjustment import Adjustment
from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator import Paginator


class AdjustmentCollection(Collection[Adjustment]):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator | None = None) -> AdjustmentCollection:
        items: list[Adjustment] = [Adjustment.from_dict(item) for item in items_data]

        return AdjustmentCollection(items, paginator)
