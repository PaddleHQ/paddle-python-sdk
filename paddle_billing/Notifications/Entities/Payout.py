from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Notifications.Entities.Entity  import Entity
from paddle_billing.Notifications.Entities.Payouts import PayoutStatus
from paddle_billing.Notifications.Entities.Shared  import CurrencyCodePayouts


@dataclass
class Payout(Entity):
    amount:        str
    currency_code: CurrencyCodePayouts
    id:            str
    status:        PayoutStatus


    @classmethod
    def from_dict(cls, data: dict) -> Payout:
        return Payout(
            amount        = data['amount'],
            id            = data['id'],
            status        = PayoutStatus(data['status']),
            currency_code = CurrencyCodePayouts(data['currency_code']),
        )
