from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.Notifications.Entities.Shared.Duration import Duration


@dataclass
class BillingDetails:
    enable_checkout: bool
    payment_terms: Duration
    purchase_order_number: str | None = None
    additional_information: str | None = None

    @staticmethod
    def from_dict(data: dict) -> BillingDetails:
        return BillingDetails(
            enable_checkout=data["enable_checkout"],
            payment_terms=Duration.from_dict(data["payment_terms"]),
            purchase_order_number=data.get("purchase_order_number"),
            additional_information=data.get("additional_information"),
        )
