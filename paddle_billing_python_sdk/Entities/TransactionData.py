from __future__  import annotations
from dataclasses import dataclass

from paddle_billing_python_sdk.Entities.Entity import Entity


@dataclass
class TransactionData(Entity):
    url: str


    @classmethod
    def from_dict(cls, data: dict) -> TransactionData:
        return TransactionData(data['url'])

