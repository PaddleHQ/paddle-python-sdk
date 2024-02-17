from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from paddle_billing.Notifications.Entities.Entity import Entity
from paddle_billing.Notifications.Entities.Shared import CatalogType, CustomData, ImportMeta, Status, TaxCategory


@dataclass
class Product(Entity):
    id:           str
    name:         str
    status:       Status
    tax_category: TaxCategory
    description:  str         | None
    image_url:    str         | None
    created_at:   datetime    | None = None
    custom_data:  CustomData  | None = None
    import_meta:  ImportMeta  | None = None
    prices:       list[Price] | None = None
    type:         CatalogType | None = None


    @classmethod
    def from_dict(cls, data: dict) -> Product:
        return Product(
            description  = data.get('description'),
            id           = data['id'],
            image_url    = data.get('image_url'),
            name         = data['name'],
            status       = Status(data['status']),
            tax_category = TaxCategory(data['tax_category']),
            prices       = [Price.from_dict(price) for price in data.get('prices', [])],
            type         = CatalogType(data['type'])                  if data.get('type')        else None,
            custom_data  = CustomData(data['custom_data'])            if data.get('custom_data') else None,
            created_at   = datetime.fromisoformat(data['created_at']) if data.get('created_at')  else None,
            import_meta  = ImportMeta.from_dict(data['import_meta'])  if data.get('import_meta') else None,
        )



# Prevents circular import
from paddle_billing.Entities.Price  import Price  # noqa E402
