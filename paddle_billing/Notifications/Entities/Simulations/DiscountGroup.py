from __future__ import annotations

from paddle_billing.Notifications.Entities.DiscountGroups import DiscountGroupStatus
from paddle_billing.Notifications.Entities.Simulations.SimulationEntity import SimulationEntity
from paddle_billing.Undefined import Undefined

from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Entities.Shared import ImportMeta


@dataclass
class DiscountGroup(SimulationEntity):
    id: str | Undefined = Undefined()
    name: str | Undefined = Undefined()
    status: DiscountGroupStatus | Undefined = Undefined()
    created_at: datetime | Undefined = Undefined()
    updated_at: datetime | Undefined = Undefined()
    import_meta: ImportMeta | None | Undefined = Undefined()

    @staticmethod
    def from_dict(data: dict[str, Any]) -> DiscountGroup:
        return DiscountGroup(
            id=data.get("id", Undefined()),
            name=data.get("name", Undefined()),
            status=DiscountGroupStatus(data["status"]) if data.get("status") else Undefined(),
            created_at=datetime.fromisoformat(data["created_at"]) if data.get("created_at") else Undefined(),
            updated_at=datetime.fromisoformat(data["updated_at"]) if data.get("updated_at") else Undefined(),
            import_meta=(
                ImportMeta.from_dict(data["import_meta"])
                if isinstance(data.get("import_meta"), dict)
                else data.get("import_meta", Undefined())
            ),
        )
