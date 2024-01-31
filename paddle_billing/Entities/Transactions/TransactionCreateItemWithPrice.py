from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Transactions.TransactionNonCatalogPrice            import TransactionNonCatalogPrice
from paddle_billing.Entities.Transactions.TransactionNonCatalogPriceWithProduct import TransactionNonCatalogPriceWithProduct


@dataclass
class TransactionCreateItemWithPrice:
    price:    TransactionNonCatalogPrice | TransactionNonCatalogPriceWithProduct
    quantity: int
