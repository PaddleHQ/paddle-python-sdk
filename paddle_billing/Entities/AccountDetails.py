from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Entity import Entity


@dataclass
class AccountDetails(Entity):
    id: str
    legacy_id: str | None
    legal_name: str | None
    display_name: str | None
    website: str | None
    email: str | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> AccountDetails:
        return AccountDetails(
            id=data["id"],
            legacy_id=data["legacy_id"],
            legal_name=data["legal_name"],
            display_name=data["display_name"],
            website=data["website"],
            email=data["email"],
        )
