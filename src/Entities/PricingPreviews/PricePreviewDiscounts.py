from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Entity   import Entity
from src.Entities.Discount import Discount


@dataclass
class PricePreviewDiscounts(Entity):
    discount:       Discount
    total:          str
    formattedTotal: str


    @classmethod
    def from_dict(cls, data: dict) -> PricePreviewDiscounts:
        return PricePreviewDiscounts(
            discount       = Discount.from_dict(data['discount']),
            total          = data['total'],
            formattedTotal = data['formatted_total'],
        )
