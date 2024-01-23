from __future__  import annotations
from dataclasses import dataclass

from src.Entities.ProductWithIncludes import ProductWithIncludes

from src.Entities.Shared.Totals     import Totals
from src.Entities.Shared.UnitTotals import UnitTotals


@dataclass
class TransactionLineItemPreview:
    priceId:    str
    quantity:   int
    taxRate:    str
    unitTotals: UnitTotals
    totals:     Totals
    product:    ProductWithIncludes


    @staticmethod
    def from_dict(data: dict) -> TransactionLineItemPreview:
        return TransactionLineItemPreview(
            priceId    = data['price_id'],
            quantity   = data['quantity'],
            taxRate    = data['tax_rate'],
            unitTotals = UnitTotals.from_dict(data['unit_totals']),
            totals     = Totals.from_dict(data['totals']),
            product    = ProductWithIncludes.from_dict(data['product']),
        )
