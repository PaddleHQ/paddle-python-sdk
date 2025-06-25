from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.Resources.Subscriptions.Operations.Price import (
    SubscriptionNonCatalogPrice,
    SubscriptionNonCatalogPriceWithProduct,
)


@dataclass
class SubscriptionUpdateItemWithPrice:
    price: SubscriptionNonCatalogPrice | SubscriptionNonCatalogPriceWithProduct
    quantity: int
