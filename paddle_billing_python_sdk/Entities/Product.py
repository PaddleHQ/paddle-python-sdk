from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from paddle_billing_python_sdk.Entities.Entity import Entity

from paddle_billing_python_sdk.Entities.Shared.CatalogType import CatalogType
from paddle_billing_python_sdk.Entities.Shared.CustomData  import CustomData
from paddle_billing_python_sdk.Entities.Shared.ImportMeta  import ImportMeta
from paddle_billing_python_sdk.Entities.Shared.Status      import Status
from paddle_billing_python_sdk.Entities.Shared.TaxCategory import TaxCategory


@dataclass
class Product(Entity):
    id:           str
    name:         str
    description:  str | None
    type:         CatalogType | None
    tax_category: TaxCategory
    image_url:    str | None
    custom_data:  CustomData | None
    status:       Status
    created_at:   datetime | None
    import_meta:  ImportMeta | None


    @classmethod
    def from_dict(cls, data: dict) -> Product:
        return Product(
            id           = data['id'],
            name         = data['name'],
            description  = data.get('description'),
            type         = CatalogType(data['type']) if 'type' in data and data['type'] != '' else None,
            tax_category = TaxCategory(data['tax_category']),
            image_url    = data.get('image_url'),
            custom_data  = CustomData(data['custom_data']) if 'custom_data' in data and data['custom_data'] != '' else None,
            status       = Status(data['status']),
            created_at   = datetime.fromisoformat(data['created_at']) if 'created_at'  in data and data['created_at'] != '' else None,
            import_meta  = ImportMeta.from_dict(data['import_meta']) if 'import_meta' in data and data['import_meta'] != '' else None,
        )

