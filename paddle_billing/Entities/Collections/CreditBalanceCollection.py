from __future__ import annotations

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator  import Paginator


class CreditBalanceCollection(Collection):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator | None = None) -> CreditBalanceCollection:
        from paddle_billing.Entities.CreditBalance import CreditBalance

        items: list[CreditBalance] = [CreditBalance.from_dict(item) for item in items_data]

        return CreditBalanceCollection(items, paginator)


    def __next__(self):
        return super().__next__()
