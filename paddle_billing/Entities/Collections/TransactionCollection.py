from __future__ import annotations
from typing import Any

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator import Paginator
from paddle_billing.Entities.Transaction import Transaction


class TransactionCollection(Collection[Transaction]):
    @classmethod
    def from_list(cls, items_data: list[dict[str, Any]], paginator: Paginator | None = None) -> TransactionCollection:
        items: list[Transaction] = [Transaction.from_dict(item) for item in items_data]

        return TransactionCollection(items, paginator)
