from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Shared.CurrencyCode import CurrencyCode


@dataclass
class AdjustmentTotals:
    subtotal:      str
    tax:           str
    total:         str
    fee:           str
    earnings:      str
    currency_code: CurrencyCode


    @staticmethod
    def from_dict(data: dict) -> AdjustmentTotals:
        return AdjustmentTotals(
            subtotal      = data['subtotal'],
            tax           = data['tax'],
            total         = data['total'],
            fee           = data['fee'],
            earnings      = data['earnings'],
            currency_code = CurrencyCode(data['currency_code']),
        )
