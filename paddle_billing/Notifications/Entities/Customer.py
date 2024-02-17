from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from paddle_billing.Notifications.Entities.Entity import Entity
from paddle_billing.Notifications.Entities.Shared import CustomData, ImportMeta, Status


@dataclass
class Customer(Entity):
    id:                str
    name:              str | None
    email:             str
    marketing_consent: bool
    status:            Status
    locale:            str
    created_at:        datetime
    updated_at:        datetime
    custom_data:       CustomData | None = None
    import_meta:       ImportMeta | None = None


    @classmethod
    def from_dict(cls, data: dict) -> Customer:
        return Customer(
            id                = data['id'],
            name              = data.get('name'),
            email             = data['email'],
            marketing_consent = data['marketing_consent'],
            status            = Status(data['status']),
            locale            = data['locale'],
            created_at        = datetime.fromisoformat(data['created_at']),
            updated_at        = datetime.fromisoformat(data['updated_at']),
            custom_data       = CustomData(data['custom_data'])           if data.get('custom_data') else None,
            import_meta       = ImportMeta.from_dict(data['import_meta']) if data.get('import_meta') else None,
        )
