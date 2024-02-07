from __future__ import annotations

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator  import Paginator


class CustomerCollection(Collection):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator | None = None) -> CustomerCollection:
        from paddle_billing.Entities.Customer import Customer

        items: list[Customer] = [Customer.from_dict(item) for item in items_data]

        return CustomerCollection(items, paginator)


    def __next__(self):
        return super().__next__()
