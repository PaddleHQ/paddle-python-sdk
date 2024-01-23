from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Entity import Entity


@dataclass
class PricePreviewTotalsFormatted(Entity):
    subtotal: str
    discount: str
    tax:      str
    total:    str


    @classmethod
    def from_dict(cls, data: dict) -> PricePreviewTotalsFormatted:
        return PricePreviewTotalsFormatted(
            subtotal = data['subtotal'],
            discount = data['discount'],
            tax      = data['tax'],
            total    = data['total'],
        )
