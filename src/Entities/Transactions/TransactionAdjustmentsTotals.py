from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Shared.CurrencyCode import CurrencyCode

from src.Entities.Transactions.TransactionBreakdown import TransactionBreakdown


@dataclass
class TransactionAdjustmentsTotals:
    subtotal:     str
    tax:          str
    total:        str
    fee:          str
    earnings:     str
    breakdown:    TransactionBreakdown
    currencyCode: CurrencyCode


    @classmethod
    def from_dict(cls, data: dict) -> TransactionAdjustmentsTotals:
        return TransactionAdjustmentsTotals(
            subtotal     = data['subtotal'],
            tax          = data['tax'],
            total        = data['total'],
            fee          = data['fee'],
            earnings     = data['earnings'],
            breakdown    = TransactionBreakdown.from_dict(data['breakdown']),
            currencyCode = CurrencyCode(data['currency_code']),
        )
