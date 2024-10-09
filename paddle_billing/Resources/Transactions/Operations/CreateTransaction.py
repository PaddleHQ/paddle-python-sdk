from dataclasses import dataclass

from paddle_billing.Operation import Operation
from paddle_billing.Undefined import Undefined
from paddle_billing.Entities.Shared import (
    Checkout,
    CollectionMode,
    CurrencyCode,
    CustomData,
    TimePeriod,
    TransactionStatus,
)
from paddle_billing.Entities.Transactions import TransactionCreateItem, TransactionCreateItemWithPrice
from paddle_billing.Resources.Transactions.Operations.Create import CreateBillingDetails


@dataclass
class CreateTransaction(Operation):
    items: list[TransactionCreateItem | TransactionCreateItemWithPrice]
    status: TransactionStatus | Undefined = Undefined()
    customer_id: str | None | Undefined = Undefined()
    address_id: str | None | Undefined = Undefined()
    business_id: str | None | Undefined = Undefined()
    custom_data: CustomData | None | Undefined = Undefined()
    currency_code: CurrencyCode | Undefined = Undefined()
    collection_mode: CollectionMode | Undefined = Undefined()
    discount_id: str | None | Undefined = Undefined()
    billing_details: CreateBillingDetails | None | Undefined = Undefined()
    billing_period: TimePeriod | None | Undefined = Undefined()
    checkout: Checkout | None | Undefined = Undefined()
