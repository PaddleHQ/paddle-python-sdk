from __future__ import annotations

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator import Paginator
from paddle_billing.Entities.CreditBalance import CreditBalance


class CreditBalanceCollection(Collection[CreditBalance]):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator | None = None) -> CreditBalanceCollection:
        items: list[CreditBalance] = [CreditBalance.from_dict(item) for item in items_data]

        return CreditBalanceCollection(items, paginator)
