from dataclasses import dataclass

from paddle_billing.Operation import Operation as Operation
from paddle_billing.Undefined import Undefined as Undefined
from paddle_billing.Resources.Transactions.Operations.Revise import (
    ReviseAddress as ReviseAddress,
    ReviseBusiness as ReviseBusiness,
    ReviseCustomer as ReviseCustomer,
)


@dataclass
class ReviseTransaction(Operation):
    address: ReviseAddress | Undefined = Undefined()
    business: ReviseBusiness | Undefined = Undefined()
    customer: ReviseCustomer | Undefined = Undefined()
