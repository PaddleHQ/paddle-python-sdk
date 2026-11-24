from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.Resources.Transactions.Operations.Price.TransactionNonCatalogPrice import (
    TransactionNonCatalogPrice as TransactionNonCatalogPrice,
)
from paddle_billing.Resources.Transactions.Operations.Price.TransactionNonCatalogPriceWithProduct import (
    TransactionNonCatalogPriceWithProduct as TransactionNonCatalogPriceWithProduct,
)


@dataclass
class TransactionCreateItemWithPrice:
    price: TransactionNonCatalogPrice | TransactionNonCatalogPriceWithProduct
    quantity: int
