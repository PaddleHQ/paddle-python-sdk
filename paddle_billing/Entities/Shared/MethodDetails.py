from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Shared.Card              import Card
from paddle_billing.Entities.Shared.PaymentMethodType import PaymentMethodType


@dataclass
class MethodDetails:
    type: PaymentMethodType
    card: Card | None


    @classmethod
    def from_dict(cls, data: dict) -> MethodDetails:
        return MethodDetails(
            PaymentMethodType(data['type']),
            Card.from_dict(data['card']) if data.get('card') else None,
        )
