from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Entity          import Entity
from paddle_billing.Entities.Shared          import AddressPreview, AvailablePaymentMethods, CurrencyCode
from paddle_billing.Entities.PricingPreviews import PricePreviewDetails


@dataclass
class PricePreview(Entity):
    customer_id:               str | None
    address_id:                str | None
    business_id:               str | None
    currency_code:             CurrencyCode
    discount_id:               str | None
    address:                   AddressPreview | None
    customer_ip_address:       str | None
    details:                   PricePreviewDetails
    available_payment_methods: list[AvailablePaymentMethods]


    @classmethod
    def from_dict(cls, data: dict) -> PricePreview:
        return PricePreview(
            customer_id               = data.get('customer_id'),
            address_id                = data.get('address_id'),
            business_id               = data.get('business_id'),
            currency_code             = CurrencyCode(data['currency_code']),
            discount_id               = data.get('discount_id'),
            address                   = AddressPreview.from_dict(data['address']) if data.get('address') else None,
            customer_ip_address       = data.get('customer_ip_address'),
            details                   = PricePreviewDetails.from_dict(data['details']),
            available_payment_methods = [AvailablePaymentMethods(item) for item in data['available_payment_methods']],
        )
