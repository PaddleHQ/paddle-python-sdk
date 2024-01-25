from __future__ import annotations

from paddle_billing_python_sdk.Entities.Collections.Collection import Collection
from paddle_billing_python_sdk.Entities.Collections.Paginator  import Paginator


class CreditBalanceCollection(Collection):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator = None) -> CreditBalanceCollection:
        from paddle_billing_python_sdk.Entities.CreditBalance import CreditBalance

        items = [CreditBalance.from_dict(item) for item in items_data]

        return CreditBalanceCollection(items, paginator)


    def __next__(self):
        return super().__next__()
