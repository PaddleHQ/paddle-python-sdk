from __future__  import annotations
from dataclasses import dataclass
from typing      import Optional

from src.Entities.Shared.Card import Card
from src.Entities.Shared.Type import Type


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
