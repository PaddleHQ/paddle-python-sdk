from dataclasses import dataclass, asdict

from paddle_billing_python_sdk.Entities.Shared.CatalogType import CatalogType
from paddle_billing_python_sdk.Entities.Shared.CustomData  import CustomData
from paddle_billing_python_sdk.Entities.Shared.Status      import Status
from paddle_billing_python_sdk.Entities.Shared.TaxCategory import TaxCategory


@dataclass
class UpdateProduct:
    name:         str | None         = None
    description:  str | None         = None
    type:         CatalogType | None = None
    tax_category: TaxCategory | None = None
    image_url:    str | None         = None
    custom_data:  CustomData | None  = None
    status:       Status | None      = None


    def get_parameters(self) -> dict:
        return asdict(self)
