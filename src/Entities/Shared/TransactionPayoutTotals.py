from __future__           import annotations
from .CurrencyCodePayouts import CurrencyCodePayouts
from dataclasses          import dataclass
from typing               import Optional


@dataclass
class TransactionPayoutTotals:
    subtotal:       str
    discount:       str
    tax:            str
    total:          str
    credit:         str
    balance:        str
    grand_total:    str
    fee:            Optional[str]
    earnings:       Optional[str]
    currency_code:  CurrencyCodePayouts


    @staticmethod
    def from_dict(data: dict) -> TransactionPayoutTotals:
        return TransactionPayoutTotals(
            subtotal        = data['subtotal'],
            discount        = data['discount'],
            tax             = data['tax'],
            total           = data['total'],
            credit          = data['credit'],
            balance         = data['balance'],
            grand_total     = data['grand_total'],
            fee             = data.get('fee'),
            earnings        = data.get('earnings'),
            currency_code   = CurrencyCodePayouts(data['currency_code']),
        )
