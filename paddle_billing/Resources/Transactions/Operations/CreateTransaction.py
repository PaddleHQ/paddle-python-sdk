from dataclasses import asdict, dataclass

from paddle_billing.Undefined import Undefined

from paddle_billing.Entities.Shared.BillingDetails    import BillingDetails
from paddle_billing.Entities.Shared.Checkout          import Checkout
from paddle_billing.Entities.Shared.CollectionMode    import CollectionMode
from paddle_billing.Entities.Shared.CurrencyCode      import CurrencyCode
from paddle_billing.Entities.Shared.CustomData        import CustomData
from paddle_billing.Entities.Shared.StatusTransaction import StatusTransaction

from paddle_billing.Entities.Transactions.TransactionCreateItem          import TransactionCreateItem
from paddle_billing.Entities.Transactions.TransactionCreateItemWithPrice import TransactionCreateItemWithPrice
from paddle_billing.Entities.Transactions.TransactionTimePeriod          import TransactionTimePeriod



@dataclass
class CreateTransaction:
    items:           list[TransactionCreateItem   | TransactionCreateItemWithPrice] = Undefined()
    status:          StatusTransaction            | Undefined                       = Undefined()
    customer_id:     str                   | None | Undefined                       = Undefined()
    address_id:      str                   | None | Undefined                       = Undefined()
    business_id:     str                   | None | Undefined                       = Undefined()
    custom_data:     CustomData            | None | Undefined                       = Undefined()
    currency_code:   CurrencyCode                 | Undefined                       = Undefined()
    collection_mode: CollectionMode               | Undefined                       = Undefined()
    discount_id:     str                   | None | Undefined                       = Undefined()
    billing_details: BillingDetails        | None | Undefined                       = Undefined()
    billing_period:  TransactionTimePeriod | None | Undefined                       = Undefined()
    checkout:        Checkout              | None | Undefined                       = Undefined()


    def get_parameters(self) -> dict:
        return asdict(self)
