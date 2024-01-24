from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Entity import Entity

from src.Entities.Shared.CurrencyCode import CurrencyCode

from src.Entities.Adjustments.AdjustmentCustomerBalance import AdjustmentCustomerBalance


@dataclass
class CreditBalance(Entity):
    customer_id:   str
    currency_code: CurrencyCode
    balance:       AdjustmentCustomerBalance


    @classmethod
    def from_dict(cls, data: dict) -> CreditBalance:
        return CreditBalance(
            customer_id   = data['customer_id'],
            currency_code = CurrencyCode(data['currency_code']),
            balance       = AdjustmentCustomerBalance.from_dict(data['balance']),
        )
