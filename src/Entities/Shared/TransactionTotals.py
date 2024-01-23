from __future__  import annotations
from dataclasses import dataclass
from typing      import Optional

from src.Entities.Shared.CurrencyCode import CurrencyCode


@dataclass
class TransactionTotals:
    subtotal:      str
    discount:      str
    tax:           str
    total:         str
    credit:        str
    balance:       str
    grand_total:   Optional[str]
    fee:           Optional[str]
    earnings:      Optional[str]
    currency_code: CurrencyCode


    @staticmethod
    def from_dict(data: dict) -> TransactionTotals:
        return TransactionTotals(
            subtotal      = data['subtotal'],
            discount      = data['discount'],
            tax           = data['tax'],
            total         = data['total'],
            credit        = data['credit'],
            balance       = data['balance'],
            grand_total   = data.get('grand_total'),
            fee           = data.get('fee'),
            earnings      = data.get('earnings'),
            currency_code = CurrencyCode(data['currency_code']),
        )
