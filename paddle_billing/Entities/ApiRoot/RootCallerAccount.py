from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class RootCallerAccount:
    id: str
    name: str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> RootCallerAccount:
        return RootCallerAccount(
            id=data["id"],
            name=data["name"],
        )
