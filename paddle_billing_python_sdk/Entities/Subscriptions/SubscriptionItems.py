from __future__  import annotations
from dataclasses import asdict, dataclass


@dataclass
class SubscriptionItems:
    price_id: str
    quantity: int


    @staticmethod
    def from_dict(data: dict) -> SubscriptionItems:
        return SubscriptionItems(
            price_id = data['price_id'],
            quantity = data['quantity'],
        )


    def get_parameters(self) -> dict:
        return asdict(self)
