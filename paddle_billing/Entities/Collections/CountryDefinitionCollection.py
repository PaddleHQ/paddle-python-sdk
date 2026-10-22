from __future__ import annotations
from typing import Any

from paddle_billing.Entities.Collections.Collection import Collection
from paddle_billing.Entities.Collections.Paginator import Paginator
from paddle_billing.Entities.CountryDefinition import CountryDefinition


class CountryDefinitionCollection(Collection[CountryDefinition]):
    @classmethod
    def from_list(
        cls, items_data: list[dict[str, Any]], paginator: Paginator | None = None
    ) -> CountryDefinitionCollection:
        items: list[CountryDefinition] = [CountryDefinition.from_dict(item) for item in items_data]

        return CountryDefinitionCollection(items, paginator)
