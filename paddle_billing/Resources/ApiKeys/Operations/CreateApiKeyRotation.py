from dataclasses import dataclass
from datetime import datetime

from paddle_billing.Operation import Operation
from paddle_billing.Undefined import Undefined
from paddle_billing.Entities.DateTime import DateTime


@dataclass
class CreateApiKeyRotation(Operation):
    grace_period_seconds: int
    new_key_expires_at: DateTime | datetime | Undefined = Undefined()
