from __future__ import annotations

from paddle_billing_python_sdk.Entities.Collections.Collection import Collection
from paddle_billing_python_sdk.Entities.Collections.Paginator  import Paginator


class TransactionsDataCollection(Collection):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator = None) -> TransactionsDataCollection:
        from paddle_billing_python_sdk.Entities.TransactionData import TransactionData

        items = [TransactionData.from_dict(item) for item in items_data]

        return TransactionsDataCollection(items, paginator)


    def __next__(self):
        return super().__next__()
