from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from paddle_billing.Undefined import Undefined
from paddle_billing.Notifications.Entities.Reports import ReportFilter, ReportStatus, ReportType
from paddle_billing.Notifications.Entities.Simulations.SimulationEntity import SimulationEntity


@dataclass
class Report(SimulationEntity):
    id: str | Undefined = Undefined()
    status: ReportStatus | Undefined = Undefined()
    rows: int | None | Undefined = Undefined()
    type: ReportType | Undefined = Undefined()
    filters: list[ReportFilter] | Undefined = Undefined()
    expires_at: datetime | None | Undefined = Undefined()
    created_at: datetime | Undefined = Undefined()
    updated_at: datetime | Undefined = Undefined()

    @staticmethod
    def from_dict(data: dict[str, Any]) -> Report:
        return Report(
            id=data.get("id", Undefined()),
            status=ReportStatus(data["status"]) if data.get("status") else Undefined(),
            rows=data.get("rows", Undefined()),
            type=ReportType(data["type"]) if data.get("type") else Undefined(),
            filters=(
                [ReportFilter.from_dict(a_filter) for a_filter in data.get("filters", [])]
                if data.get("filters") is not None
                else data.get("filters", Undefined())
            ),
            expires_at=(
                datetime.fromisoformat(data["expires_at"])
                if data.get("expires_at")
                else data.get("expires_at", Undefined())
            ),
            created_at=(
                datetime.fromisoformat(data["created_at"])
                if data.get("created_at")
                else data.get("created_at", Undefined())
            ),
            updated_at=(
                datetime.fromisoformat(data["updated_at"])
                if data.get("updated_at")
                else data.get("updated_at", Undefined())
            ),
        )
