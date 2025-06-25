from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class PricePreviewUnitTotalsFormatted:
    subtotal: str
    discount: str
    tax: str
    total: str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> PricePreviewUnitTotalsFormatted:
        return PricePreviewUnitTotalsFormatted(
            subtotal=data["subtotal"],
            discount=data["discount"],
            tax=data["tax"],
            total=data["total"],
        )
