from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Entities.Shared.KoreaLocalPaymentMethodType import KoreaLocalPaymentMethodType


@dataclass
class KoreaLocalUnderlyingDetails:
    type: KoreaLocalPaymentMethodType

    @staticmethod
    def from_dict(data: dict[str, Any]) -> KoreaLocalUnderlyingDetails:
        return KoreaLocalUnderlyingDetails(
            type=KoreaLocalPaymentMethodType(data["type"]),
        )
