from __future__                      import annotations
from dataclasses                     import dataclass
from datetime                        import datetime
from src.Entities.Shared.CustomData  import CustomData
from src.Entities.Shared.CatalogType import CatalogType
from src.Entities.Shared.Status      import Status
from src.Entities.Shared.TaxCategory import TaxCategory
from typing                          import Optional


@dataclass
class Product:
    id:          str
    name:        str
    description: Optional[str]
    type:        Optional[CatalogType]
    taxCategory: TaxCategory
    imageUrl:    Optional[str]
    customData:  Optional[CustomData]
    status:      Status
    createdAt:   Optional[datetime]


    @classmethod
    def from_dict(cls, data: dict) -> Product:
        return cls(
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

