from dataclasses import dataclass, asdict

from paddle_billing_python_sdk.Undefined                                 import Undefined

from paddle_billing_python_sdk.Entities.PricingPreviews.PricePreviewItem import PricePreviewItem
from paddle_billing_python_sdk.Entities.Shared.CurrencyCode              import CurrencyCode
from paddle_billing_python_sdk.Entities.Shared.AddressPreview            import AddressPreview


@dataclass
class PreviewPrice:
    items:               list[PricePreviewItem]
    customer_id:         str | None | Undefined            = Undefined()
    address_id:          str | None | Undefined            = Undefined()
    business_id:         str | None | Undefined            = Undefined()
    currency_code:       CurrencyCode | Undefined          = Undefined()
    discount_id:         str | None | Undefined            = Undefined()
    address:             AddressPreview | None | Undefined = Undefined()
    customer_ip_address: str | None | Undefined            = Undefined()

    def get_parameters(self) -> dict:
        return asdict(self)
