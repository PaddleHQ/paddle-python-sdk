from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Entity import Entity


@dataclass
class PricePreviewItem(Entity):
    priceId:  str
    quantity: int


    @classmethod
    def from_dict(cls, data: dict) -> PricePreviewItem:
        return PricePreviewItem(
            priceId  = data['price_id'],
            quantity = data['quantity'],
        )
