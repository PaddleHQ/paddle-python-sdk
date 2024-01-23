from __future__  import annotations
from dataclasses import dataclass

from src.Entities.ProductWithIncludes import ProductWithIncludes

from src.Entities.Transactions.TransactionProration import TransactionProration

from src.Entities.Shared.Totals     import Totals
from src.Entities.Shared.UnitTotals import UnitTotals


@dataclass
class TransactionLineItem:
    id:         str
    priceId:    str
    quantity:   int
    proration:  TransactionProration | None
    taxRate:    str
    unitTotals: UnitTotals
    totals:     Totals
    product:    ProductWithIncludes


    @staticmethod
    def from_dict(data: dict) -> TransactionLineItem:
        return TransactionLineItem(
            id         = data['id'],
            priceId    = data['price_id'],
            quantity   = data['quantity'],
            proration  = TransactionProration.from_dict(data['proration']) if 'proration' in data else None,
            taxRate    = data['tax_rate'],
            unitTotals = UnitTotals.from_dict(data['unit_totals']),
            totals     = Totals.from_dict(data['totals']),
            product    = ProductWithIncludes.from_dict(data['product']),
        )
