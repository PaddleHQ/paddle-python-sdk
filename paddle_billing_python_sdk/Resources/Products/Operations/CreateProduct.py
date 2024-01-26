from dataclasses import dataclass, asdict

from paddle_billing_python_sdk.Entities.Shared.CatalogType import CatalogType
from paddle_billing_python_sdk.Entities.Shared.CustomData  import CustomData
from paddle_billing_python_sdk.Entities.Shared.TaxCategory import TaxCategory


@dataclass
class CreateProduct:
    name:         str
    tax_category: TaxCategory
    type:         CatalogType | None = None
    description:  str | None         = None
    image_url:    str | None         = None
    custom_data:  CustomData | None  = None


    def get_parameters(self) -> dict:
        return asdict(self)
