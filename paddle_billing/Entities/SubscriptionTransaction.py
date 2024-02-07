from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from paddle_billing.Entities.Address  import Address
from paddle_billing.Entities.Business import Business
from paddle_billing.Entities.Customer import Customer
from paddle_billing.Entities.Discount import Discount
from paddle_billing.Entities.Entity   import Entity

from paddle_billing.Entities.Shared import (
    BillingDetails,
    Checkout,
    CollectionMode,
    CurrencyCode,
    CustomData,
    TransactionPaymentAttempt,
    TransactionOrigin,
    TransactionStatus,
)

from paddle_billing.Entities.Subscriptions import (
    SubscriptionAdjustment,
    SubscriptionDetails,
    SubscriptionTimePeriod,
    SubscriptionTransactionItem,
)


@dataclass
class SubscriptionTransaction(Entity):
    id:              str
    status:          TransactionStatus
    customer_id:     str | None
    address_id:      str | None
    business_id:     str | None
    custom_data:     CustomData | None
    currency_code:   CurrencyCode
    origin:          TransactionOrigin
    subscription_id: str | None
    invoice_id:      str | None
    invoice_number:  str | None
    collection_mode: CollectionMode
    discount_id:     str | None
    billing_details: BillingDetails | None
    billing_period:  SubscriptionTimePeriod
    items:           list[SubscriptionTransactionItem]
    details:         SubscriptionDetails
    payments:        list[TransactionPaymentAttempt]
    checkout:        Checkout
    created_at:      datetime
    updated_at:      datetime
    billed_at:       datetime | None
    customer:        Customer
    address:         Address
    business:        Business
    discount:        Discount
    adjustments:     list[SubscriptionAdjustment]


    @classmethod
    def from_dict(cls, data: dict) -> SubscriptionTransaction:
        return SubscriptionTransaction(
            id              = data['id'],
            status          = TransactionStatus(data['status']),
            customer_id     = data.get('customer_id'),
            address_id      = data.get('address_id'),
            business_id     = data.get('business_id'),
            currency_code   = CurrencyCode(data['currency_code']),
            origin          = TransactionOrigin(data['origin']),
            subscription_id = data.get('subscription_id'),
            invoice_id      = data.get('invoice_id'),
            invoice_number  = data.get('invoice_number'),
            collection_mode = CollectionMode(data['collection_mode']),
            discount_id     = data.get('discount_id'),
            billing_period  = SubscriptionTimePeriod.from_dict(data['billing_period']),
            details         = SubscriptionDetails.from_dict(data['details']),
            checkout        = Checkout.from_dict(data['checkout']),
            created_at      = datetime.fromisoformat(data['created_at']),
            updated_at      = datetime.fromisoformat(data['updated_at']),
            customer        = Customer.from_dict(data['customer']),
            address         = Address.from_dict(data['address']),
            business        = Business.from_dict(data['business']),
            discount        = Discount.from_dict(data['discount']),
            items           = [SubscriptionTransactionItem.from_dict(item)  for item       in data['items']],
            payments        = [TransactionPaymentAttempt.from_dict(payment) for payment    in data['payments']],
            adjustments     = [SubscriptionAdjustment.from_dict(adjustment) for adjustment in data['adjustments']],
            billed_at       = datetime.fromisoformat(data['billed_at'])         if data.get('billed_at')       else None,
            billing_details = BillingDetails.from_dict(data['billing_details']) if data.get('billing_details') else None,
            custom_data     = CustomData(data['custom_data'])                   if data.get('custom_data')     else None,
        )
