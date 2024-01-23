from __future__                     import annotations
from .SubscriptionProration         import SubscriptionProration
from dataclasses                    import dataclass
from src.Entities.Product           import Product
from src.Entities.Shared.Totals     import Totals
from src.Entities.Shared.UnitTotals import UnitTotals


@dataclass
class SubscriptionTransactionLineItem:
    id:          str
    price_id:    str
    quantity:    int
    proration:   SubscriptionProration
    tax_rate:    str
    unit_totals: UnitTotals
    totals:      Totals
    product:     Product


    @staticmethod
    def from_dict(data: dict) -> SubscriptionTransactionLineItem:
        return SubscriptionTransactionLineItem(
            id          = data['id'],
            price_id    = data['price_id'],
            quantity    = data['quantity'],
            proration   = SubscriptionProration.from_dict(data['proration']),
            tax_rate    = data['tax_rate'],
            unit_totals = UnitTotals.from_dict(data['unit_totals']),
            totals      = Totals.from_dict(data['totals']),
            product     = Product.from_dict(data['product']),
        )
