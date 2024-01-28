from typing import TYPE_CHECKING

from paddle_billing_python_sdk.ResponseParser import ResponseParser

from paddle_billing_python_sdk.Entities.Subscription                                   import Subscription
from paddle_billing_python_sdk.Entities.SubscriptionPreview                            import SubscriptionPreview
from paddle_billing_python_sdk.Entities.SubscriptionWithIncludes                       import SubscriptionWithIncludes
from paddle_billing_python_sdk.Entities.TransactionWithIncludes                        import TransactionWithIncludes
from paddle_billing_python_sdk.Entities.Collections.Paginator                          import Paginator
from paddle_billing_python_sdk.Entities.Collections.SubscriptionWithIncludesCollection import SubscriptionWithIncludesCollection

from paddle_billing_python_sdk.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException

from paddle_billing_python_sdk.Resources.Subscriptions.Operations.CancelSubscription        import CancelSubscription
from paddle_billing_python_sdk.Resources.Subscriptions.Operations.CreateOneTimeCharge       import CreateOneTimeCharge
from paddle_billing_python_sdk.Resources.Subscriptions.Operations.ListSubscriptions         import ListSubscriptions
from paddle_billing_python_sdk.Resources.Subscriptions.Operations.PauseSubscription         import PauseSubscription
from paddle_billing_python_sdk.Resources.Subscriptions.Operations.PreviewOneTimeCharge      import PreviewOneTimeCharge
from paddle_billing_python_sdk.Resources.Subscriptions.Operations.PreviewUpdateSubscription import PreviewUpdateSubscription
from paddle_billing_python_sdk.Resources.Subscriptions.Operations.ResumeSubscription        import ResumeSubscription
from paddle_billing_python_sdk.Resources.Subscriptions.Operations.UpdateSubscription        import UpdateSubscription
from paddle_billing_python_sdk.Resources.Subscriptions.Operations.Get.Includes              import Includes


if TYPE_CHECKING:
    from paddle_billing_python_sdk.Client import Client


class SubscriptionsClient:
    def __init__(self, client: 'Client'):
        self.client   = client
        self.response = None


    def list(self, operation: ListSubscriptions = None) -> SubscriptionWithIncludesCollection:
        if operation is None:
            operation = ListSubscriptions()

        self.response = self.client.get_raw('/subscriptions', operation.get_parameters())
        parser        = ResponseParser(self.response)

        return SubscriptionWithIncludesCollection.from_list(
            parser.get_data(),
            Paginator(self.client, parser.get_pagination(), SubscriptionWithIncludesCollection)
        )


    def get(self, subscription_id: str, includes = None) -> SubscriptionWithIncludes:
        if includes is None:
            includes = []

        invalid_items = [item for item in includes if not isinstance(item, Includes)]
        if invalid_items:
            raise InvalidArgumentException('includes', Includes.__name__, invalid_items)

        params        = {'include': ','.join(include.value for include in includes)} if includes else {}
        self.response = self.client.get_raw(f"/subscriptions/{subscription_id}", params)
        parser        = ResponseParser(self.response)

        return SubscriptionWithIncludes.from_dict(parser.get_data())


    def update(self, subscription_id: str, operation: UpdateSubscription) -> Subscription:
        self.response = self.client.patch_raw(f"/subscriptions/{subscription_id}", operation.get_parameters())
        parser        = ResponseParser(self.response)

        return Subscription.from_dict(parser.get_data())


    def pause(self, subscription_id: str, operation: PauseSubscription) -> Subscription:
        self.response = self.client.post_raw(f"/subscriptions/{subscription_id}/pause", operation.get_parameters())
        parser        = ResponseParser(self.response)

        return Subscription.from_dict(parser.get_data())


    def resume(self, subscription_id: str, operation: ResumeSubscription) -> Subscription:
        self.response = self.client.post_raw(f"/subscriptions/{subscription_id}/resume", operation.get_parameters())
        parser        = ResponseParser(self.response)

        return Subscription.from_dict(parser.get_data())


    def cancel(self, subscription_id: str, operation: CancelSubscription) -> Subscription:
        self.response = self.client.post_raw(f"/subscriptions/{subscription_id}/cancel", operation.get_parameters())
        parser        = ResponseParser(self.response)

        return Subscription.from_dict(parser.get_data())


    def get_payment_method_change_transaction(self, subscription_id: str) -> TransactionWithIncludes:
        self.response = self.client.get_raw(f"/subscriptions/{subscription_id}/update-payment-method-transaction")
        parser        = ResponseParser(self.response)

        return TransactionWithIncludes.from_dict(parser.get_data())


    def activate(self, subscription_id: str) -> Subscription:
        self.response = self.client.post_raw(f"/subscriptions/{subscription_id}/activate")
        parser        = ResponseParser(self.response)

        return Subscription.from_dict(parser.get_data())


    def create_one_time_charge(self, subscription_id: str, operation: CreateOneTimeCharge) -> Subscription:
        self.response = self.client.post_raw(f"/subscriptions/{subscription_id}/charge", operation.get_parameters())
        parser        = ResponseParser(self.response)

        return Subscription.from_dict(parser.get_data())


    def preview_update(self, subscription_id: str, operation: PreviewUpdateSubscription) -> SubscriptionPreview:
        self.response = self.client.patch_raw(f"/subscriptions/{subscription_id}/preview", operation.get_parameters())
        parser        = ResponseParser(self.response)

        return SubscriptionPreview.from_dict(parser.get_data())


    def preview_one_time_charge(self, subscription_id: str, operation: PreviewOneTimeCharge) -> SubscriptionPreview:
        self.response = self.client.post_raw(f"/subscriptions/{subscription_id}/charge/preview", operation.get_parameters())
        parser        = ResponseParser(self.response)

        return SubscriptionPreview.from_dict(parser.get_data())
