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
    status:       Status
    tax_category: TaxCategory
    created_at:   datetime    | None
    custom_data:  CustomData  | None
    description:  str         | None
    image_url:    str         | None
    import_meta:  ImportMeta  | None
    type:         CatalogType | None


    @classmethod
    def from_dict(cls, data: dict) -> Product:
        return Product(
            id           = data['id'],
            name         = data['name'],
            description  = data.get('description'),
            tax_category = TaxCategory(data['tax_category']),
            image_url    = data.get('image_url'),
            status       = Status(data['status']),
            type         = CatalogType(data['type'])                  if data.get('type')        else None,
            custom_data  = CustomData(data['custom_data'])            if data.get('custom_data') else None,
            created_at   = datetime.fromisoformat(data['created_at']) if data.get('created_at')  else None,
            import_meta  = ImportMeta.from_dict(data['import_meta'])  if data.get('import_meta') else None,
        )

