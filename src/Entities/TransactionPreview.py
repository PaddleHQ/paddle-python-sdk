from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Entity import Entity

from src.Entities.Shared.AddressPreview            import AddressPreview
from src.Entities.Shared.AvailablePaymentMethods   import AvailablePaymentMethods
from src.Entities.Shared.CurrencyCode              import CurrencyCode
from src.Entities.Shared.TransactionDetailsPreview import TransactionDetailsPreview

from src.Entities.Transactions.TransactionItemPreviewWithPrice import TransactionItemPreviewWithPrice


@dataclass
class TransactionPreview(Entity):
    customerId:              str | None
    addressId:               str | None
    businessId:              str | None
    currencyCode:            CurrencyCode
    discountId:              str | None
    customerIpAddress:       str | None
    address:                 AddressPreview | None
    ignoreTrials:            bool
    items:                   list[TransactionItemPreviewWithPrice]
    details:                 TransactionDetailsPreview
    availablePaymentMethods: list[AvailablePaymentMethods]


    @classmethod
    def from_dict(cls, data: dict) -> TransactionPreview:
        return TransactionPreview(
            customerId              = data.get('customer_id'),
            addressId               = data.get('address_id'),
            businessId              = data.get('business_id'),
            currencyCode            = CurrencyCode(data['currency_code']),
            discountId              = data.get('discount_id'),
            customerIpAddress       = data.get('customer_ip_address'),
            address                 = AddressPreview.from_dict(data['address']) if 'address' in data else None,
            ignoreTrials            = data['ignore_trials'],
            items                   = [TransactionItemPreviewWithPrice.from_dict(item) for item in data['items']],
            details                 = TransactionDetailsPreview.from_dict(data['details']),
            availablePaymentMethods = [AvailablePaymentMethods(method) for method in data['available_payment_methods']],
        )
