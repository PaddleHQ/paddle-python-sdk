from __future__  import annotations
from dataclasses import dataclass

from paddle_billing_python_sdk.Entities.Shared.Card import Card
from paddle_billing_python_sdk.Entities.Shared.Type import Type


@dataclass
class MethodDetails:
    type: Type
    card: Card | None


    @classmethod
    def from_dict(cls, data: dict) -> MethodDetails:
        return MethodDetails(
            Type(data['type']),
            Card.from_dict(data['card']) if 'card' in data and data['card'] != '' else None,
        )
