from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class BusinessesContacts:
    name: str
    email: str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> BusinessesContacts:
        return BusinessesContacts(
            name=data["name"],
            email=data["email"],
        )
