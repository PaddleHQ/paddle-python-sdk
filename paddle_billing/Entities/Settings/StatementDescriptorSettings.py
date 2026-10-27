from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Entity import Entity
from paddle_billing.Entities.Settings.StatementDescriptorPreview import StatementDescriptorPreview


@dataclass
class StatementDescriptorSettings(Entity):
    name: str
    preview: StatementDescriptorPreview

    @staticmethod
    def from_dict(data: dict[str, Any]) -> StatementDescriptorSettings:
        return StatementDescriptorSettings(
            name=data["name"],
            preview=StatementDescriptorPreview.from_dict(data["preview"]),
        )
