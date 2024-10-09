from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Shared.Duration import Duration
from paddle_billing.Undefined import Undefined


@dataclass
class UpdateBillingDetails:
    payment_terms: Duration | Undefined = Undefined()
    enable_checkout: bool | Undefined = Undefined()
    purchase_order_number: str | Undefined = Undefined()
    additional_information: str | None | Undefined = Undefined()
