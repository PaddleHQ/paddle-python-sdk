from __future__ import annotations
from dataclasses import dataclass
from typing import Any
from urllib.parse import parse_qs, urlparse

from paddle_billing.Entities.Metrics.MetricsExploreData import MetricsExploreData
from paddle_billing.Entities.Shared import MetaPaginated


@dataclass
class MetricsExploreResponse:
    data: MetricsExploreData
    meta: MetaPaginated

    @property
    def has_more(self) -> bool:
        return self.meta.pagination.has_more

    @property
    def next_cursor(self) -> str | None:
        """The `after` value to pass to the next run_explore_query call, or None on the last page."""
        if not self.has_more or not self.meta.pagination.next:
            return None

        after = parse_qs(urlparse(self.meta.pagination.next).query).get("after")

        return after[0] if after else None

    @staticmethod
    def from_dict(body: dict[str, Any]) -> MetricsExploreResponse:
        return MetricsExploreResponse(
            data=MetricsExploreData.from_dict(body["data"]),
            meta=MetaPaginated.from_dict(body["meta"]),
        )
