from __future__  import annotations
from dataclasses import dataclass

from paddle_billing_python_sdk.Entities.Entity   import Entity
from paddle_billing_python_sdk.Entities.Discount import Discount


@dataclass
class PricePreviewDiscounts(Entity):
    discount:       Discount
    total:          str
    formatted_total: str


    @classmethod
    def from_dict(cls, data: dict) -> PricePreviewDiscounts:
        return PricePreviewDiscounts(
            discount        = Discount.from_dict(data['discount']),
            total           = data['total'],
            formatted_total = data['formatted_total'],
        )