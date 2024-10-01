from __future__ import annotations

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator import Paginator
from paddle_billing.Entities.SubscriptionPreview import SubscriptionPreview


class SubscriptionPreviewCollection(Collection[SubscriptionPreview]):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator | None = None) -> SubscriptionPreviewCollection:
        items: list[SubscriptionPreview] = [SubscriptionPreview.from_dict(item) for item in items_data]

        return SubscriptionPreviewCollection(items, paginator)
