from __future__  import annotations
from dataclasses import dataclass


@dataclass
class AdjustmentItemTotals:
    subtotal: str
    tax:      str
    total:    str


    @staticmethod
    def from_dict(data: dict) -> AdjustmentItemTotals:
        return AdjustmentItemTotals(
            subtotal = data['subtotal'],
            tax      = data['tax'],
            total    = data['total'],
        )
