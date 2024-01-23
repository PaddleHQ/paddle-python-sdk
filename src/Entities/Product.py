from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from src.Entities.Entity import Entity

from src.Entities.Shared.CustomData  import CustomData
from src.Entities.Shared.CatalogType import CatalogType
from src.Entities.Shared.Status      import Status
from src.Entities.Shared.TaxCategory import TaxCategory


@dataclass
class Product(Entity):
    id:          str
    name:        str
    description: str | None
    type:        CatalogType | None
    taxCategory: TaxCategory
    imageUrl:    str | None
    customData:  CustomData | None
    status:      Status
    createdAt:   datetime | None


    @classmethod
    def from_dict(cls, data: dict) -> Product:
        return Product(
            id          = data['id'],
            name        = data['name'],
            description = data.get('description'),
            type        = CatalogType(data['type']) if data.get('type') else None,
            taxCategory = TaxCategory(data['tax_category']),
            imageUrl    = data.get('image_url'),
            customData  = CustomData(data['custom_data']) if data.get('custom_data') else None,
            status      = Status(data['status']),
            createdAt   = datetime.fromisoformat(data['created_at']) if data.get('created_at') else None,
        )

