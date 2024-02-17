from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Notifications.Entities.Shared.CurrencyCode import CurrencyCode


@dataclass
class Money:
    """
    https://developer.paddle.com/api-reference/about/data-types#money
    When specifying the amount, specify it with the lowest denomination of the currency included. For example,
    $420.69USD would be called with Money('42069', CurrencyCode('USD'))
    """
    amount:        str
    currency_code: CurrencyCode | None


    def __post_init__(self):
        if any(substring in self.amount for substring in [',', '.']):
            raise ValueError('Money amount should not contain decimals or commas')


    @staticmethod
    def from_dict(data: dict) -> Money:
        return Money(
            amount        = data['amount'],
            currency_code = CurrencyCode(data['currency_code']) if data.get('currency_code') else None,
        )
