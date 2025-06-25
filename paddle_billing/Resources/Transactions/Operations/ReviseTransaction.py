from dataclasses import dataclass

from paddle_billing.Operation import Operation
from paddle_billing.Undefined import Undefined
from paddle_billing.Resources.Transactions.Operations.Revise import (
    ReviseAddress,
    ReviseBusiness,
    ReviseCustomer,
)


@dataclass
class ReviseTransaction(Operation):
    address: ReviseAddress | Undefined = Undefined()
    business: ReviseBusiness | Undefined = Undefined()
    customer: ReviseCustomer | Undefined = Undefined()
