from __future__ import annotations
from typing import Any

from paddle_billing.Entities.Collections.Collection import Collection as Collection
from paddle_billing.Entities.Collections.Paginator import Paginator as Paginator
from paddle_billing.Entities.ClientToken import ClientToken as ClientToken


class ClientTokenCollection(Collection[ClientToken]):
    @classmethod
    def from_list(cls, items_data: list[dict[str, Any]], paginator: Paginator | None = None) -> ClientTokenCollection:
        items: list[ClientToken] = [ClientToken.from_dict(item) for item in items_data]

        return ClientTokenCollection(items, paginator)
