from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class AdjustmentTotals:
    subtotal: str
    tax: str
    total: str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> AdjustmentTotals:
        return AdjustmentTotals(
            subtotal=data["subtotal"],
            tax=data["tax"],
            total=data["total"],
        )
