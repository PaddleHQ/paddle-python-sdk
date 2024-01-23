from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Entity import Entity

from src.Entities.PricingPreviews.PricePreviewLineItem import PricePreviewLineItem


@dataclass
class PricePreviewDetails(Entity):
    lineItems: list[PricePreviewLineItem]


    @classmethod
    def from_dict(cls, data: dict) -> PricePreviewDetails:
        return PricePreviewDetails(lineItems=[PricePreviewLineItem.from_dict(item) for item in data['line_items']])
