from __future__ import annotations

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator import Paginator
from paddle_billing.Entities.Event import Event


class EventCollection(Collection[Event]):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator | None = None) -> EventCollection:
        items: list[Event] = [Event.from_dict(item) for item in items_data]

        return EventCollection(items, paginator)
