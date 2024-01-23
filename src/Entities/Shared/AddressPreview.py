from __future__     import annotations
from dataclasses    import dataclass
from .CountryCode   import CountryCode
from typing         import Optional


@dataclass
class AddressPreview:
    postal_code:  Optional[str]
    country_code: CountryCode


    @staticmethod
    def from_dict(data: dict) -> AddressPreview:
        return AddressPreview(
            postal_code  = data.get('postal_code'),
            country_code = CountryCode(data['country_code']),
        )
