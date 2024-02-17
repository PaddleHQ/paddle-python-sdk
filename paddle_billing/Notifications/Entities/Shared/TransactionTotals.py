from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Notifications.Entities.Shared.CurrencyCode import CurrencyCode


@dataclass
class TransactionTotals:
    subtotal:          str
    discount:          str
    tax:               str
    total:             str
    credit:            str
    balance:           str
    grand_total:       str | None
    fee:               str | None
    earnings:          str | None
    currency_code:     CurrencyCode
    credit_to_balance: str


    @staticmethod
    def from_dict(data: dict) -> TransactionTotals:
        return TransactionTotals(
            subtotal          = data['subtotal'],
            discount          = data['discount'],
            tax               = data['tax'],
            total             = data['total'],
            credit            = data['credit'],
            balance           = data['balance'],
            grand_total       = data.get('grand_total'),
            fee               = data.get('fee'),
            earnings          = data.get('earnings'),
            currency_code     = CurrencyCode(data['currency_code']),
            credit_to_balance = data['credit_to_balance'],
        )
