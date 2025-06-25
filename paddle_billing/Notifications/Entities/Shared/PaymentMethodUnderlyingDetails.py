from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from paddle_billing.Notifications.Entities.Shared.KoreaLocalUnderlyingDetails import KoreaLocalUnderlyingDetails


@dataclass
class PaymentMethodUnderlyingDetails:
    korea_local: KoreaLocalUnderlyingDetails

    @staticmethod
    def from_dict(data: dict[str, Any]) -> PaymentMethodUnderlyingDetails:
        return PaymentMethodUnderlyingDetails(
            korea_local=KoreaLocalUnderlyingDetails.from_dict(data["korea_local"]),
        )
