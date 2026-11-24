from dataclasses import dataclass

from paddle_billing.Operation import Operation as Operation
from paddle_billing.Undefined import Undefined as Undefined
from paddle_billing.Entities.ClientTokens import ClientTokenStatus as ClientTokenStatus


@dataclass
class UpdateClientToken(Operation):
    status: ClientTokenStatus | Undefined = Undefined()
