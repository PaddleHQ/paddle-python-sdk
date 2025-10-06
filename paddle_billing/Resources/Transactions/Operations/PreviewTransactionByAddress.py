from dataclasses import dataclass

from paddle_billing.Operation import Operation
from paddle_billing.Undefined import Undefined
from paddle_billing.Entities.Shared import AddressPreview, CurrencyCode
from paddle_billing.Resources.Transactions.Operations.Preview import (
    TransactionItemPreviewWithPriceId,
    TransactionItemPreviewWithNonCatalogPrice,
)
from paddle_billing.Resources.Transactions.Operations.Discount.TransactionNonCatalogDiscount import (
    TransactionNonCatalogDiscount,
)


@dataclass
class PreviewTransactionByAddress(Operation):
    address: AddressPreview
    items: list[TransactionItemPreviewWithPriceId | TransactionItemPreviewWithNonCatalogPrice]
    customer_id: str | None | Undefined = Undefined()
    currency_code: CurrencyCode | None | Undefined = Undefined()
    discount_id: str | None | Undefined = Undefined()
    ignore_trials: bool | Undefined = Undefined()
    discount: TransactionNonCatalogDiscount | None | Undefined = Undefined()
