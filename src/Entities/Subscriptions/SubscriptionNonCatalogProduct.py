from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Shared.CatalogType import CatalogType
from src.Entities.Shared.CustomData  import CustomData
from src.Entities.Shared.TaxCategory import TaxCategory


@dataclass
class SubscriptionNonCatalogProduct:
    name:        str
    description: str | None
    type:        CatalogType | None
    taxCategory: TaxCategory
    imageUrl:    str | None
    customData:  CustomData | None


    @staticmethod
    def from_dict(data: dict) -> SubscriptionNonCatalogProduct:
        return SubscriptionNonCatalogProduct(
            name        = data['name'],
            description = data.get('description'),
            type        = CatalogType(data['type']) if data.get('type') is not None else None,
            taxCategory = TaxCategory(data['tax_category']),
            imageUrl    = data.get('image_url'),
            customData  = CustomData(data['custom_data']) if 'custom_data' in data else None,
        )
