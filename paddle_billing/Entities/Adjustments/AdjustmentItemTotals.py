from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Adjustments import AdjustmentProration
from paddle_billing.Entities.Shared      import Type, AdjustmentItemTotals as SharedAdjustmentItemTotals


@dataclass
class AdjustmentItemTotals:
    id:        str
    item_id:   str
    type:      Type
    amount:    str | None
    proration: AdjustmentProration
    totals:    SharedAdjustmentItemTotals


    @staticmethod
    def from_dict(data: dict) -> AdjustmentItemTotals:
        return AdjustmentItemTotals(
            id        = data['id'],
            item_id   = data['item_id'],
            type      = Type(data['type']),
            amount    = data.get('amount'),
            proration = AdjustmentProration.from_dict(data['proration']),
            totals    = SharedAdjustmentItemTotals.from_dict(data['totals']),
        )
