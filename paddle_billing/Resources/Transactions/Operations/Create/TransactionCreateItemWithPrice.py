from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.Resources.Transactions.Operations.Price.TransactionNonCatalogPrice import TransactionNonCatalogPrice
from paddle_billing.Resources.Transactions.Operations.Price.TransactionNonCatalogPriceWithProduct import (
    TransactionNonCatalogPriceWithProduct,
)


@dataclass
class TransactionCreateItemWithPrice:
    price: TransactionNonCatalogPrice | TransactionNonCatalogPriceWithProduct
    quantity: int
