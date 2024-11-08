from dataclasses import dataclass

from paddle_billing.Operation import Operation
from paddle_billing.Undefined import Undefined
from paddle_billing.Entities.Shared import CatalogType, CustomData, TaxCategory


@dataclass
class CreateProduct(Operation):
    name: str
    tax_category: TaxCategory
    type: CatalogType | None | Undefined = Undefined()
    description: str | None | Undefined = Undefined()
    image_url: str | None | Undefined = Undefined()
    custom_data: CustomData | None | Undefined = Undefined()
