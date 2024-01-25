from __future__ import annotations

from paddle_billing_python_sdk.Entities.Collections.Collection import Collection
from paddle_billing_python_sdk.Entities.Collections.Paginator  import Paginator


class PriceWithIncludesCollection(Collection):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator = None) -> PriceWithIncludesCollection:
        from paddle_billing_python_sdk.Entities.PriceWithIncludes import PriceWithIncludes

        items = [PriceWithIncludes.from_dict(item) for item in items_data]

        return PriceWithIncludesCollection(items, paginator)


    def __next__(self):
        return super().__next__()
