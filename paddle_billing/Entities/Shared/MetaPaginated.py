from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Shared.Pagination import Pagination


@dataclass
class MetaPaginated:
    request_id: str
    pagination: Pagination

    @staticmethod
    def from_dict(data: dict[str, Any]) -> MetaPaginated:
        return MetaPaginated(
            request_id=data["request_id"],
            pagination=Pagination.from_dict(data["pagination"]),
        )
