from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from paddle_billing_python_sdk.Entities.Entity import Entity

from paddle_billing_python_sdk.Entities.Shared.CustomData import CustomData
from paddle_billing_python_sdk.Entities.Shared.ImportMeta import ImportMeta
from paddle_billing_python_sdk.Entities.Shared.Status     import Status


@dataclass
class Customer(Entity):
    id:                str
    name:              str | None
    email:             str
    marketing_consent: bool
    status:            Status
    custom_data:       CustomData | None
    locale:            str
    created_at:        datetime
    updated_at:        datetime
    import_meta:       ImportMeta | None


    @classmethod
    def from_dict(cls, data: dict) -> Customer:
        return Customer(
            id                = data['id'],
            name              = data.get('name'),
            email             = data['email'],
            marketing_consent = data['marketing_consent'],
            status            = Status(data['status']),
            custom_data       = CustomData(data['custom_data']) if 'custom_data' in data and data['custom_data'] != '' else None,
            locale            = data['locale'],
            created_at        = datetime.fromisoformat(data['created_at']),
            updated_at        = datetime.fromisoformat(data['updated_at']),
            import_meta       = ImportMeta.from_dict(data['import_meta']) if 'import_meta' in data and data['import_meta'] != '' else None,
        )
