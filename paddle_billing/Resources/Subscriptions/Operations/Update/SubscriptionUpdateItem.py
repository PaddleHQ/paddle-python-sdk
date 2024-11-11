from __future__ import annotations
from dataclasses import dataclass
from paddle_billing.Undefined import Undefined


@dataclass
class SubscriptionUpdateItem:
    price_id: str
    quantity: int | Undefined = Undefined()
