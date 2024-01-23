from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime
from typing      import Optional, List

from src.Entities.Entity import Entity

from src.Entities.Shared.Contacts   import Contacts
from src.Entities.Shared.CustomData import CustomData
from src.Entities.Shared.Status     import Status


@dataclass
class Business(Entity):
    id:            str
    name:          str
    companyNumber: Optional[str]
    taxIdentifier: Optional[str]
    status:        Status
    contacts:      List[Contacts]
    createdAt:     datetime
    updatedAt:     datetime
    customData:    Optional[CustomData]


    @classmethod
    def from_dict(cls, data: dict) -> Business:
        return cls(
            id            = data['id'],
            name          = data['name'],
            companyNumber = data.get('company_number'),
            taxIdentifier = data.get('tax_identifier'),
            status        = Status(data['status']),
            contacts      = [Contacts.from_dict(contact) for contact in data['contacts']],
            createdAt     = datetime.fromisoformat(data['created_at']),
            updatedAt     = datetime.fromisoformat(data['updated_at']),
            customData    = CustomData(data['custom_data']) if 'custom_data' in data else None
        )
