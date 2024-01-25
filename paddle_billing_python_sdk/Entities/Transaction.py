from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from paddle_billing_python_sdk.Entities.Entity import Entity

from paddle_billing_python_sdk.Entities.Shared.BillingDetails            import BillingDetails
from paddle_billing_python_sdk.Entities.Shared.Checkout                  import Checkout
from paddle_billing_python_sdk.Entities.Shared.CollectionMode            import CollectionMode
from paddle_billing_python_sdk.Entities.Shared.CustomData                import CustomData
from paddle_billing_python_sdk.Entities.Shared.CurrencyCode              import CurrencyCode
from paddle_billing_python_sdk.Entities.Shared.StatusTransaction         import StatusTransaction
from paddle_billing_python_sdk.Entities.Shared.TransactionOrigin         import TransactionOrigin
from paddle_billing_python_sdk.Entities.Shared.TransactionPaymentAttempt import TransactionPaymentAttempt

from paddle_billing_python_sdk.Entities.Transactions.TransactionDetails    import TransactionDetails
from paddle_billing_python_sdk.Entities.Transactions.TransactionItem       import TransactionItem
from paddle_billing_python_sdk.Entities.Transactions.TransactionTimePeriod import TransactionTimePeriod


@dataclass
class Transaction(Entity):
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
    billing_period:  TransactionTimePeriod | None
    items:           list[TransactionItem]
    details:         TransactionDetails
    payments:        list[TransactionPaymentAttempt]
    checkout:        Checkout
    created_at:      datetime
    updated_at:      datetime
    billed_at:       datetime | None


    @classmethod
    def from_dict(cls, data: dict) -> Transaction:
        return Transaction(
            id              = data['id'],
            status          = StatusTransaction(data['status']),
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
            details         = TransactionDetails.from_dict(data['details']),
            created_at      = datetime.fromisoformat(data['created_at']),
            updated_at      = datetime.fromisoformat(data['updated_at']),
            items           = [TransactionItem.from_dict(item)              for item    in data.get('items',    [])],
            payments        = [TransactionPaymentAttempt.from_dict(payment) for payment in data.get('payments', [])],
            custom_data     = CustomData(data['custom_data'])                         if data.get('custom_data')     else None,
            billing_details = BillingDetails.from_dict(data['billing_details'])       if data.get('billing_details') else None,
            billing_period  = TransactionTimePeriod.from_dict(data['billing_period']) if data.get('billing_period')  else None,
            checkout        = Checkout.from_dict(data['checkout'])                    if data.get('checkout')        else None,
            billed_at       = datetime.fromisoformat(data['billed_at'])               if data.get('billed_at')       else None,
        )