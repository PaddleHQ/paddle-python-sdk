from __future__               import annotations
from .CurrencyCodeAdjustments import CurrencyCodeAdjustments
from dataclasses              import dataclass


@dataclass
class Original:
    amount:        str
    currency_code: CurrencyCodeAdjustments


    @staticmethod
    def from_dict(data: dict) -> Original:
        return Original(
            amount        = data['amount'],
            currency_code = CurrencyCodeAdjustments(data['currency_code']),
        )
