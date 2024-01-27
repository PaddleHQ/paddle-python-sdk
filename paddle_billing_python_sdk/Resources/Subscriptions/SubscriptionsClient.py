from typing import TYPE_CHECKING

from paddle_billing_python_sdk.ResponseParser import ResponseParser

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
        self.client = client


    def list(self, operation: ListSubscriptions = None) -> SubscriptionWithIncludesCollection:
        if operation is None:
            operation = ListSubscriptions()

        response = self.client.get_raw('/subscriptions', operation.get_parameters())
        parser   = ResponseParser(response)

        return SubscriptionWithIncludesCollection.from_list(
            parser.get_data(),
            Paginator(self.client, parser.get_pagination(), SubscriptionWithIncludesCollection)
        )


    def get(self, subscription_id: str, includes = None) -> SubscriptionWithIncludes:
        if includes is None:
            includes = []

        invalid_items = [item for item in includes if not isinstance(item, GetIncludes)]
        if invalid_items:
            raise InvalidArgumentException('includes', Includes.__name__, invalid_items)

        params   = {'include': ','.join(include.value for include in includes)} if includes else {}
        response = self.client.get_raw(f"/subscriptions/{subscription_id}", params)
        parser   = ResponseParser(response)

        return SubscriptionWithIncludes.from_dict(parser.get_data())


    def update(self, subscription_id: str, operation: UpdateSubscription) -> SubscriptionWithIncludes:
        response = self.client.patch_raw(f"/subscriptions/{subscription_id}", operation.get_parameters())
        parser   = ResponseParser(response)

        return SubscriptionWithIncludes.from_dict(parser.get_data())


    def pause(self, subscription_id: str, operation: PauseSubscription) -> SubscriptionWithIncludes:
        response = self.client.post_raw(f"/subscriptions/{subscription_id}/pause", operation.get_parameters())
        parser   = ResponseParser(response)

        return SubscriptionWithIncludes.from_dict(parser.get_data())


    def resume(self, subscription_id: str, operation: ResumeSubscription) -> SubscriptionWithIncludes:
        response = self.client.post_raw(f"/subscriptions/{subscription_id}/resume", operation.get_parameters())
        parser   = ResponseParser(response)

        return SubscriptionWithIncludes.from_dict(parser.get_data())


    def cancel(self, subscription_id: str, operation: CancelSubscription) -> SubscriptionWithIncludes:
        response = self.client.post_raw(f"/subscriptions/{subscription_id}/cancel", operation.get_parameters())
        parser   = ResponseParser(response)

        return SubscriptionWithIncludes.from_dict(parser.get_data())


    def get_payment_method_change_transaction(self, subscription_id: str) -> TransactionWithIncludes:
        response = self.client.get_raw(f"/subscriptions/{subscription_id}/update-payment-method-transaction")
        parser   = ResponseParser(response)

        return TransactionWithIncludes.from_dict(parser.get_data())


    def activate(self, subscription_id: str) -> SubscriptionWithIncludes:
        response = self.client.post_raw(f"/subscriptions/{subscription_id}/activate")
        parser   = ResponseParser(response)

        return SubscriptionWithIncludes.from_dict(parser.get_data())


    def create_one_time_charge(self, subscription_id: str, operation: CreateOneTimeCharge) -> SubscriptionWithIncludes:
        response = self.client.post_raw(f"/subscriptions/{subscription_id}/charge", operation.get_parameters())
        parser   = ResponseParser(response)

        return SubscriptionWithIncludes.from_dict(parser.get_data())


    def preview_update(self, subscription_id: str, operation: PreviewUpdateSubscription) -> SubscriptionPreview:
        response = self.client.patch_raw(f"/subscriptions/{subscription_id}/preview", operation.get_parameters())
        parser   = ResponseParser(response)

        return SubscriptionPreview.from_dict(parser.get_data())


    def preview_one_time_charge(self, subscription_id: str, operation: PreviewOneTimeCharge) -> SubscriptionPreview:
        response = self.client.post_raw(f"/subscriptions/{subscription_id}/charge/preview", operation.get_parameters())
        parser   = ResponseParser(response)

        return SubscriptionPreview.from_dict(parser.get_data())
