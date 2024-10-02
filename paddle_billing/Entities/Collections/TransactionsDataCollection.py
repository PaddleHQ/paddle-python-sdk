from __future__ import annotations

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator import Paginator
from paddle_billing.Entities.TransactionData import TransactionData


class TransactionsDataCollection(Collection[TransactionData]):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator | None = None) -> TransactionsDataCollection:
        items: list[TransactionData] = [TransactionData.from_dict(item) for item in items_data]

        return TransactionsDataCollection(items, paginator)
