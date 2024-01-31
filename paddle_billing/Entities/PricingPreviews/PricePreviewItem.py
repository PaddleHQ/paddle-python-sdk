from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Entity import Entity


@dataclass
class PricePreviewItem(Entity):
    price_id: str
    quantity: int


    @classmethod
    def from_dict(cls, data: dict) -> PricePreviewItem:
        return PricePreviewItem(
            price_id = data['price_id'],
            quantity = data['quantity'],
        )
