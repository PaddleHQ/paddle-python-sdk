from __future__                      import annotations
from .Entity                         import Entity
from dataclasses                     import dataclass


@dataclass
class TransactionData(Entity):
    url: str


    @classmethod
    def from_dict(cls, data: dict) -> TransactionData:
        return cls(data['url'])

