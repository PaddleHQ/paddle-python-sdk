from __future__ import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Simulations.Config.Options import DunningExhaustedAction, PaymentOutcome
from paddle_billing.Undefined import Undefined


@dataclass
class SubscriptionResumeOptionsCreate:
    payment_outcome: PaymentOutcome | Undefined = Undefined()
    dunning_exhausted_action: DunningExhaustedAction | None | Undefined = Undefined()

    @staticmethod
    def for_successful_payment() -> SubscriptionResumeOptionsCreate:
        return SubscriptionResumeOptionsCreate(payment_outcome=PaymentOutcome.Success)

    @staticmethod
    def for_recovered_updated_payment_method() -> SubscriptionResumeOptionsCreate:
        return SubscriptionResumeOptionsCreate(payment_outcome=PaymentOutcome.RecoveredUpdatedPaymentMethod)

    @staticmethod
    def for_recovered_existing_payment_method() -> SubscriptionResumeOptionsCreate:
        return SubscriptionResumeOptionsCreate(payment_outcome=PaymentOutcome.RecoveredExistingPaymentMethod)

    @staticmethod
    def for_failed_payment(
        dunning_exhausted_action: DunningExhaustedAction | Undefined = Undefined(),
    ) -> SubscriptionResumeOptionsCreate:
        return SubscriptionResumeOptionsCreate(
            payment_outcome=PaymentOutcome.Failed,
            dunning_exhausted_action=dunning_exhausted_action,
        )
