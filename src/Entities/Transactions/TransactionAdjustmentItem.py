from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Shared.AdjustmentItemTotals import AdjustmentItemTotals
from src.Entities.Shared.Type                 import Type

from src.Entities.Transactions.TransactionProration import TransactionProration


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
