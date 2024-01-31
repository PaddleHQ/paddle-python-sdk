from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from paddle_billing_python_sdk.Entities.Entity  import Entity
from paddle_billing_python_sdk.Entities.Address import Address
from paddle_billing_python_sdk.Entities.Business import Business
from paddle_billing_python_sdk.Entities.Customer import Customer
from paddle_billing_python_sdk.Entities.Discount import Discount

from paddle_billing_python_sdk.Entities.Shared.AvailablePaymentMethods   import AvailablePaymentMethods
from paddle_billing_python_sdk.Entities.Shared.BillingDetails            import BillingDetails
from paddle_billing_python_sdk.Entities.Shared.Checkout                  import Checkout
from paddle_billing_python_sdk.Entities.Shared.CollectionMode            import CollectionMode
from paddle_billing_python_sdk.Entities.Shared.CustomData                import CustomData
from paddle_billing_python_sdk.Entities.Shared.CurrencyCode              import CurrencyCode
from paddle_billing_python_sdk.Entities.Shared.StatusTransaction         import StatusTransaction
from paddle_billing_python_sdk.Entities.Shared.TransactionOrigin         import TransactionOrigin
from paddle_billing_python_sdk.Entities.Shared.TransactionPaymentAttempt import TransactionPaymentAttempt

from paddle_billing_python_sdk.Entities.Transactions.TransactionAdjustment        import TransactionAdjustment
from paddle_billing_python_sdk.Entities.Transactions.TransactionAdjustmentsTotals import TransactionAdjustmentsTotals
from paddle_billing_python_sdk.Entities.Transactions.TransactionDetails           import TransactionDetails
from paddle_billing_python_sdk.Entities.Transactions.TransactionItem              import TransactionItem
from paddle_billing_python_sdk.Entities.Transactions.TransactionTimePeriod        import TransactionTimePeriod


@dataclass
class Transaction(Entity):
    id:                        str
    status:                    StatusTransaction
    customer_id:               str        | None
    address_id:                str        | None
    business_id:               str        | None
    custom_data:               CustomData | None
    currency_code:             CurrencyCode
    origin:                    TransactionOrigin
    subscription_id:           str | None
    invoice_id:                str | None
    invoice_number:            str | None
    collection_mode:           CollectionMode
    discount_id:               str                   | None
    billing_details:           BillingDetails        | None
    billing_period:            TransactionTimePeriod | None
    items:                     list[TransactionItem]
    details:                   TransactionDetails
    payments:                  list[TransactionPaymentAttempt]
    checkout:                  Checkout | None
    created_at:                datetime
    updated_at:                datetime
    billed_at:                 datetime                           | None
    address:                   Address                            | None = None
    adjustments:               list[TransactionAdjustment]        | None = None
    adjustment_totals:         list[TransactionAdjustmentsTotals] | None = None
    business:                  Business                           | None = None
    customer:                  Customer                           | None = None
    discount:                  Discount                           | None = None
    available_payment_methods: list[AvailablePaymentMethods]      | None = None


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
            items           = [TransactionItem.from_dict(item)           for item in data.get('items',       [])],
            payments        = [TransactionPaymentAttempt.from_dict(item) for item in data.get('payments',    [])],
            adjustments     = [TransactionAdjustment.from_dict(item)     for item in data.get('adjustments', [])],
            address         = Address.from_dict(data['address'])                      if data.get('address')         else None,
            billed_at       = datetime.fromisoformat(data['billed_at'])               if data.get('billed_at')       else None,
            billing_details = BillingDetails.from_dict(data['billing_details'])       if data.get('billing_details') else None,
            billing_period  = TransactionTimePeriod.from_dict(data['billing_period']) if data.get('billing_period')  else None,
            business        = Business.from_dict(data['business'])                    if data.get('business')        else None,
            custom_data     = CustomData(data['custom_data'])                         if data.get('custom_data')     else None,
            checkout        = Checkout.from_dict(data['checkout'])                    if data.get('checkout')        else None,
            customer        = Customer.from_dict(data['customer'])                    if data.get('customer')        else None,
            discount        = Discount.from_dict(data['discount'])                    if data.get('discount')        else None,

            available_payment_methods = [AvailablePaymentMethods(item) for item    in data.get('available_payment_methods', [])],
            adjustment_totals         = TransactionAdjustmentsTotals.from_dict(data['adjustment_totals']) if data.get('adjustment_totals') else None,
        )
