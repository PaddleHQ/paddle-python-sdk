from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Subscriptions.SubscriptionNonCatalogPrice            import SubscriptionNonCatalogPrice
from paddle_billing.Entities.Subscriptions.SubscriptionNonCatalogPriceWithProduct import SubscriptionNonCatalogPriceWithProduct


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
