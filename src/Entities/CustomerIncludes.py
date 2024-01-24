from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from src.Entities.Entity import Entity

from src.Entities.Shared.CustomData import CustomData
from src.Entities.Shared.Status     import Status


@dataclass
class CustomerIncludes(Entity):
    id:                str
    name:              str | None
    email:             str
    marketing_consent: bool
    status:            Status
    custom_data:       CustomData | None
    locale:            str
    created_at:        datetime
    updated_at:        datetime


    @classmethod
    def from_dict(cls, data: dict) -> CustomerIncludes:
        return CustomerIncludes(
            id                = data['id'],
            name              = data.get('name'),
            email             = data['email'],
            marketing_consent = data['marketing_consent'],
            status            = Status(data['status']),
            custom_data       = CustomData(data['custom_data']) if data.get('custom_data') else None,
            locale            = data['locale'],
            created_at        = datetime.fromisoformat(data['created_at']),
            updated_at        = datetime.fromisoformat(data['updated_at']),
        )
