from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Price   import Price
from paddle_billing.Entities.Product import Product
from paddle_billing.Entities.Shared  import Totals, UnitTotals

from paddle_billing.Entities.PricingPreviews.PricePreviewDiscounts           import PricePreviewDiscounts
from paddle_billing.Entities.PricingPreviews.PricePreviewTotalsFormatted     import PricePreviewTotalsFormatted
from paddle_billing.Entities.PricingPreviews.PricePreviewUnitTotalsFormatted import PricePreviewUnitTotalsFormatted


@dataclass
class PricePreviewLineItem:
    price:                 Price
    quantity:              int
    tax_rate:              str
    unit_totals:           UnitTotals
    formatted_unit_totals: PricePreviewUnitTotalsFormatted
    totals:                Totals
    formatted_totals:      PricePreviewTotalsFormatted
    product:               Product
    discounts:             list[PricePreviewDiscounts]


    @classmethod
    def from_dict(cls, data: dict) -> PricePreviewLineItem:
        return PricePreviewLineItem(
            price                 = Price.from_dict(data['price']),
            quantity              = data['quantity'],
            tax_rate              = data['tax_rate'],
            unit_totals           = UnitTotals.from_dict(data['unit_totals']),
            formatted_unit_totals = PricePreviewUnitTotalsFormatted.from_dict(data['formatted_unit_totals']),
            totals                = Totals.from_dict(data['totals']),
            formatted_totals      = PricePreviewTotalsFormatted.from_dict(data['formatted_totals']),
            product               = Product.from_dict(data['product']),
            discounts             = [PricePreviewDiscounts.from_dict(item) for item in data['discounts']],
        )
