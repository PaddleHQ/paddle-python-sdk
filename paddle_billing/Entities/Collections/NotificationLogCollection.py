from __future__ import annotations

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator import Paginator
from paddle_billing.Entities.NotificationLog import NotificationLog


class NotificationLogCollection(Collection[NotificationLog]):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator | None = None) -> NotificationLogCollection:
        items: list[NotificationLog] = [NotificationLog.from_dict(item) for item in items_data]

        return NotificationLogCollection(items, paginator)
