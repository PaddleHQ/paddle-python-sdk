from __future__  import annotations
from dataclasses import dataclass


@dataclass
class SubscriptionUpdateItem:
    price_id: str
    quantity: int


    @staticmethod
    def from_dict(data: dict) -> SubscriptionUpdateItem:
        return SubscriptionUpdateItem(
            price_id = data['price_id'],
            quantity = data['quantity'],
        )
