from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Transactions.TransactionNonCatalogPrice            import TransactionNonCatalogPrice
from paddle_billing.Entities.Transactions.TransactionNonCatalogPriceWithProduct import TransactionNonCatalogPriceWithProduct


@dataclass
class TransactionItemPreviewWithNonCatalogPrice:
    price:             TransactionNonCatalogPrice | TransactionNonCatalogPriceWithProduct
    quantity:          int
    include_in_totals: bool | None


    @staticmethod
    def from_dict(data: dict) -> TransactionItemPreviewWithNonCatalogPrice:
        return TransactionItemPreviewWithNonCatalogPrice(
            price             = data['price'],
            quantity          = data['quantity'],
            include_in_totals = data.get('include_in_totals'),
        )
