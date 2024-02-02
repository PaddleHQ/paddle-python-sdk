from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Subscriptions import SubscriptionNonCatalogPrice, SubscriptionNonCatalogPriceWithProduct


@dataclass
class SubscriptionItemsWithPrice:
    price:    SubscriptionNonCatalogPrice | SubscriptionNonCatalogPriceWithProduct
    quantity: int


    @staticmethod
    def from_dict(data: dict) -> SubscriptionItemsWithPrice:
        return SubscriptionItemsWithPrice(
            price    = data['price'],
            quantity = data['quantity'],
        )
