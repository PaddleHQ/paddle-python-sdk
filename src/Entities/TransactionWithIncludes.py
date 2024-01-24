from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from src.Entities.Address  import Address
from src.Entities.Business import Business
from src.Entities.Customer import Customer
from src.Entities.Discount import Discount
from src.Entities.Entity   import Entity

from src.Entities.Shared.AvailablePaymentMethods   import AvailablePaymentMethods
from src.Entities.Shared.BillingDetails            import BillingDetails
from src.Entities.Shared.Checkout                  import Checkout
from src.Entities.Shared.CollectionMode            import CollectionMode
from src.Entities.Shared.CustomData                import CustomData
from src.Entities.Shared.CurrencyCode              import CurrencyCode
from src.Entities.Shared.StatusTransaction         import StatusTransaction
from src.Entities.Shared.TransactionOrigin         import TransactionOrigin
from src.Entities.Shared.TransactionPaymentAttempt import TransactionPaymentAttempt

from src.Entities.Transactions.TransactionAdjustment        import TransactionAdjustment
from src.Entities.Transactions.TransactionAdjustmentsTotals import TransactionAdjustmentsTotals
from src.Entities.Transactions.TransactionDetails           import TransactionDetails
from src.Entities.Transactions.TransactionItem              import TransactionItem
from src.Entities.Transactions.TransactionTimePeriod        import TransactionTimePeriod


@dataclass
class TransactionWithIncludes(Entity):
    id:                        str
    status:                    StatusTransaction
    customer_id:               str | None
    address_id:                str | None
    business_id:               str | None
    custom_data:               CustomData | None
    currency_code:             CurrencyCode
    origin:                    TransactionOrigin
    subscription_id:           str | None
    invoice_id:                str | None
    invoice_number:            str | None
    collection_mode:           CollectionMode
    discount_id:               str | None
    billing_details:           BillingDetails | None
    billing_period:            TransactionTimePeriod | None
    items:                     list[TransactionItem]
    details:                   TransactionDetails
    payments:                  list[TransactionPaymentAttempt]
    checkout:                  Checkout | None
    created_at:                datetime
    updated_at:                datetime
    billed_at:                 datetime | None
    address:                   Address | None
    adjustments:               list[TransactionAdjustment]
    adjustments_totals:        TransactionAdjustmentsTotals | None
    business:                  Business | None
    customer:                  Customer | None
    discount:                  Discount | None
    available_payment_methods: list[AvailablePaymentMethods]


    @classmethod
    def from_dict(cls, data: dict) -> TransactionWithIncludes:
        return TransactionWithIncludes(
            id                        = data['id'],
            status                    = StatusTransaction(data['status']),
            customer_id               = data.get('customer_id'),
            address_id                = data.get('address_id'),
            business_id               = data.get('business_id'),
            custom_data               = CustomData(data['custom_data']) if 'custom_data' in data else None,
            currency_code             = CurrencyCode(data['currency_code']),
            origin                    = TransactionOrigin(data['origin']),
            subscription_id           = data.get('subscription_id'),
            invoice_id                = data.get('invoice_id'),
            invoice_number            = data.get('invoice_number'),
            collection_mode           = CollectionMode(data['collection_mode']),
            discount_id               = data.get('discount_id'),
            billing_details           = BillingDetails.from_dict(data['billing_details']) if 'billing_details' in data else None,
            billing_period            = TransactionTimePeriod.from_dict(data['billing_period']) if 'billing_period' in data else None,
            items                     = [TransactionItem.from_dict(item) for item in data.get('items', [])],
            details                   = TransactionDetails.from_dict(data['details']),
            payments                  = [TransactionPaymentAttempt.from_dict(payment) for payment in data.get('payments', [])],
            checkout                  = Checkout.from_dict(data['checkout']) if 'checkout' in data else None,
            created_at                = datetime.fromisoformat(data['created_at']),
            updated_at                = datetime.fromisoformat(data['updated_at']),
            billed_at                 = datetime.fromisoformat(data['billed_at']) if 'billed_at' in data else None,
            address                   = Address.from_dict(data['address']) if 'address' in data else None,
            adjustments               = [TransactionAdjustment.from_dict(adjustment) for adjustment in data.get('adjustments', [])],
            adjustments_totals        = TransactionAdjustmentsTotals.from_dict(data['adjustments_totals']) if 'adjustments_totals' in data else None,
            business                  = Business.from_dict(data['business']) if 'business' in data else None,
            customer                  = Customer.from_dict(data['customer']) if 'customer' in data else None,
            discount                  = Discount.from_dict(data['discount']) if 'discount' in data else None,
            available_payment_methods = [AvailablePaymentMethods(payment_method) for payment_method in data.get('available_payment_methods', [])],
        )
