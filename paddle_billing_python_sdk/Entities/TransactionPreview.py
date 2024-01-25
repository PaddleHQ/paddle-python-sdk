from __future__  import annotations
from dataclasses import dataclass

from paddle_billing_python_sdk.Entities.Entity import Entity

from paddle_billing_python_sdk.Entities.Shared.AddressPreview            import AddressPreview
from paddle_billing_python_sdk.Entities.Shared.AvailablePaymentMethods   import AvailablePaymentMethods
from paddle_billing_python_sdk.Entities.Shared.CurrencyCode              import CurrencyCode
from paddle_billing_python_sdk.Entities.Shared.TransactionDetailsPreview import TransactionDetailsPreview

from paddle_billing_python_sdk.Entities.Transactions.TransactionItemPreviewWithPrice import TransactionItemPreviewWithPrice


@dataclass
class TransactionPreview(Entity):
    customer_id:               str | None
    address_id:                str | None
    business_id:               str | None
    currency_code:             CurrencyCode
    discount_id:               str | None
    customer_ip_address:       str | None
    address:                   AddressPreview | None
    ignore_trials:             bool
    items:                     list[TransactionItemPreviewWithPrice]
    details:                   TransactionDetailsPreview
    available_payment_methods: list[AvailablePaymentMethods]


    @classmethod
    def from_dict(cls, data: dict) -> TransactionPreview:
        return TransactionPreview(
            customer_id               = data.get('customer_id'),
            address_id                = data.get('address_id'),
            business_id               = data.get('business_id'),
            currency_code             = CurrencyCode(data['currency_code']),
            discount_id               = data.get('discount_id'),
            customer_ip_address       = data.get('customer_ip_address'),
            address                   = AddressPreview.from_dict(data['address']) if 'address' in data else None,
            ignore_trials             = data['ignore_trials'],
            items                     = [TransactionItemPreviewWithPrice.from_dict(item) for item in data['items']],
            details                   = TransactionDetailsPreview.from_dict(data['details']),
            available_payment_methods = [AvailablePaymentMethods(method) for method in data['available_payment_methods']],
        )
