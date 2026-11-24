from dataclasses import dataclass

from paddle_billing.Operation import Operation as Operation
from paddle_billing.Undefined import Undefined as Undefined
from paddle_billing.Entities.Shared import (
    CatalogType as CatalogType,
    CustomData as CustomData,
    Status as Status,
    TaxCategory as TaxCategory,
)


@dataclass
class UpdateProduct(Operation):
    name: str | Undefined = Undefined()
    description: str | None | Undefined = Undefined()
    type: CatalogType | None | Undefined = Undefined()
    tax_category: TaxCategory | Undefined = Undefined()
    image_url: str | None | Undefined = Undefined()
    custom_data: CustomData | None | Undefined = Undefined()
    status: Status | Undefined = Undefined()
