from __future__ import annotations
from typing import Any

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator import Paginator
from paddle_billing.Entities.Customer import Customer


class CustomerCollection(Collection[Customer]):
    @classmethod
    def from_list(cls, items_data: list[dict[str, Any]], paginator: Paginator | None = None) -> CustomerCollection:
        items: list[Customer] = [Customer.from_dict(item) for item in items_data]

        return CustomerCollection(items, paginator)
