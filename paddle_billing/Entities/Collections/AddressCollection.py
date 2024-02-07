from __future__ import annotations

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator  import Paginator


class AddressCollection(Collection):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator | None = None) -> AddressCollection:
        from paddle_billing.Entities.Address import Address

        items: list[Address] = [Address.from_dict(item) for item in items_data]

        return AddressCollection(items, paginator)


    def __next__(self):
        return super().__next__()
