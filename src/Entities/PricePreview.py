from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Entity import Entity

from src.Entities.Shared.AddressPreview          import AddressPreview
from src.Entities.Shared.AvailablePaymentMethods import AvailablePaymentMethods
from src.Entities.Shared.CurrencyCode            import CurrencyCode

from src.Entities.PricingPreviews.PricePreviewDetails import PricePreviewDetails


@dataclass
class PricePreview(Entity):
    customerId:              str | None
    addressId:               str | None
    businessId:              str | None
    currencyCode:            CurrencyCode
    discountId:              str | None
    address:                 AddressPreview | None
    customerIpAddress:       str | None
    details:                 PricePreviewDetails
    availablePaymentMethods: list[AvailablePaymentMethods]


    @classmethod
    def from_dict(cls, data: dict) -> PricePreview:
        return PricePreview(
            customerId              = data.get('customer_id'),
            addressId               = data.get('address_id'),
            businessId              = data.get('business_id'),
            currencyCode            = CurrencyCode(data['currency_code']),
            discountId              = data.get('discount_id'),
            address                 = AddressPreview.from_dict(data['address']) if 'address' in data else None,
            customerIpAddress       = data.get('customer_ip_address'),
            details                 = PricePreviewDetails.from_dict(data['details']),
            availablePaymentMethods = [AvailablePaymentMethods(item) for item in data['available_payment_methods']],
        )
