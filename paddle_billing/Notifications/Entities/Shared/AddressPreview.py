from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Notifications.Entities.Shared.CountryCode import CountryCode


@dataclass
class AddressPreview:
    postal_code:  str | None
    country_code: CountryCode


    @staticmethod
    def from_dict(data: dict) -> AddressPreview:
        return AddressPreview(
            postal_code  = data.get('postal_code'),
            country_code = CountryCode(data['country_code']),
        )
