from paddle_billing_python_sdk.Entities.Event import Event

from paddle_billing_python_sdk.Entities.Collections.Collection import Collection


class EventCollection(Collection):
    @classmethod
    def from_list(cls, items_data, paginator=None):
        items = [Event.from_dict(item) for item in items_data]
        return cls(items, paginator)


    def __next__(self):
        return super().__next__()
