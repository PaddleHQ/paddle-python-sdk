from dataclasses import dataclass

from paddle_billing.Operation import Operation
from paddle_billing.Undefined import Undefined
from paddle_billing.Entities.ClientTokens import ClientTokenStatus


@dataclass
class UpdateClientToken(Operation):
    status: ClientTokenStatus | Undefined = Undefined()
