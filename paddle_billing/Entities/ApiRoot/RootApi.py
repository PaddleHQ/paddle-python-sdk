from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.ApiRoot.RootEnvironment import RootEnvironment


@dataclass
class RootApi:
    name: str
    version: str
    environment: RootEnvironment
    documentation_url: str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> RootApi:
        return RootApi(
            name=data["name"],
            version=data["version"],
            environment=RootEnvironment(data["environment"]),
            documentation_url=data["documentation_url"],
        )
