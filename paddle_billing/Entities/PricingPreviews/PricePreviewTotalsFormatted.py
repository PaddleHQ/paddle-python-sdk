from __future__ import annotations
from dataclasses import dataclass


@dataclass
class PricePreviewTotalsFormatted:
    subtotal: str
    discount: str
    tax: str
    total: str

    @staticmethod
    def from_dict(data: dict) -> PricePreviewTotalsFormatted:
        return PricePreviewTotalsFormatted(
            subtotal=data["subtotal"],
            discount=data["discount"],
            tax=data["tax"],
            total=data["total"],
        )
