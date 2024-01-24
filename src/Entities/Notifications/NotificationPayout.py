from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Entity import Entity

from src.Entities.Notifications.NotificationPayoutStatus import NotificationPayoutStatus

from src.Entities.Shared.CurrencyCodePayouts import CurrencyCodePayouts


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
