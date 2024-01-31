from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Shared.CurrencyCode import CurrencyCode

from paddle_billing.Entities.Transactions.TransactionBreakdown import TransactionBreakdown


@dataclass
class TransactionAdjustmentsTotals:
    subtotal:      str
    tax:           str
    total:         str
    fee:           str
    earnings:      str
    breakdown:     TransactionBreakdown
    currency_code: CurrencyCode


    @staticmethod
    def from_dict(data: dict) -> TransactionAdjustmentsTotals:
        return TransactionAdjustmentsTotals(
            subtotal      = data['subtotal'],
            tax           = data['tax'],
            total         = data['total'],
            fee           = data['fee'],
            earnings      = data['earnings'],
            breakdown     = TransactionBreakdown.from_dict(data['breakdown']),
            currency_code = CurrencyCode(data['currency_code']),
        )
