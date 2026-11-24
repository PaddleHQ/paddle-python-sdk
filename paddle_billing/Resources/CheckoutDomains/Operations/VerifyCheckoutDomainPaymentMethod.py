from dataclasses import dataclass

from paddle_billing.Operation import Operation as Operation
from paddle_billing.Entities.CheckoutDomains import CheckoutDomainPaymentMethod as CheckoutDomainPaymentMethod


@dataclass
class VerifyCheckoutDomainPaymentMethod(Operation):
    payment_method: CheckoutDomainPaymentMethod
