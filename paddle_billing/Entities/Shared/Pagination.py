from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class Pagination:
    per_page: int
    next: str
    has_more: bool
    estimated_total: int

    @staticmethod
    def from_dict(data: dict[str, Any]) -> Pagination:
        return Pagination(
            per_page=data["per_page"],
            next=data["next"],
            has_more=data["has_more"],
            estimated_total=data["estimated_total"],
        )
