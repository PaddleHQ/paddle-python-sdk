from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from paddle_billing_python_sdk.Entities.Discounts.DiscountStatus import DiscountStatus
from paddle_billing_python_sdk.Entities.Discounts.DiscountType   import DiscountType

from paddle_billing_python_sdk.Entities.Entity import Entity

from paddle_billing_python_sdk.Entities.Shared.CurrencyCode import CurrencyCode


@dataclass
class NotificationDiscount(Entity):
    id:                          str
    status:                      DiscountStatus
    description:                 str
    enabled_for_checkout:        bool
    code:                        str | None
    type:                        DiscountType
    amount:                      str
    currency_code:               CurrencyCode | None
    recur:                       bool
    maximum_recurring_intervals: int | None
    usage_limit:                 int | None
    restrict_to:                 list | None
    expires_at:                  datetime | None
    created_at:                  datetime
    updated_at:                  datetime


    @classmethod
    def from_dict(cls, data: dict) -> NotificationDiscount:
        return NotificationDiscount(
            id                          = data['id'],
            status                      = DiscountStatus(data['status']),
            description                 = data['description'],
            enabled_for_checkout        = data['enabled_for_checkout'],
            code                        = data.get('code'),
            type                        = DiscountType(data['type']),
            amount                      = data['amount'],
            currency_code               = CurrencyCode(data['currency_code']) if data.get('currency_code') else None,
            recur                       = data['recur'],
            maximum_recurring_intervals = data.get('maximum_recurring_intervals'),
            usage_limit                 = data.get('usage_limit'),
            restrict_to                 = data.get('restrict_to'),
            expires_at                  = datetime.fromisoformat(data['expires_at']) if data.get('expires_at') else None,
            created_at                  = datetime.fromisoformat(data['created_at']),
            updated_at                  = datetime.fromisoformat(data['updated_at']),
        )
