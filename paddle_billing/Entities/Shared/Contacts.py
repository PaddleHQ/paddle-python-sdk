from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class Contacts:
    name: str
    email: str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> Contacts:
        return Contacts(
            name=data["name"],
            email=data["email"],
        )
