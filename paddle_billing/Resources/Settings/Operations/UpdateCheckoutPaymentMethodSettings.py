from dataclasses import dataclass

from paddle_billing.Operation import Operation as Operation
from paddle_billing.Entities.Settings import CheckoutPaymentMethodsUpdate as CheckoutPaymentMethodsUpdate


@dataclass
class UpdateCheckoutPaymentMethodSettings(Operation):
    payment_methods: CheckoutPaymentMethodsUpdate
