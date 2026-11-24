from dataclasses import dataclass

from paddle_billing.Operation import Operation as Operation

# Unused since default_url became required; kept so existing imports from this module still work.
from paddle_billing.Undefined import Undefined as Undefined  # noqa: F401


@dataclass
class UpdateCheckoutUrl(Operation):
    default_url: str
