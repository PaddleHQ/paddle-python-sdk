from __future__  import annotations
from dataclasses import asdict, dataclass

from paddle_billing.Entities.Shared import CatalogType, CustomData, TaxCategory


@dataclass
class SubscriptionNonCatalogProduct:
    name:         str
    description:  str         | None
    type:         CatalogType | None
    tax_category: TaxCategory
    image_url:    str        | None
    custom_data:  CustomData | None


    @staticmethod
    def from_dict(data: dict) -> SubscriptionNonCatalogProduct:
        return SubscriptionNonCatalogProduct(
            name         = data['name'],
            description  = data.get('description'),
            tax_category = TaxCategory(data['tax_category']),
            image_url    = data.get('image_url'),
            type         = CatalogType(data['type'])       if data.get('type')        else None,
            custom_data  = CustomData(data['custom_data']) if data.get('custom_data') else None,
        )


    def get_parameters(self) -> dict:
        parameters = asdict(self)

        if isinstance(self.custom_data, CustomData):
            parameters['custom_data'] = self.custom_data.get_parameters()

        return parameters
