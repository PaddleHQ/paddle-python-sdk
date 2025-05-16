from __future__ import annotations
from typing import Any

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator import Paginator
from paddle_billing.Entities.PaymentMethod import PaymentMethod


class PaymentMethodCollection(Collection[PaymentMethod]):
    @classmethod
    def from_list(cls, items_data: list[dict[str, Any]], paginator: Paginator | None = None) -> PaymentMethodCollection:
        items: list[PaymentMethod] = [PaymentMethod.from_dict(item) for item in items_data]

        return PaymentMethodCollection(items, paginator)
