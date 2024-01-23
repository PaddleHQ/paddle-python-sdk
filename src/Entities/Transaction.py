from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime
from typing      import Optional, List

from src.Entities.Entity                             import Entity
from src.Entities.Shared.BillingDetails              import BillingDetails
from src.Entities.Shared.Checkout                    import Checkout
from src.Entities.Shared.CollectionMode              import CollectionMode
from src.Entities.Shared.CustomData                  import CustomData
from src.Entities.Shared.CurrencyCode                import CurrencyCode
from src.Entities.Shared.StatusTransaction           import StatusTransaction
from src.Entities.Shared.TransactionOrigin           import TransactionOrigin
from src.Entities.Shared.TransactionPaymentAttempt   import TransactionPaymentAttempt
from src.Entities.Transactions.TransactionDetails    import TransactionDetails
from src.Entities.Transactions.TransactionItem       import TransactionItem
from src.Entities.Transactions.TransactionTimePeriod import TransactionTimePeriod


@dataclass
class Transaction(Entity):
    id:             str
    status:         StatusTransaction
    customerId:     Optional[str]
    addressId:      Optional[str]
    businessId:     Optional[str]
    customData:     Optional[CustomData]
    currencyCode:   CurrencyCode
    origin:         TransactionOrigin
    subscriptionId: Optional[str]
    invoiceId:      Optional[str]
    invoiceNumber:  Optional[str]
    collectionMode: CollectionMode
    discountId:     Optional[str]
    billingDetails: Optional[BillingDetails]
    billingPeriod:  Optional[TransactionTimePeriod]
    items:          List[TransactionItem]
    details:        TransactionDetails
    payments:       List[TransactionPaymentAttempt]
    checkout:       Checkout
    createdAt:      datetime
    updatedAt:      datetime
    billedAt:       Optional[datetime]


    @classmethod
    def from_dict(cls, data: dict) -> Transaction:
        return Transaction(
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
            billingPeriod  = TransactionTimePeriod.from_dict(data['billing_period']) if 'billing_period' in data else None,
            items          = [TransactionItem.from_dict(item) for item in data.get('items', [])],
            details        = TransactionDetails.from_dict(data['details']),
            payments       = [TransactionPaymentAttempt.from_dict(payment) for payment in data.get('payments', [])],
            checkout       = Checkout.from_dict(data['checkout']) if 'checkout' in data else None,
            createdAt      = datetime.fromisoformat(data['created_at']),
            updatedAt      = datetime.fromisoformat(data['updated_at']),
            billedAt       = datetime.fromisoformat(data['billed_at']) if 'billed_at' in data else None,
        )
