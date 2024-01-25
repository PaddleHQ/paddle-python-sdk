from __future__  import annotations
from dataclasses import dataclass

from paddle_billing_python_sdk.Entities.Entity  import Entity
from paddle_billing_python_sdk.Entities.Price   import Price
from paddle_billing_python_sdk.Entities.Product import Product

from paddle_billing_python_sdk.Entities.Shared.Totals     import Totals
from paddle_billing_python_sdk.Entities.Shared.UnitTotals import UnitTotals

from paddle_billing_python_sdk.Entities.PricingPreviews.PricePreviewUnitTotalsFormatted import PricePreviewUnitTotalsFormatted
from paddle_billing_python_sdk.Entities.PricingPreviews.PricePreviewTotalsFormatted     import PricePreviewTotalsFormatted
from paddle_billing_python_sdk.Entities.PricingPreviews.PricePreviewDiscounts           import PricePreviewDiscounts


@dataclass
class PricePreviewLineItem(Entity):
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
