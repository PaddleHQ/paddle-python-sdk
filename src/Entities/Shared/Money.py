from __future__    import annotations
from .CurrencyCode import CurrencyCode
from dataclasses   import dataclass
from typing        import Optional


@dataclass
class Money:
    amount: str
    currencyCode: Optional[CurrencyCode]


    @staticmethod
    def from_dict(data: dict) -> Money:
        currency_code = CurrencyCode(data['currency_code']) \
            if 'currency_code' in data and data['currency_code'] != '' \
            else None

        return Money(
            amount       = data['amount'],
            currencyCode = currency_code,
        )
