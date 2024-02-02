from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.PricingPreviews.PricePreviewLineItem import PricePreviewLineItem


@dataclass
class PricePreviewDetails(Entity):
    line_items: list[PricePreviewLineItem]


    @classmethod
    def from_dict(cls, data: dict) -> PricePreviewDetails:
        return PricePreviewDetails(line_items=[PricePreviewLineItem.from_dict(item) for item in data['line_items']])
