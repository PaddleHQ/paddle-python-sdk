from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Adjustments.AdjustmentProration import AdjustmentProration

from src.Entities.Shared.AdjustmentItemTotals import AdjustmentItemTotals as SharedAdjustmentItemTotals
from src.Entities.Shared.Type                 import Type


@dataclass
class AdjustmentItemTotals:
    id:        str
    item_id:    str
    type:      Type
    amount:    str | None
    proration: AdjustmentProration
    totals:    SharedAdjustmentItemTotals


    @staticmethod
    def from_dict(data: dict) -> AdjustmentItemTotals:
        return AdjustmentItemTotals(
            id        = data['id'],
            item_id    = data['item_id'],
            type      = Type(data['type']),
            amount    = data.get('amount'),
            proration = AdjustmentProration.from_dict(data['proration']),
            totals    = SharedAdjustmentItemTotals.from_dict(data['totals']),
        )
