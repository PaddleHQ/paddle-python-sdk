from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Entity      import Entity
from paddle_billing.Entities.Shared      import CurrencyCode
from paddle_billing.Entities.Adjustments import AdjustmentCustomerBalance


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
