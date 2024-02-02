from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Entity        import Entity
from paddle_billing.Entities.Notifications import NotificationPayoutStatus
from paddle_billing.Entities.Shared        import CurrencyCodePayouts


@dataclass
class NotificationPayout(Entity):
    id:            str
    status:        NotificationPayoutStatus
    amount:        str
    currency_code: CurrencyCodePayouts


    @classmethod
    def from_dict(cls, data: dict) -> NotificationPayout:
        return NotificationPayout(
            id            = data['id'],
            status        = NotificationPayoutStatus(data['status']),
            amount        = data['amount'],
            currency_code = CurrencyCodePayouts(data['currency_code']),
        )
