from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from src.Entities.Entity import Entity

from src.Entities.Reports.ReportFilters import ReportFilters
from src.Entities.Reports.ReportStatus  import ReportStatus
from src.Entities.Reports.ReportType    import ReportType


@dataclass
class Report(Entity):
    id:        str
    status:    ReportStatus
    rows:      int | None
    type:      ReportType
    filters:   list[ReportFilters]
    expiresAt: datetime | None
    createdAt: datetime
    updatedAt: datetime


    @classmethod
    def from_dict(cls, data: dict) -> Report:
        return Report(
            id        = data['id'],
            status    = ReportStatus(data['status']),
            rows      = data.get('rows'),
            type      = ReportType(data['type']),
            filters   = [ReportFilters.from_dict(a_filter) for a_filter in data.get('filters', [])],
            expiresAt = datetime.fromisoformat(data['expires_at']) if 'expires_at' in data else None,
            createdAt = datetime.fromisoformat(data['created_at']),
            updatedAt = datetime.fromisoformat(data['updated_at']),
        )
