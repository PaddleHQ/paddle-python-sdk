from __future__                                               import annotations
from dataclasses                                              import dataclass
from .Entity                                                  import Entity
from src.Entities.Shared.AddressPreview                       import AddressPreview
from src.Entities.Shared.AvailablePaymentMethods              import AvailablePaymentMethods
from src.Entities.Shared.CurrencyCode                         import CurrencyCode
from src.Entities.Shared.TransactionDetailsPreview            import TransactionDetailsPreview
from src.Entities.Transaction.TransactionItemPreviewWithPrice import TransactionItemPreviewWithPrice
from typing                                                   import Optional, List


@dataclass
class TransactionPreview(Entity):
    customerId:              Optional[str]
    addressId:               Optional[str]
    businessId:              Optional[str]
    currencyCode:            CurrencyCode
    discountId:              Optional[str]
    customerIpAddress:       Optional[str]
    address:                 Optional[AddressPreview]
    ignoreTrials:            bool
    items:                   List[TransactionItemPreviewWithPrice]
    details:                 TransactionDetailsPreview
    availablePaymentMethods: List[AvailablePaymentMethods]


    @classmethod
    def from_dict(cls, data: dict) -> TransactionPreview:
        return cls(
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
