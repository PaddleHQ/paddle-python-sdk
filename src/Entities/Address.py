from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from src.Entities.Entity import Entity

from src.Entities.Shared.CountryCode import CountryCode
from src.Entities.Shared.CustomData  import CustomData
from src.Entities.Shared.Status      import Status


@dataclass
class Address(Entity):
    id:           str
    description:  str | None
    first_line:   str | None
    second_line:  str | None
    city:         str | None
    postal_code:  str | None
    region:       str | None
    country_code: CountryCode
    custom_data:  CustomData | None
    status:       Status
    created_at:   datetime
    updated_at:   datetime


    @classmethod
    def from_dict(cls, data: dict) -> Address:
        return Address(
            id           = data['id'],
            description  = data.get('description'),
            first_line   = data.get('first_line'),
            second_line  = data.get('second_line'),
            city         = data.get('city'),
            postal_code  = data.get('postal_code'),
            region       = data.get('region'),
            country_code = CountryCode(data['country_code']),
            custom_data  = CustomData(data['custom_data']) if 'custom_data' in data else None,
            status       = Status(data['status']),
            created_at   = datetime.fromisoformat(data['created_at']),
            updated_at   = datetime.fromisoformat(data['updated_at']),
        )
