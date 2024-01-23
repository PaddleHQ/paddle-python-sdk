from __future__  import annotations
from dataclasses import dataclass


@dataclass
class SubscriptionItems:
    priceId:  str
    quantity: int


    @staticmethod
    def from_dict(data: dict) -> SubscriptionItems:
        return SubscriptionItems(
            priceId  = data['price_id'],
            quantity = data['quantity'],
        )
