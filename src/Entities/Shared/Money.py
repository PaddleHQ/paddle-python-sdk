from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Shared.CurrencyCode import CurrencyCode


@dataclass
class Money:
    amount:        str
    currency_code: CurrencyCode | None


    @staticmethod
    def from_dict(data: dict) -> Money:
        return Money(
            amount        = data['amount'],
            currency_code = CurrencyCode(data['currency_code']) if 'currency_code' in data else None,
        )
