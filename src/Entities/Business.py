from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from src.Entities.Entity import Entity

from src.Entities.Shared.Contacts   import Contacts
from src.Entities.Shared.CustomData import CustomData
from src.Entities.Shared.ImportMeta import ImportMeta
from src.Entities.Shared.Status     import Status


@dataclass
class Business(Entity):
    id:            str
    name:          str
    company_number: str | None
    tax_identifier: str | None
    status:        Status
    contacts:      list[Contacts]
    created_at:     datetime
    updated_at:     datetime
    custom_data:    CustomData | None
    import_meta:   ImportMeta | None


    @classmethod
    def from_dict(cls, data: dict) -> Business:
        return Business(
            id             = data['id'],
            name           = data['name'],
            company_number = data.get('company_number'),
            tax_identifier = data.get('tax_identifier'),
            status         = Status(data['status']),
            contacts       = [Contacts.from_dict(contact) for contact in data['contacts']],
            created_at     = datetime.fromisoformat(data['created_at']),
            updated_at     = datetime.fromisoformat(data['updated_at']),
            custom_data    = CustomData(data['custom_data'])           if 'custom_data' in data else None,
            import_meta    = ImportMeta.from_dict(data['import_meta']) if 'import_meta' in data else None,
        )
