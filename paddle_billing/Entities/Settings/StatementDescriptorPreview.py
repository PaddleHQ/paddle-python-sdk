from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class StatementDescriptorPreview:
    default: str
    paypal: str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> StatementDescriptorPreview:
        return StatementDescriptorPreview(
            default=data["default"],
            paypal=data["paypal"],
        )
