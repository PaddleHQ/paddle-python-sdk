from __future__ import annotations

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator import Paginator
from paddle_billing.Entities.EventType import EventType


class EventTypeCollection(Collection[EventType]):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator | None = None) -> EventTypeCollection:
        items: list[EventType] = [EventType.from_dict(item) for item in items_data]

        return EventTypeCollection(items, paginator)
