from dataclasses import dataclass

from paddle_billing.Operation import Operation
from paddle_billing.Entities.CheckoutDomains import CheckoutDomainPaymentMethod


@dataclass
class VerifyCheckoutDomainPaymentMethod(Operation):
    payment_method: CheckoutDomainPaymentMethod
