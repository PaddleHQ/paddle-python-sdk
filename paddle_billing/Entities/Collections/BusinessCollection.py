from __future__ import annotations

from paddle_billing.Entities.Business import Business
from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator import Paginator


class BusinessCollection(Collection[Business]):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator | None = None) -> BusinessCollection:

        items: list[Business] = [Business.from_dict(item) for item in items_data]

        return BusinessCollection(items, paginator)
