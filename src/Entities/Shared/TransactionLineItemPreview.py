from __future__  import annotations
from dataclasses import dataclass

from src.Entities.ProductWithIncludes import ProductWithIncludes

from src.Entities.Shared.Totals     import Totals
from src.Entities.Shared.UnitTotals import UnitTotals


@dataclass
class TransactionLineItemPreview:
    price_id:    str
    quantity:    int
    tax_rate:    str
    unit_totals: UnitTotals
    totals:      Totals
    product:     ProductWithIncludes


    @staticmethod
    def from_dict(data: dict) -> TransactionLineItemPreview:
        return TransactionLineItemPreview(
            price_id    = data['price_id'],
            quantity    = data['quantity'],
            tax_rate    = data['tax_rate'],
            unit_totals = UnitTotals.from_dict(data['unit_totals']),
            totals      = Totals.from_dict(data['totals']),
            product     = ProductWithIncludes.from_dict(data['product']),
        )
