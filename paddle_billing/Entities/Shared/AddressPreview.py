from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Shared.CountryCode import CountryCode


@dataclass
class AddressPreview:
    postal_code: str | None
    country_code: CountryCode

    @staticmethod
    def from_dict(data: dict[str, Any]) -> AddressPreview:
        return AddressPreview(
            postal_code=data.get("postal_code"),
            country_code=CountryCode(data["country_code"]),
        )
