from __future__ import annotations

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator  import Paginator


class TransactionPreviewCollection(Collection):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator | None = None) -> TransactionPreviewCollection:
        from paddle_billing.Entities.TransactionPreview import TransactionPreview

        items: list[TransactionPreview] = [TransactionPreview.from_dict(item) for item in items_data]

        return TransactionPreviewCollection(items, paginator)


    def __next__(self):
        return super().__next__()
