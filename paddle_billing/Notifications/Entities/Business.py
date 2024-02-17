from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from paddle_billing.Notifications.Entities.Entity     import Entity
from paddle_billing.Notifications.Entities.Businesses import BusinessesContacts
from paddle_billing.Notifications.Entities.Shared     import CustomData, ImportMeta, Status


@dataclass
class Business(Entity):
    id:             str
    name:           str
    company_number: str | None
    tax_identifier: str | None
    status:         Status
    contacts:       list[BusinessesContacts]
    created_at:     datetime
    updated_at:     datetime
    custom_data:    CustomData | None = None
    import_meta:    ImportMeta | None = None


    @classmethod
    def from_dict(cls, data: dict) -> Business:
        return Business(
            id             = data['id'],
            name           = data['name'],
            company_number = data.get('company_number'),
            tax_identifier = data.get('tax_identifier'),
            status         = Status(data['status']),
            created_at     = datetime.fromisoformat(data['created_at']),
            updated_at     = datetime.fromisoformat(data['updated_at']),
            contacts       = [BusinessesContacts.from_dict(contact) for contact in data['contacts']],
            custom_data    = CustomData(data['custom_data'])           if data.get('custom_data') else None,
            import_meta    = ImportMeta.from_dict(data['import_meta']) if data.get('import_meta') else None,
        )
