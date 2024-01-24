from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from src.Entities.Address  import Address
from src.Entities.Business import Business
from src.Entities.Customer import Customer
from src.Entities.Discount import Discount
from src.Entities.Entity   import Entity

from src.Entities.Shared.BillingDetails            import BillingDetails
from src.Entities.Shared.Checkout                  import Checkout
from src.Entities.Shared.CollectionMode            import CollectionMode
from src.Entities.Shared.CurrencyCode              import CurrencyCode
from src.Entities.Shared.CustomData                import CustomData
from src.Entities.Shared.StatusTransaction         import StatusTransaction
from src.Entities.Shared.TransactionOrigin         import TransactionOrigin
from src.Entities.Shared.TransactionPaymentAttempt import TransactionPaymentAttempt

from src.Entities.Subscriptions.SubscriptionAdjustment      import SubscriptionAdjustment
from src.Entities.Subscriptions.SubscriptionDetails         import SubscriptionDetails
from src.Entities.Subscriptions.SubscriptionTimePeriod      import SubscriptionTimePeriod
from src.Entities.Subscriptions.SubscriptionTransactionItem import SubscriptionTransactionItem


@dataclass
class SubscriptionTransaction(Entity):
    id:             str
    status:         StatusTransaction
    customerId:     str | None
    addressId:      str | None
    businessId:     str | None
    customData:     CustomData | None
    currencyCode:   CurrencyCode
    origin:         TransactionOrigin
    subscriptionId: str | None
    invoiceId:      str | None
    invoiceNumber:  str | None
    collectionMode: CollectionMode
    discountId:     str | None
    billingDetails: BillingDetails | None
    billingPeriod:  SubscriptionTimePeriod
    items:          list[SubscriptionTransactionItem]
    details:        SubscriptionDetails
    payments:       list[TransactionPaymentAttempt]
    checkout:       Checkout
    createdAt:      datetime
    updatedAt:      datetime
    billedAt:       datetime | None
    customer:       Customer
    address:        Address
    business:       Business
    discount:       Discount
    adjustments:    list[SubscriptionAdjustment]


    @classmethod
    def from_dict(cls, data: dict) -> SubscriptionTransaction:
        return SubscriptionTransaction(
            id             = data['id'],
            status         = StatusTransaction(data['status']),
            customerId     = data.get('customer_id'),
            addressId      = data.get('address_id'),
            businessId     = data.get('business_id'),
            customData     = CustomData(data['custom_data']) if 'custom_data' in data else None,
            currencyCode   = CurrencyCode(data['currency_code']),
            origin         = TransactionOrigin(data['origin']),
            subscriptionId = data.get('subscription_id'),
            invoiceId      = data.get('invoice_id'),
            invoiceNumber  = data.get('invoice_number'),
            collectionMode = CollectionMode(data['collection_mode']),
            discountId     = data.get('discount_id'),
            billingDetails = BillingDetails.from_dict(data['billing_details']) if 'billing_details' in data else None,
            billingPeriod  = SubscriptionTimePeriod.from_dict(data['billing_period']),
            items          = [SubscriptionTransactionItem.from_dict(item) for item in data['items']],
            details        = SubscriptionDetails.from_dict(data['details']),
            payments       = [TransactionPaymentAttempt.from_dict(payment) for payment in data['payments']],
            checkout       = Checkout.from_dict(data['checkout']),
            createdAt      = datetime.fromisoformat(data['created_at']),
            updatedAt      = datetime.fromisoformat(data['updated_at']),
            billedAt       = datetime.fromisoformat(data['billed_at']) if 'billed_at' in data else None,
            customer       = Customer.from_dict(data['customer']),
            address        = Address.from_dict(data['address']),
            business       = Business.from_dict(data['business']),
            discount       = Discount.from_dict(data['discount']),
            adjustments    = [SubscriptionAdjustment.from_dict(adjustment) for adjustment in data['adjustments']],
        )
