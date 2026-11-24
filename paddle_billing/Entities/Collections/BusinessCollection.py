from __future__ import annotations
from typing import Any

from paddle_billing.Entities.Business import Business as Business
from paddle_billing.Entities.Collections.Collection import Collection as Collection
from paddle_billing.Entities.Collections.Paginator import Paginator as Paginator


class BusinessCollection(Collection[Business]):
    @classmethod
    def from_list(cls, items_data: list[dict[str, Any]], paginator: Paginator | None = None) -> BusinessCollection:

        items: list[Business] = [Business.from_dict(item) for item in items_data]

        return BusinessCollection(items, paginator)
