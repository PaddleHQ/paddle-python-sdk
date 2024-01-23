from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Adjustments.AdjustmentType import AdjustmentType


@dataclass
class AdjustmentItem:
    itemId: str
    type:   AdjustmentType
    amount: str | None


    @staticmethod
    def from_dict(data: dict) -> AdjustmentItem:
        return AdjustmentItem(
            itemId = data['itemId'],
            type   = AdjustmentType(data['type']),
            amount = data.get('amount'),
        )
