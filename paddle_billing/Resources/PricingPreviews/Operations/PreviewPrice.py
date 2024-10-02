from dataclasses import asdict, dataclass

from paddle_billing.Undefined import Undefined
from paddle_billing.Entities.PricingPreviews import PricePreviewItem
from paddle_billing.Entities.Shared import CurrencyCode, AddressPreview

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException


@dataclass
class PreviewPrice:
    items: list[PricePreviewItem]
    customer_id: str | None | Undefined = Undefined()
    address_id: str | None | Undefined = Undefined()
    business_id: str | None | Undefined = Undefined()
    currency_code: CurrencyCode | Undefined = Undefined()
    discount_id: str | None | Undefined = Undefined()
    address: AddressPreview | None | Undefined = Undefined()
    customer_ip_address: str | None | Undefined = Undefined()

    def __post_init__(self):
        # Validation
        if len(self.items) == 0:
            raise InvalidArgumentException.array_is_empty("items")

        invalid_items = [item for item in self.items if not isinstance(item, PricePreviewItem)]
        if invalid_items:
            raise InvalidArgumentException.array_contains_invalid_types(
                "items", PricePreviewItem.__name__, invalid_items
            )

    def get_parameters(self) -> dict:
        return asdict(self)
