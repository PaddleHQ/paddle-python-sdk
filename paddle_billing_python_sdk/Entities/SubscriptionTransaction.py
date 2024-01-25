from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from paddle_billing_python_sdk.Entities.Address  import Address
from paddle_billing_python_sdk.Entities.Business import Business
from paddle_billing_python_sdk.Entities.Customer import Customer
from paddle_billing_python_sdk.Entities.Discount import Discount
from paddle_billing_python_sdk.Entities.Entity   import Entity

from paddle_billing_python_sdk.Entities.Shared.BillingDetails            import BillingDetails
from paddle_billing_python_sdk.Entities.Shared.Checkout                  import Checkout
from paddle_billing_python_sdk.Entities.Shared.CollectionMode            import CollectionMode
from paddle_billing_python_sdk.Entities.Shared.CurrencyCode              import CurrencyCode
from paddle_billing_python_sdk.Entities.Shared.CustomData                import CustomData
from paddle_billing_python_sdk.Entities.Shared.StatusTransaction         import StatusTransaction
from paddle_billing_python_sdk.Entities.Shared.TransactionOrigin         import TransactionOrigin
from paddle_billing_python_sdk.Entities.Shared.TransactionPaymentAttempt import TransactionPaymentAttempt

from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionAdjustment      import SubscriptionAdjustment
from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionDetails         import SubscriptionDetails
from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionTimePeriod      import SubscriptionTimePeriod
from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionTransactionItem import SubscriptionTransactionItem


@dataclass
class SubscriptionTransaction(Entity):
    id:              str
    status:          StatusTransaction
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
            status          = StatusTransaction(data['status']),
            customer_id     = data.get('customer_id'),
            address_id      = data.get('address_id'),
            business_id     = data.get('business_id'),
            custom_data     = CustomData(data['custom_data']) if 'custom_data' in data and data['custom_data'] != '' else None,
            currency_code   = CurrencyCode(data['currency_code']),
            origin          = TransactionOrigin(data['origin']),
            subscription_id = data.get('subscription_id'),
            invoice_id      = data.get('invoice_id'),
            invoice_number  = data.get('invoice_number'),
            collection_mode = CollectionMode(data['collection_mode']),
            discount_id     = data.get('discount_id'),
            billing_details = BillingDetails.from_dict(data['billing_details']) if 'billing_details' in data and data['billing_details'] != '' else None,
            billing_period  = SubscriptionTimePeriod.from_dict(data['billing_period']),
            items           = [SubscriptionTransactionItem.from_dict(item) for item in data['items']],
            details         = SubscriptionDetails.from_dict(data['details']),
            payments        = [TransactionPaymentAttempt.from_dict(payment) for payment in data['payments']],
            checkout        = Checkout.from_dict(data['checkout']),
            created_at      = datetime.fromisoformat(data['created_at']),
            updated_at      = datetime.fromisoformat(data['updated_at']),
            billed_at       = datetime.fromisoformat(data['billed_at']) if 'billed_at' in data and data['billed_at'] != '' else None,
            customer        = Customer.from_dict(data['customer']),
            address         = Address.from_dict(data['address']),
            business        = Business.from_dict(data['business']),
            discount        = Discount.from_dict(data['discount']),
            adjustments     = [SubscriptionAdjustment.from_dict(adjustment) for adjustment in data['adjustments']],
        )
