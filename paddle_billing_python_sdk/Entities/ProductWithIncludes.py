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
    id:           str
    name:         str
    description:  Optional[str]
    type:         CatalogType | None
    tax_category: TaxCategory
    image_url:    Optional[str]
    custom_data:  CustomData | None
    status:       Status
    created_at:   datetime | None
    prices:       PriceWithIncludesCollection


    @classmethod
    def from_dict(cls, data: dict) -> ProductWithIncludes:
        return ProductWithIncludes(
            id           = data['id'],
            name         = data['name'],
            description  = data.get('description'),
            type         = CatalogType(data['type']) if data.get('type') else None,
            tax_category = TaxCategory(data['tax_category']),
            image_url    = data.get('image_url'),
            custom_data  = CustomData(data['custom_data']) if data.get('custom_data') else None,
            status       = Status(data['status']),
            created_at   = datetime.fromisoformat(data['created_at']) if data.get('created_at') else None,
            prices       = PriceWithIncludesCollection.from_list(data['prices']),
        )
