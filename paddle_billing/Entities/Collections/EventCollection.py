from __future__ import annotations

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator  import Paginator


class EventCollection(Collection):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator | None = None) -> EventCollection:
        from paddle_billing.Entities.Event import Event

        items: list[Event] = [Event.from_dict(item) for item in items_data]

        return EventCollection(items, paginator)


    def __next__(self):
        return super().__next__()
