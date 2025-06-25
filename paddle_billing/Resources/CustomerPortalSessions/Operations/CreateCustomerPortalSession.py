from dataclasses import dataclass

from paddle_billing.Operation import Operation
from paddle_billing.Undefined import Undefined


@dataclass
class CreateCustomerPortalSession(Operation):
    subscription_ids: list[str] | Undefined = Undefined()
