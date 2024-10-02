from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Entity import Entity


@dataclass
class TransactionData(Entity):
    url: str

    @staticmethod
    def from_dict(data: dict) -> TransactionData:
        return TransactionData(data["url"])
