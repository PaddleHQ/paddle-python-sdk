from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Shared.CatalogType import CatalogType
from src.Entities.Shared.CustomData  import CustomData
from src.Entities.Shared.TaxCategory import TaxCategory


@dataclass
class SubscriptionNonCatalogProduct:
    name:         str
    description:  str | None
    type:         CatalogType | None
    tax_category: TaxCategory
    image_url:    str | None
    custom_data:  CustomData | None


    @staticmethod
    def from_dict(data: dict) -> SubscriptionNonCatalogProduct:
        return SubscriptionNonCatalogProduct(
            name         = data['name'],
            description  = data.get('description'),
            type         = CatalogType(data['type']) if data.get('type') is not None else None,
            tax_category = TaxCategory(data['tax_category']),
            image_url    = data.get('image_url'),
            custom_data  = CustomData(data['custom_data']) if 'custom_data' in data else None,
        )
