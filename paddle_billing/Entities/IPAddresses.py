from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Entity import Entity


@dataclass
class IPAddresses(Entity):
    ipv4_cidrs: list[str] | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> IPAddresses:
        return IPAddresses(
            ipv4_cidrs=data["ipv4_cidrs"],
        )
