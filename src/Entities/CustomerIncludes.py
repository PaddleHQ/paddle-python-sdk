from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from src.Entities.Entity import Entity

from src.Entities.Shared.CustomData import CustomData
from src.Entities.Shared.Status     import Status


@dataclass
class CustomerIncludes(Entity):
    id:               str
    name:             str | None
    email:            str
    marketingConsent: bool
    status:           Status
    customData:       CustomData | None
    locale:           str
    createdAt:        datetime
    updatedAt:        datetime


    @classmethod
    def from_dict(cls, data: dict) -> CustomerIncludes:
        return CustomerIncludes(
            id               = data['id'],
            name             = data.get('name'),
            email            = data['email'],
            marketingConsent = data['marketing_consent'],
            status           = Status(data['status']),
            customData       = CustomData(data['custom_data']) if data.get('custom_data') else None,
            locale           = data['locale'],
            createdAt        = datetime.fromisoformat(data['created_at']),
            updatedAt        = datetime.fromisoformat(data['updated_at']),
        )
