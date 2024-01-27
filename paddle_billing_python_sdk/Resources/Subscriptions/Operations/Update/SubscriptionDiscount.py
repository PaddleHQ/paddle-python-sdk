from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionEffectiveFrom import SubscriptionEffectiveFrom


class SubscriptionDiscount:
    def __init__(self, id: str, effective_from: SubscriptionEffectiveFrom):
        self.id = id
        self.effective_from = effective_from
