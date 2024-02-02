from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Shared import AddressPreview, AvailablePaymentMethods, CurrencyCode

from paddle_billing.Entities.Shared.TransactionDetailsPreview             import TransactionDetailsPreview
from paddle_billing.Entities.Transactions.TransactionItemPreviewWithPrice import TransactionItemPreviewWithPrice


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
            ignore_trials             = data['ignore_trials'],
            details                   = TransactionDetailsPreview.from_dict(data['details']),
            items                     = [TransactionItemPreviewWithPrice.from_dict(item) for item   in data['items']],
            available_payment_methods = [AvailablePaymentMethods(method)                 for method in data['available_payment_methods']],
            address                   = AddressPreview.from_dict(data['address']) if data.get('address') else None,
        )
