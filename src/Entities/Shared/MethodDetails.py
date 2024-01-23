from __future__  import annotations
from .Card       import Card
from .Type       import Type
from dataclasses import dataclass
from typing      import Optional


@dataclass
class MethodDetails:
    type: Type
    card: Optional[Card]


    @classmethod
    def from_dict(cls, data: dict) -> MethodDetails:
        return cls(
            Type(data['type']),
            Card.from_dict(data['card']) if 'card' in data and data['card'] != '' else None,
        )
