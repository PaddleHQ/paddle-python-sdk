from dataclasses import dataclass

from paddle_billing.Operation import Operation
from paddle_billing.Entities.Settings import CheckoutPaymentMethodsUpdate


@dataclass
class UpdateCheckoutPaymentMethodSettings(Operation):
    payment_methods: CheckoutPaymentMethodsUpdate
