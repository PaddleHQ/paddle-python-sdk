from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.Resources.Subscriptions.Operations.Price import (
    SubscriptionNonCatalogPrice as SubscriptionNonCatalogPrice,
    SubscriptionNonCatalogPriceWithProduct as SubscriptionNonCatalogPriceWithProduct,
)


@dataclass
class SubscriptionChargeItemWithPrice:
    price: SubscriptionNonCatalogPrice | SubscriptionNonCatalogPriceWithProduct
    quantity: int
