from __future__ import annotations

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator import Paginator
from paddle_billing.Entities.NotificationSetting import NotificationSetting


class NotificationSettingCollection(Collection[NotificationSetting]):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator | None = None) -> NotificationSettingCollection:
        items: list[NotificationSetting] = [NotificationSetting.from_dict(item) for item in items_data]

        return NotificationSettingCollection(items, paginator)
