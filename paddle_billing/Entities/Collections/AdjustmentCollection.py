from __future__ import annotations

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator  import Paginator


class AdjustmentCollection(Collection):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator | None = None) -> AdjustmentCollection:
        from paddle_billing.Entities.Adjustment import Adjustment

        items: list[Adjustment] = [Adjustment.from_dict(item) for item in items_data]

        return AdjustmentCollection(items, paginator)


    def __next__(self):
        return super().__next__()
