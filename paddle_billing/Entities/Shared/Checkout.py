from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class Checkout:
    url: str | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> Checkout:
        return Checkout(url=data.get("url"))
