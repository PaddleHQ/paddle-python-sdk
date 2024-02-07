from __future__ import annotations

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator  import Paginator


class NotificationLogCollection(Collection):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator | None = None) -> NotificationLogCollection:
        from paddle_billing.Entities.NotificationLog import NotificationLog

        items: list[NotificationLog] = [NotificationLog.from_dict(item) for item in items_data]

        return NotificationLogCollection(items, paginator)


    def __next__(self):
        return super().__next__()
