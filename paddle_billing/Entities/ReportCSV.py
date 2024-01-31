from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Entity import Entity


@dataclass
class ReportCSV(Entity):
    url: str

    @classmethod
    def from_dict(cls, data: dict) -> ReportCSV:
        return ReportCSV(url=data['url'])
