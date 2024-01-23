from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Price import Price

from src.Entities.Subscriptions.SubscriptionProration import SubscriptionProration


@dataclass
class SubscriptionTransactionItem:
    priceId:   str
    price:     Price
    quantity:  int
    proration: SubscriptionProration


    @staticmethod
    def from_dict(data: dict) -> SubscriptionTransactionItem:
        return SubscriptionTransactionItem(
            priceId   = data['price_id'],
            price     = Price.from_dict(data['price']),
            quantity  = data['quantity'],
            proration = SubscriptionProration.from_dict(data['proration']),
        )
