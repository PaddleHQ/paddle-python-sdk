from __future__                                           import annotations
from .Entity                                              import Entity
from dataclasses                                          import dataclass
from datetime                                             import datetime
from src.Entities.Collections.PriceWithIncludesCollection import PriceWithIncludesCollection  # TODO
from src.Entities.Shared.CatalogType                      import CatalogType
from src.Entities.Shared.CustomData                       import CustomData
from src.Entities.Shared.Status                           import Status
from src.Entities.Shared.TaxCategory                      import TaxCategory
from typing                                               import Optional, Union


@dataclass
class ProductWithIncludes(Entity):
    id:          str
    name:        str
    description: Optional[str]
    type:        Union[CatalogType, None]
    taxCategory: TaxCategory
    imageUrl:    Optional[str]
    customData:  Union[CustomData, None]
    status:      Status
    createdAt:   Union[datetime, None]
    prices:      PriceWithIncludesCollection


    @classmethod
    def from_dict(cls, data: dict) -> ProductWithIncludes:
        return ProductWithIncludes(
            id          = data['id'],
            name        = data['name'],
            description = data.get('description'),
            type        = CustomData(data['type']) if data.get('type') else None,
            taxCategory = TaxCategory(data['tax_category']),
            imageUrl    = data.get('image_url'),
            customData  = CustomData(data['custom_data']) if data.get('custom_data') else None,
            status      = Status(data['status']),
            createdAt   = datetime.fromisoformat(data['created_at']) if data.get('created_at') else None,
            prices      = PriceWithIncludesCollection.from_dict(data.get('prices', [])),  # TODO
        )
