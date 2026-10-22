from __future__ import annotations
from typing import Any

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator import Paginator
from paddle_billing.Entities.CurrencyDefinition import CurrencyDefinition


class CurrencyDefinitionCollection(Collection[CurrencyDefinition]):
    @classmethod
    def from_list(
        cls, items_data: list[dict[str, Any]], paginator: Paginator | None = None
    ) -> CurrencyDefinitionCollection:
        items: list[CurrencyDefinition] = [CurrencyDefinition.from_dict(item) for item in items_data]

        return CurrencyDefinitionCollection(items, paginator)
