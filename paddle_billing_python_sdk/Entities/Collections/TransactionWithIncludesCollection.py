from __future__ import annotations

from paddle_billing_python_sdk.Entities.Collections.Collection import Collection
from paddle_billing_python_sdk.Entities.Collections.Paginator  import Paginator


class TransactionWithIncludesCollection(Collection):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator = None) -> TransactionWithIncludesCollection:
        from paddle_billing_python_sdk.Entities.TransactionWithIncludes import TransactionWithIncludes

        items = [TransactionWithIncludes.from_dict(item) for item in items_data]

        return TransactionWithIncludesCollection(items, paginator)


    def __next__(self):
        return super().__next__()
