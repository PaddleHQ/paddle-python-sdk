from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from src.Entities.Discounts.DiscountStatus import DiscountStatus
from src.Entities.Discounts.DiscountType   import DiscountType

from src.Entities.Entity import Entity

from src.Entities.Shared.CurrencyCode import CurrencyCode


@dataclass
class NotificationDiscount(Entity):
    id:                        str
    status:                    DiscountStatus
    description:               str
    enabledForCheckout:        bool
    code:                      str | None
    type:                      DiscountType
    amount:                    str
    currencyCode:              CurrencyCode | None
    recur:                     bool
    maximumRecurringIntervals: int | None
    usageLimit:                int | None
    restrictTo:                list | None
    expiresAt:                 datetime | None
    createdAt:                 datetime
    updatedAt:                 datetime


    @classmethod
    def from_dict(cls, data: dict) -> NotificationDiscount:
        return NotificationDiscount(
            id                        = data['id'],
            status                    = DiscountStatus(data['status']),
            description               = data['description'],
            enabledForCheckout        = data['enabled_for_checkout'],
            code                      = data.get('code'),
            type                      = DiscountType(data['type']),
            amount                    = data['amount'],
            currencyCode              = CurrencyCode(data['currency_code']) if data.get('currency_code') else None,
            recur                     = data['recur'],
            maximumRecurringIntervals = data.get('maximum_recurring_intervals'),
            usageLimit                = data.get('usage_limit'),
            restrictTo                = data.get('restrict_to'),
            expiresAt                 = datetime.fromisoformat(data['expires_at']) if data.get('expires_at') else None,
            createdAt                 = datetime.fromisoformat(data['created_at']),
            updatedAt                 = datetime.fromisoformat(data['updated_at']),
        )
