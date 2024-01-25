from __future__ import annotations

from paddle_billing_python_sdk.Entities.Collections.Collection import Collection
from paddle_billing_python_sdk.Entities.Collections.Paginator  import Paginator


class TransactionCollection(Collection):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator = None) -> TransactionCollection:
        from paddle_billing_python_sdk.Entities.Transaction import Transaction

        items = [Transaction.from_dict(item) for item in items_data]

        return TransactionCollection(items, paginator)


    def __next__(self):
        return super().__next__()