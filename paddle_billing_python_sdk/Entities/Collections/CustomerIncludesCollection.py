from __future__ import annotations

from paddle_billing_python_sdk.Entities.Collections.Collection import Collection
from paddle_billing_python_sdk.Entities.Collections.Paginator  import Paginator


class CustomerIncludesCollection(Collection):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator = None) -> CustomerIncludesCollection:
        from paddle_billing_python_sdk.Entities.CustomerIncludes import CustomerIncludes

        items = [CustomerIncludes.from_dict(item) for item in items_data]

        return CustomerIncludesCollection(items, paginator)


    def __next__(self):
        return super().__next__()
