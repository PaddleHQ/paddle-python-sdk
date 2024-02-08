from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from paddle_billing.Entities.Adjustment import Adjustment
from paddle_billing.Entities.Entity     import Entity
from paddle_billing.Entities.Address    import Address
from paddle_billing.Entities.Business   import Business
from paddle_billing.Entities.Customer   import Customer
from paddle_billing.Entities.Discount   import Discount

from paddle_billing.Entities.Shared import (
    AvailablePaymentMethods,
    BillingDetails,
    Checkout,
    CollectionMode,
    CurrencyCode,
    CustomData,
    TransactionOrigin,
    TransactionPaymentAttempt,
    TransactionStatus,
)

from paddle_billing.Entities.Transactions.TransactionAdjustmentsTotals import TransactionAdjustmentsTotals
from paddle_billing.Entities.Transactions.TransactionDetails           import TransactionDetails
from paddle_billing.Entities.Transactions.TransactionItem              import TransactionItem
from paddle_billing.Entities.Transactions.TransactionTimePeriod        import TransactionTimePeriod


@dataclass
class Transaction(Entity):
    id:                        str
    status:                    TransactionStatus
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
    adjustments:               list[Adjustment]                   | None = None
    adjustment_totals:         list[TransactionAdjustmentsTotals] | None = None
    business:                  Business                           | None = None
    customer:                  Customer                           | None = None
    discount:                  Discount                           | None = None
    available_payment_methods: list[AvailablePaymentMethods]      | None = None
    receipt_data:              str                                | None = None


    @classmethod
    def from_dict(cls, data: dict) -> Transaction:
        return Transaction(
            address_id      = data.get('address_id'),
            business_id     = data.get('business_id'),
            collection_mode = CollectionMode(data['collection_mode']),
            created_at      = datetime.fromisoformat(data['created_at']),
            currency_code   = CurrencyCode(data['currency_code']),
            customer_id     = data.get('customer_id'),
            details         = TransactionDetails.from_dict(data['details']),
            discount_id     = data.get('discount_id'),
            id              = data['id'],
            invoice_id      = data.get('invoice_id'),
            invoice_number  = data.get('invoice_number'),
            origin          = TransactionOrigin(data['origin']),
            receipt_data    = data.get('receipt_data'),
            status          = TransactionStatus(data['status']),
            subscription_id = data.get('subscription_id'),
            updated_at      = datetime.fromisoformat(data['updated_at']),
            items           = [TransactionItem.from_dict(item)           for item in data.get('items',       [])],
            payments        = [TransactionPaymentAttempt.from_dict(item) for item in data.get('payments',    [])],
            adjustments     = [Adjustment.from_dict(item)                for item in data.get('adjustments', [])],
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
