from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Shared.AdjustmentItemTotals import AdjustmentItemTotals
from paddle_billing.Entities.Shared.Type                 import Type

from paddle_billing.Entities.Transactions.TransactionProration import TransactionProration


@dataclass
class TransactionAdjustmentItem:
    id:        str
    item_id:   str
    type:      Type
    amount:    str | None
    proration: TransactionProration
    totals:    AdjustmentItemTotals


    @staticmethod
    def from_dict(data: dict) -> TransactionAdjustmentItem:
        return TransactionAdjustmentItem(
            id        = data['id'],
            item_id   = data['item_id'],
            type      = Type(data['type']),
            amount    = data.get('amount'),
            proration = data['proration'],
            totals    = AdjustmentItemTotals.from_dict(data['totals']),
        )
