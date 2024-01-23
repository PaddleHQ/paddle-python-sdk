from __future__  import annotations
from dataclasses import dataclass


@dataclass
class SubscriptionUpdateItem:
    priceId:  str
    quantity: int


    @staticmethod
    def from_dict(data: dict) -> SubscriptionUpdateItem:
        return SubscriptionUpdateItem(
            priceId  = data['price_id'],
            quantity = data['quantity']
        )
