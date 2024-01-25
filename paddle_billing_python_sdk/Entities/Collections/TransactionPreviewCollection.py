from __future__ import annotations

from paddle_billing_python_sdk.Entities.Collections.Collection import Collection
from paddle_billing_python_sdk.Entities.Collections.Paginator  import Paginator


class TransactionPreviewCollection(Collection):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator = None) -> TransactionPreviewCollection:
        from paddle_billing_python_sdk.Entities.TransactionPreview import TransactionPreview

        items = [TransactionPreview.from_dict(item) for item in items_data]

        return TransactionPreviewCollection(items, paginator)


    def __next__(self):
        return super().__next__()
