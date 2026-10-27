from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.ApiRoot.RootAuthType import RootAuthType
from paddle_billing.Entities.ApiRoot.RootCallerAccount import RootCallerAccount


@dataclass
class RootCaller:
    auth_type: RootAuthType | None
    account: RootCallerAccount | None
    permissions: list[str]

    @staticmethod
    def from_dict(data: dict[str, Any]) -> RootCaller:
        return RootCaller(
            auth_type=RootAuthType(data["auth_type"]) if data["auth_type"] is not None else None,
            account=RootCallerAccount.from_dict(data["account"]) if data["account"] is not None else None,
            permissions=list(data["permissions"]),
        )
