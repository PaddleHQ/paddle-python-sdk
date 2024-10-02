from __future__ import annotations

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator import Paginator
from paddle_billing.Entities.Notification import Notification


class NotificationCollection(Collection[Notification]):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator | None = None) -> NotificationCollection:
        items: list[Notification] = [Notification.from_dict(item) for item in items_data]

        return NotificationCollection(items, paginator)
