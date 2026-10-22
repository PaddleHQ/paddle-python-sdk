from __future__ import annotations
from typing import Any

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator import Paginator
from paddle_billing.Entities.CheckoutDomain import CheckoutDomain


class CheckoutDomainCollection(Collection[CheckoutDomain]):
    @classmethod
    def from_list(
        cls, items_data: list[dict[str, Any]], paginator: Paginator | None = None
    ) -> CheckoutDomainCollection:
        items: list[CheckoutDomain] = [CheckoutDomain.from_dict(item) for item in items_data]

        return CheckoutDomainCollection(items, paginator)
