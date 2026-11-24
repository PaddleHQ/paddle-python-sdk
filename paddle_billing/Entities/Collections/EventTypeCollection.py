from __future__ import annotations
from typing import Any

from paddle_billing.Entities.Collections.Collection import Collection as Collection
from paddle_billing.Entities.Collections.Paginator import Paginator as Paginator
from paddle_billing.Entities.EventType import EventType as EventType


class EventTypeCollection(Collection[EventType]):
    @classmethod
    def from_list(cls, items_data: list[dict[str, Any]], paginator: Paginator | None = None) -> EventTypeCollection:
        items: list[EventType] = [EventType.from_dict(item) for item in items_data]

        return EventTypeCollection(items, paginator)
