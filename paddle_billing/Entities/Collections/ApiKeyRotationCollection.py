from __future__ import annotations
from typing import Any

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator import Paginator
from paddle_billing.Entities.ApiKeyRotation import ApiKeyRotation


class ApiKeyRotationCollection(Collection[ApiKeyRotation]):
    @classmethod
    def from_list(
        cls, items_data: list[dict[str, Any]], paginator: Paginator | None = None
    ) -> ApiKeyRotationCollection:
        items: list[ApiKeyRotation] = [ApiKeyRotation.from_dict(item) for item in items_data]

        return ApiKeyRotationCollection(items, paginator)
