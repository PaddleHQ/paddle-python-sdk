from __future__ import annotations

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator import Paginator
from paddle_billing.Entities.Product import Product


class ProductCollection(Collection[Product]):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator | None = None) -> ProductCollection:
        items: list[Product] = [Product.from_dict(item) for item in items_data]

        return ProductCollection(items, paginator)
