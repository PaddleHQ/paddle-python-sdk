from __future__  import annotations
from dataclasses import dataclass

from paddle_billing_python_sdk.Entities.Shared.CustomData  import CustomData
from paddle_billing_python_sdk.Entities.Shared.TaxCategory import TaxCategory


@dataclass
class TransactionNonCatalogProduct:
    name:         str
    description:  str | None
    tax_category: TaxCategory
    image_url:    str | None
    custom_data:  CustomData | None


    @staticmethod
    def from_dict(data: dict) -> TransactionNonCatalogProduct:
        return TransactionNonCatalogProduct(
            name         = data['name'],
            description  = data.get('description'),
            tax_category = TaxCategory(data['tax_category']) if 'tax_category' in data and data['tax_category'] != '' else None,
            image_url    = data.get('image_url'),
            custom_data  = CustomData(data['custom_data']) if 'custom_data' in data and data['custom_data'] != '' else None,
        )
