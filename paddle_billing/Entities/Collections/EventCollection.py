from __future__ import annotations
from typing import Any

from paddle_billing.Entities.Collections.Collection import Collection as Collection
from paddle_billing.Entities.Collections.Paginator import Paginator as Paginator
from paddle_billing.Entities.Event import Event as Event


class EventCollection(Collection[Event]):
    @classmethod
    def from_list(cls, items_data: list[dict[str, Any]], paginator: Paginator | None = None) -> EventCollection:
        items: list[Event] = [Event.from_dict(item) for item in items_data]

        return EventCollection(items, paginator)
