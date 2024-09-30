from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Entity import Entity


@dataclass
class CreditNote(Entity):
    url: str


    @staticmethod
    def from_dict(data: dict) -> TransactionData:
        return CreditNote(data['url'])

