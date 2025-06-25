from __future__ import annotations
from dataclasses import dataclass


@dataclass
class SubscriptionCreationItemCreate:
    price_id: str
    quantity: int
