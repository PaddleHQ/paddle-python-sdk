from dataclasses import asdict, dataclass

from paddle_billing.Undefined       import Undefined
from paddle_billing.Entities.Shared import CatalogType, CustomData, TaxCategory


@dataclass
class CreateProduct:
    name:         str
    tax_category: TaxCategory
    type:         CatalogType | None | Undefined = Undefined()
    description:  str         | None | Undefined = Undefined()
    image_url:    str         | None | Undefined = Undefined()
    custom_data:  CustomData  | None | Undefined = Undefined()


    def get_parameters(self) -> dict:
        return asdict(self)
