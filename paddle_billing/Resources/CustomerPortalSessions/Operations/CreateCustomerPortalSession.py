from dataclasses import dataclass

from paddle_billing.Operation import Operation


@dataclass
class CreateCustomerPortalSession(Operation):
    subscription_ids: list[str] = (None,)
