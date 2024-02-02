from dataclasses import asdict, dataclass

from paddle_billing.Undefined       import Undefined
from paddle_billing.Entities.Shared import CatalogType, CustomData, Status, TaxCategory


@dataclass
class UpdateProduct:
    name:         str                | Undefined = Undefined()
    description:  str         | None | Undefined = Undefined()
    type:         CatalogType | None | Undefined = Undefined()
    tax_category: TaxCategory        | Undefined = Undefined()
    image_url:    str         | None | Undefined = Undefined()
    custom_data:  CustomData  | None | Undefined = Undefined()
    status:       Status             | Undefined = Undefined()


    def get_parameters(self) -> dict:
        return asdict(self)
