from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime
from typing      import Optional

from paddle_billing_python_sdk.Entities.Entity import Entity

from paddle_billing_python_sdk.Entities.Collections.PriceWithIncludesCollection import PriceWithIncludesCollection

from paddle_billing_python_sdk.Entities.Shared.CatalogType import CatalogType
from paddle_billing_python_sdk.Entities.Shared.CustomData  import CustomData
from paddle_billing_python_sdk.Entities.Shared.Status      import Status
from paddle_billing_python_sdk.Entities.Shared.TaxCategory import TaxCategory


@dataclass
class ProductWithIncludes(Entity):
    description:  Optional[str]
    id:           str
    image_url:    Optional[str]
    name:         str
    prices:       PriceWithIncludesCollection
    status:       Status
    tax_category: TaxCategory
    type:         CatalogType | None
    custom_data:  CustomData  | None
    created_at:   datetime    | None


    @classmethod
    def from_dict(cls, data: dict) -> ProductWithIncludes:
        return ProductWithIncludes(
            description  = data.get('description'),
            id           = data['id'],
            image_url    = data.get('image_url'),
            name         = data['name'],
            prices       = PriceWithIncludesCollection.from_list(data['prices']),
            status       = Status(data['status']),
            tax_category = TaxCategory(data['tax_category']),
            created_at   = datetime.fromisoformat(data['created_at']) if data.get('created_at')  else None,
            custom_data  = CustomData(data['custom_data'])            if data.get('custom_data') else None,
            type         = CatalogType(data['type'])                  if data.get('type')        else None,
        )
