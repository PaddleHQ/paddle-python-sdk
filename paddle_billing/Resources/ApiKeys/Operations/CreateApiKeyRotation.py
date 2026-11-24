from dataclasses import dataclass
from datetime import datetime

from paddle_billing.Operation import Operation as Operation
from paddle_billing.Undefined import Undefined as Undefined
from paddle_billing.Entities.DateTime import DateTime as DateTime


@dataclass
class CreateApiKeyRotation(Operation):
    grace_period_seconds: int
    new_key_expires_at: DateTime | datetime | Undefined = Undefined()
