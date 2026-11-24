from dataclasses import dataclass

from paddle_billing.Operation import Operation as Operation
from paddle_billing.Undefined import Undefined as Undefined
from paddle_billing.Entities.Settings import AudienceOptIn as AudienceOptIn


@dataclass
class UpdateCheckoutFeatures(Operation):
    discounts_enabled: bool | Undefined = Undefined()
    audience_opt_in: AudienceOptIn | Undefined = Undefined()
    saved_payment_methods_enabled: bool | Undefined = Undefined()
