from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Product import Product
from paddle_billing.Entities.Shared.Totals import Totals
from paddle_billing.Entities.Shared.UnitTotals import UnitTotals
from paddle_billing.Entities.Shared.Proration import Proration


@dataclass
class TransactionLineItemPreview:
    price_id: str
    quantity: int
    tax_rate: str
    unit_totals: UnitTotals
    totals: Totals
    product: Product
    proration: Proration

    @staticmethod
    def from_dict(data: dict) -> TransactionLineItemPreview:
        return TransactionLineItemPreview(
            price_id=data["price_id"],
            quantity=data["quantity"],
            tax_rate=data["tax_rate"],
            unit_totals=UnitTotals.from_dict(data["unit_totals"]),
            totals=Totals.from_dict(data["totals"]),
            product=Product.from_dict(data["product"]),
            proration=Proration.from_dict(data["proration"]),
        )
