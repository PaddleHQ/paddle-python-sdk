from __future__ import annotations
from typing import Any

from paddle_billing.Entities.Collections.Collection import Collection as Collection
from paddle_billing.Entities.Collections.Paginator import Paginator as Paginator
from paddle_billing.Entities.Verification import Verification as Verification


class VerificationCollection(Collection[Verification]):
    @classmethod
    def from_list(cls, items_data: list[dict[str, Any]], paginator: Paginator | None = None) -> VerificationCollection:
        items: list[Verification] = [Verification.from_dict(item) for item in items_data]

        return VerificationCollection(items, paginator)
