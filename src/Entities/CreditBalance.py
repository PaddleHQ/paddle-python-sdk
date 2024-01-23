from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Entity import Entity

from src.Entities.Shared.CurrencyCode import CurrencyCode

from src.Entities.Adjustments.AdjustmentCustomerBalance import AdjustmentCustomerBalance


@dataclass
class CreditBalance(Entity):
    customerId:   str
    currencyCode: CurrencyCode
    balance:      AdjustmentCustomerBalance


    @classmethod
    def from_dict(cls, data: dict) -> CreditBalance:
        return CreditBalance(
            customerId   = data['customer_id'],
            currencyCode = CurrencyCode(data['currency_code']),
            balance      = AdjustmentCustomerBalance.from_dict(data['balance']),
        )
