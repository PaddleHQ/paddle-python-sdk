from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.ApiRoot import RootApi, RootCaller


@dataclass
class RootContext(Entity):
    api: RootApi
    caller: RootCaller

    @staticmethod
    def from_dict(data: dict[str, Any]) -> RootContext:
        return RootContext(
            api=RootApi.from_dict(data["api"]),
            caller=RootCaller.from_dict(data["caller"]),
        )
