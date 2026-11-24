from __future__ import annotations
from typing import Any

from paddle_billing.Entities.Collections.Collection import Collection as Collection
from paddle_billing.Entities.Collections.Paginator import Paginator as Paginator
from paddle_billing.Entities.Notification import Notification as Notification


class NotificationCollection(Collection[Notification]):
    @classmethod
    def from_list(cls, items_data: list[dict[str, Any]], paginator: Paginator | None = None) -> NotificationCollection:
        items: list[Notification] = [Notification.from_dict(item) for item in items_data]

        return NotificationCollection(items, paginator)
