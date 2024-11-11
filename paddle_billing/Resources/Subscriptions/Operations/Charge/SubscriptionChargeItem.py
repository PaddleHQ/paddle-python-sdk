from __future__ import annotations
from dataclasses import dataclass


@dataclass
class SubscriptionChargeItem:
    price_id: str
    quantity: int
