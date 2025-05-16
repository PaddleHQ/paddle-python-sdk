from __future__ import annotations
from typing import Any

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator import Paginator
from paddle_billing.Entities.SubscriptionPreview import SubscriptionPreview


class SubscriptionPreviewCollection(Collection[SubscriptionPreview]):
    @classmethod
    def from_list(cls, items_data: list[Any], paginator: Paginator | None = None) -> SubscriptionPreviewCollection:
        items: list[SubscriptionPreview] = [SubscriptionPreview.from_dict(item) for item in items_data]

        return SubscriptionPreviewCollection(items, paginator)
