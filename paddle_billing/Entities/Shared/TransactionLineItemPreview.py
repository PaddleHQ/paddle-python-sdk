from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Shared.TransactionPreviewProduct import TransactionPreviewProduct
from paddle_billing.Entities.Shared.Totals import Totals
from paddle_billing.Entities.Shared.UnitTotals import UnitTotals
from paddle_billing.Entities.Shared.Proration import Proration


@dataclass
class TransactionLineItemPreview:
    price_id: str | None
    quantity: int
    tax_rate: str
    unit_totals: UnitTotals
    totals: Totals
    product: TransactionPreviewProduct
    proration: Proration | None

    @staticmethod
    def from_dict(data: dict) -> TransactionLineItemPreview:
        return TransactionLineItemPreview(
            price_id=data.get("price_id"),
            quantity=data["quantity"],
            tax_rate=data["tax_rate"],
            unit_totals=UnitTotals.from_dict(data["unit_totals"]),
            totals=Totals.from_dict(data["totals"]),
            product=TransactionPreviewProduct.from_dict(data["product"]),
            proration=Proration.from_dict(data["proration"]) if data.get("proration") else None,
        )
