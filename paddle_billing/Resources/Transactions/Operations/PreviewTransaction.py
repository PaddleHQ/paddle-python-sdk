from dataclasses import asdict, dataclass

from paddle_billing.Undefined             import Undefined
from paddle_billing.Entities.Shared       import AddressPreview, CollectionMode, CurrencyCode
from paddle_billing.Entities.Transactions import TransactionItemPreviewWithPriceId, TransactionItemPreviewWithNonCatalogPrice



@dataclass
class PreviewTransaction:
    items:               list[TransactionItemPreviewWithPriceId | TransactionItemPreviewWithNonCatalogPrice]
    customer_id:         str            | None | Undefined = Undefined()
    address_id:          str            | None | Undefined = Undefined()
    business_id:         str            | None | Undefined = Undefined()
    currency_code:       CurrencyCode          | Undefined = Undefined()
    collection_mode:     CollectionMode        | Undefined = Undefined()
    discount_id:         str            | None | Undefined = Undefined()
    customer_ip_address: str            | None | Undefined = Undefined()
    address:             AddressPreview | None | Undefined = Undefined()
    ignore_trials:       bool                  | Undefined = Undefined()


    def get_parameters(self) -> dict:
        return asdict(self)
