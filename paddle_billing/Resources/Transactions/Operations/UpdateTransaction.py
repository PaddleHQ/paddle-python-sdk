from dataclasses import asdict, dataclass

from paddle_billing.Undefined import Undefined
from paddle_billing.Entities.Shared import BillingDetails, Checkout, CollectionMode, CurrencyCode, CustomData, TimePeriod, TransactionStatus
from paddle_billing.Entities.Transactions import TransactionCreateItem, TransactionCreateItemWithPrice


@dataclass
class UpdateTransaction:
    items: list[TransactionCreateItem | TransactionCreateItemWithPrice] = Undefined()
    status: TransactionStatus | Undefined = Undefined()
    customer_id: str | None | Undefined = Undefined()
    address_id: str | None | Undefined = Undefined()
    business_id: str | None | Undefined = Undefined()
    custom_data: CustomData | None | Undefined = Undefined()
    currency_code: CurrencyCode | Undefined = Undefined()
    collection_mode: CollectionMode | Undefined = Undefined()
    discount_id: str | None | Undefined = Undefined()
    billing_details: BillingDetails | None | Undefined = Undefined()
    billing_period: TimePeriod | None | Undefined = Undefined()
    checkout: Checkout | None | Undefined = Undefined()

    def get_parameters(self) -> dict:
        return asdict(self)
