from __future__ import annotations
from dataclasses import dataclass


@dataclass
class PricePreviewUnitTotalsFormatted:
    subtotal: str
    discount: str
    tax: str
    total: str

    @staticmethod
    def from_dict(data: dict) -> PricePreviewUnitTotalsFormatted:
        return PricePreviewUnitTotalsFormatted(
            subtotal=data["subtotal"],
            discount=data["discount"],
            tax=data["tax"],
            total=data["total"],
        )
