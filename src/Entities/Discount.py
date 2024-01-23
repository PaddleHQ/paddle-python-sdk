from __future__  import annotations
from .Entity     import Entity
from dataclasses import dataclass
from datetime    import datetime
from typing      import Optional, List

from src.Entities.Discounts.DiscountStatus import DiscountStatus
from src.Entities.Discounts.DiscountType   import DiscountType

from src.Entities.Shared.CurrencyCode import CurrencyCode


@dataclass
class Discount(Entity):
    id:                        str
    status:                    DiscountStatus
    description:               str
    enabledForCheckout:        bool
    code:                      Optional[str]
    type:                      DiscountType
    amount:                    str
    currencyCode:              Optional[CurrencyCode]
    recur:                     bool
    maximumRecurringIntervals: Optional[int]
    usageLimit:                Optional[int]
    restrictTo:                Optional[List[str]]
    expiresAt:                 Optional[datetime]
    timesUsed:                 int
    createdAt:                 datetime
    updatedAt:                 datetime


    @classmethod
    def from_dict(cls, data: dict) -> Discount:
        return Discount(
            id                        = data['id'],
            status                    = DiscountStatus(data['status']),
            description               = data['description'],
            enabledForCheckout        = data['enabled_for_checkout'],
            code                      = data.get('code'),
            type                      = DiscountType(data['type']),
            amount                    = data['amount'],
            currencyCode              = CurrencyCode(data['currency_code']) if 'currency_code' in data else None,
            recur                     = data['recur'],
            maximumRecurringIntervals = data.get('maximum_recurring_intervals'),
            usageLimit                = data.get('usage_limit'),
            restrictTo                = data.get('restrict_to'),
            expiresAt                 = datetime.fromisoformat(data['expires_at']) if 'expires_at' in data else None,
            timesUsed                 = data['times_used'],
            createdAt                 = datetime.fromisoformat(data['created_at']),
            updatedAt                 = datetime.fromisoformat(data['updated_at'])
        )
