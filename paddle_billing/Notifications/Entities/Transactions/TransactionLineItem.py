from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Notifications.Entities.Product import Product

from paddle_billing.Notifications.Entities.Transactions.TransactionProration import TransactionProration

from paddle_billing.Notifications.Entities.Shared.Totals     import Totals
from paddle_billing.Notifications.Entities.Shared.UnitTotals import UnitTotals


@dataclass
class TransactionLineItem:
    id:          str
    price_id:    str
    quantity:    int
    proration:   TransactionProration | None
    tax_rate:    str
    unit_totals: UnitTotals
    totals:      Totals
    product:     Product


    @staticmethod
    def from_dict(data: dict) -> TransactionLineItem:
        return TransactionLineItem(
            id          = data['id'],
            price_id    = data['price_id'],
            quantity    = data['quantity'],
            proration   = TransactionProration.from_dict(data['proration']) if data.get('proration') else None,
            tax_rate    = data['tax_rate'],
            unit_totals = UnitTotals.from_dict(data['unit_totals']),
            totals      = Totals.from_dict(data['totals']),
            product     = Product.from_dict(data['product']),
        )
