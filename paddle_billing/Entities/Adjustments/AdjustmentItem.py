from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Adjustments.AdjustmentType import AdjustmentType


@dataclass
class AdjustmentItem:
    item_id: str
    type:    AdjustmentType
    amount:  str | None


    @staticmethod
    def from_dict(data: dict) -> AdjustmentItem:
        return AdjustmentItem(
            item_id = data['item_id'],
            type    = AdjustmentType(data['type']),
            amount  = data.get('amount'),
        )
