from __future__ import annotations
from dataclasses import dataclass
from typing import Any
from urllib.parse import parse_qs, urlparse


@dataclass
class MetricsExplorePagination:
    per_page: int
    next: str
    has_more: bool
    estimated_total: int
    # Explore pages by re-POSTing to `next`, which the SDK can't target, so pass this to explore() instead.
    after: str | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> MetricsExplorePagination:
        return MetricsExplorePagination(
            per_page=data["per_page"],
            next=data["next"],
            has_more=data["has_more"],
            estimated_total=data["estimated_total"],
            after=MetricsExplorePagination._after(data["next"], data["has_more"]),
        )

    @staticmethod
    def _after(next_url: str, has_more: bool) -> str | None:
        if not has_more or not next_url:
            return None

        after = parse_qs(urlparse(next_url).query).get("after")

        return after[0] if after else None
