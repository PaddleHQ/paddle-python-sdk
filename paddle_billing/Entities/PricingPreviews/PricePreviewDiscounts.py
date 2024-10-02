from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Discount import Discount


@dataclass
class PricePreviewDiscounts:
    discount: Discount
    total: str
    formatted_total: str

    @staticmethod
    def from_dict(data: dict) -> PricePreviewDiscounts:
        return PricePreviewDiscounts(
            discount=Discount.from_dict(data["discount"]),
            total=data["total"],
            formatted_total=data["formatted_total"],
        )
