from dataclasses import dataclass

from paddle_billing.Operation import Operation


@dataclass
class UpdateCheckoutUrl(Operation):
    default_url: str
