from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Entity  import Entity
from src.Entities.Price   import Price
from src.Entities.Product import Product

from src.Entities.Shared.Totals     import Totals
from src.Entities.Shared.UnitTotals import UnitTotals

from src.Entities.PricingPreviews.PricePreviewUnitTotalsFormatted import PricePreviewUnitTotalsFormatted
from src.Entities.PricingPreviews.PricePreviewTotalsFormatted     import PricePreviewTotalsFormatted
from src.Entities.PricingPreviews.PricePreviewDiscounts           import PricePreviewDiscounts


@dataclass
class PricePreviewLineItem(Entity):
    price:               Price
    quantity:            int
    tax_rate:             str
    unit_totals:          UnitTotals
    formattedUnitTotals: PricePreviewUnitTotalsFormatted
    totals:              Totals
    formattedTotals:     PricePreviewTotalsFormatted
    product:             Product
    discounts:           list[PricePreviewDiscounts]


    @classmethod
    def from_dict(cls, data: dict) -> PricePreviewLineItem:
        return PricePreviewLineItem(
            price               = Price.from_dict(data['price']),
            quantity            = data['quantity'],
            tax_rate             = data['tax_rate'],
            unit_totals          = UnitTotals.from_dict(data['unit_totals']),
            formattedUnitTotals = PricePreviewUnitTotalsFormatted.from_dict(data['formatted_unit_totals']),
            totals              = Totals.from_dict(data['totals']),
            formattedTotals     = PricePreviewTotalsFormatted.from_dict(data['formatted_totals']),
            product             = Product.from_dict(data['product']),
            discounts           = [PricePreviewDiscounts.from_dict(item) for item in data['discounts']],
        )
