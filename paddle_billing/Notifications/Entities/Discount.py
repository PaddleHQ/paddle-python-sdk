from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from paddle_billing.Notifications.Entities.Discounts import DiscountStatus, DiscountType
from paddle_billing.Notifications.Entities.Entity    import Entity
from paddle_billing.Notifications.Entities.Shared    import CurrencyCode, CustomData, ImportMeta


@dataclass
class Discount(Entity):
    amount:                      str
    created_at:                  datetime
    description:                 str
    enabled_for_checkout:        bool
    id:                          str
    recur:                       bool
    status:                      DiscountStatus
    type:                        DiscountType
    updated_at:                  datetime
    code:                        str          | None = None
    currency_code:               CurrencyCode | None = None
    custom_data:                 CustomData   | None = None
    expires_at:                  datetime     | None = None
    import_meta:                 ImportMeta   | None = None
    maximum_recurring_intervals: int          | None = None
    restrict_to:                 list         | None = None
    usage_limit:                 int          | None = None


    @classmethod
    def from_dict(cls, data: dict) -> Discount:
        return Discount(
            amount                      = data['amount'],
            code                        = data.get('code'),
            created_at                  = datetime.fromisoformat(data['created_at']),
            description                 = data['description'],
            enabled_for_checkout        = data['enabled_for_checkout'],
            id                          = data['id'],
            maximum_recurring_intervals = data.get('maximum_recurring_intervals'),
            usage_limit                 = data.get('usage_limit'),
            recur                       = data['recur'],
            restrict_to                 = data.get('restrict_to'),
            status                      = DiscountStatus(data['status']),
            type                        = DiscountType(data['type']),
            updated_at                  = datetime.fromisoformat(data['updated_at']),
            currency_code               = CurrencyCode(data['currency_code'])        if data.get('currency_code') else None,
            custom_data                 = CustomData(data['custom_data'])            if data.get('custom_data')   else None,
            expires_at                  = datetime.fromisoformat(data['expires_at']) if data.get('expires_at')    else None,
            import_meta                 = ImportMeta.from_dict(data['import_meta'])  if data.get('import_meta')   else None,
        )
