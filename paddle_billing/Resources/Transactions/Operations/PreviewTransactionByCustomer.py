from dataclasses import asdict, dataclass

from paddle_billing.Undefined import Undefined
from paddle_billing.Entities.Shared import CurrencyCode
from paddle_billing.Entities.Transactions import (
    TransactionItemPreviewWithPriceId,
    TransactionItemPreviewWithNonCatalogPrice,
)


@dataclass
class PreviewTransactionByCustomer:
    address_id: str
    customer_id: str
    items: list[TransactionItemPreviewWithPriceId | TransactionItemPreviewWithNonCatalogPrice]
    business_id: str | None | Undefined = Undefined()
    currency_code: CurrencyCode | Undefined = Undefined()
    discount_id: str | None | Undefined = Undefined()
    ignore_trials: bool | Undefined = Undefined()

    def get_parameters(self) -> dict:
        return asdict(self)
