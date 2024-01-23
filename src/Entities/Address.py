from __future__          import annotations
from .Entity             import Entity
from .Shared.CountryCode import CountryCode
from .Shared.CustomData  import CustomData
from .Shared.Status      import Status
from dataclasses         import dataclass
from datetime            import datetime
from typing              import Optional


@dataclass
class Address(Entity):
    id:           str
    description:  Optional[str]
    first_line:   Optional[str]
    second_line:  Optional[str]
    city:         Optional[str]
    postal_code:  Optional[str]
    region:       Optional[str]
    country_code: CountryCode
    custom_data:  Optional[CustomData]
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
