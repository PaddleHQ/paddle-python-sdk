from __future__ import annotations

from paddle_billing.Entities.DiscountGroups import DiscountGroupStatus
from .Entity import Entity
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Entities.Shared import ImportMeta


@dataclass
class DiscountGroup(Entity):
    id: str
    name: str
    status: DiscountGroupStatus
    created_at: datetime
    updated_at: datetime
    import_meta: ImportMeta | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> DiscountGroup:
        return DiscountGroup(
            id=data["id"],
            name=data["name"],
            status=DiscountGroupStatus(data["status"]),
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
            import_meta=ImportMeta.from_dict(data["import_meta"]) if data.get("import_meta") else None,
        )
