from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Transactions.TransactionNonCatalogPrice            import TransactionNonCatalogPrice
from src.Entities.Transactions.TransactionNonCatalogPriceWithProduct import TransactionNonCatalogPriceWithProduct


@dataclass
class TransactionCreateItemWithPrice:
    price:    TransactionNonCatalogPrice | TransactionNonCatalogPriceWithProduct
    quantity: int
