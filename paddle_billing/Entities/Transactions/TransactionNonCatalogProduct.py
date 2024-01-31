from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Shared.CustomData  import CustomData
from paddle_billing.Entities.Shared.TaxCategory import TaxCategory


@dataclass
class TransactionNonCatalogProduct:
    name:         str
    tax_category: TaxCategory
    description:  str        | None
    image_url:    str        | None
    custom_data:  CustomData | None


    @staticmethod
    def from_dict(data: dict) -> TransactionNonCatalogProduct:
        return TransactionNonCatalogProduct(
            name         = data['name'],
            description  = data.get('description'),
            image_url    = data.get('image_url'),
            tax_category = TaxCategory(data['tax_category']) if data.get('tax_category') else None,
            custom_data  = CustomData(data['custom_data'])   if data.get('custom_data')  else None,
        )
