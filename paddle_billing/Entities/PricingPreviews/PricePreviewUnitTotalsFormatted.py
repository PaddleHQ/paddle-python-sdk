from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Entity import Entity


@dataclass
class PricePreviewUnitTotalsFormatted(Entity):
    subtotal: str
    discount: str
    tax:      str
    total:    str


    @classmethod
    def from_dict(cls, data: dict) -> PricePreviewUnitTotalsFormatted:
        return PricePreviewUnitTotalsFormatted(
            subtotal = data['subtotal'],
            discount = data['discount'],
            tax      = data['tax'],
            total    = data['total'],
        )
