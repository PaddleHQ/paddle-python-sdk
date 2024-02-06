from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Price                               import Price
from paddle_billing.Entities.Subscriptions.SubscriptionProration import SubscriptionProration


@dataclass
class SubscriptionTransactionItem:
    price_id:  str
    price:     Price
    quantity:  int
    proration: SubscriptionProration


    @staticmethod
    def from_dict(data: dict) -> SubscriptionTransactionItem:
        return SubscriptionTransactionItem(
            price_id  = data['price_id'],
            price     = Price.from_dict(data['price']),
            quantity  = data['quantity'],
            proration = SubscriptionProration.from_dict(data['proration']),
        )
