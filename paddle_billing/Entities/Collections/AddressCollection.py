from __future__ import annotations
from typing import Any

from paddle_billing.Entities.Address import Address as Address
from paddle_billing.Entities.Collections.Collection import Collection as Collection
from paddle_billing.Entities.Collections.Paginator import Paginator as Paginator


class AddressCollection(Collection[Address]):
    @classmethod
    def from_list(cls, items_data: list[dict[str, Any]], paginator: Paginator | None = None) -> AddressCollection:
        items: list[Address] = [Address.from_dict(item) for item in items_data]

        return AddressCollection(items, paginator)
