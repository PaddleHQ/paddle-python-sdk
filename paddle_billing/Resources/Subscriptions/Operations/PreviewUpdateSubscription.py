from dataclasses import asdict, dataclass

from paddle_billing.Undefined import Undefined

from paddle_billing.Entities.DateTime      import DateTime
from paddle_billing.Entities.Shared        import BillingDetails, CollectionMode, CurrencyCode, CustomData
from paddle_billing.Entities.Subscriptions import SubscriptionItems, SubscriptionOnPaymentFailure, SubscriptionProrationBillingMode

from paddle_billing.Resources.Subscriptions.Operations.Update.SubscriptionDiscount import SubscriptionDiscount


@dataclass
class PreviewUpdateSubscription:
    customer_id:            str                                      | Undefined = Undefined()
    address_id:             str                                      | Undefined = Undefined()
    business_id:            str                               | None | Undefined = Undefined()
    currency_code:          CurrencyCode                             | Undefined = Undefined()
    next_billed_at:         DateTime                                 | Undefined = Undefined()
    discount:               SubscriptionDiscount              | None | Undefined = Undefined()
    collection_mode:        CollectionMode                           | Undefined = Undefined()
    billing_details:        BillingDetails                    | None | Undefined = Undefined()
    scheduled_change:                                           None | Undefined = Undefined()
    items:                  list[SubscriptionItems]                  | Undefined = Undefined()
    custom_data:            CustomData                        | None | Undefined = Undefined()
    proration_billing_mode: SubscriptionProrationBillingMode         | Undefined = Undefined()
    on_payment_failure:     SubscriptionOnPaymentFailure             | Undefined = Undefined()


    def get_parameters(self) -> dict:
        parameters = asdict(self)

        if isinstance(self.next_billed_at, DateTime):
            parameters['next_billed_at'] = self.next_billed_at.format()
        if not isinstance(self.items, Undefined):
            parameters['items'] = [item.get_parameters() for item in self.items]

        return parameters
