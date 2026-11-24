from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.Undefined import Undefined as Undefined
from paddle_billing.Resources.Transactions.Operations.Price.TransactionNonCatalogPrice import (
    TransactionNonCatalogPrice as TransactionNonCatalogPrice,
)
from paddle_billing.Resources.Transactions.Operations.Price.TransactionNonCatalogPriceWithProduct import (
    TransactionNonCatalogPriceWithProduct as TransactionNonCatalogPriceWithProduct,
)


@dataclass
class TransactionItemPreviewWithNonCatalogPrice:
    price: TransactionNonCatalogPrice | TransactionNonCatalogPriceWithProduct
    quantity: int
    include_in_totals: bool | None | Undefined = Undefined()
