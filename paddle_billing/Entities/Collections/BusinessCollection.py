from __future__ import annotations

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator  import Paginator


class BusinessCollection(Collection):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator | None = None) -> BusinessCollection:
        from paddle_billing.Entities.Business import Business

        items: list[Business] = [Business.from_dict(item) for item in items_data]

        return BusinessCollection(items, paginator)


    def __next__(self):
        return super().__next__()
