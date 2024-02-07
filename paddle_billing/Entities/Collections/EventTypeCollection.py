from __future__ import annotations

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator  import Paginator


class EventTypeCollection(Collection):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator | None = None) -> EventTypeCollection:
        from paddle_billing.Entities.EventType import EventType

        items: list[EventType] = [EventType.from_dict(item) for item in items_data]

        return EventTypeCollection(items, paginator)


    def __next__(self):
        return super().__next__()
