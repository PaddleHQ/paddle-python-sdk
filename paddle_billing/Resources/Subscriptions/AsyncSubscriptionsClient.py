# AUTO-GENERATED FILE — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/Subscriptions/SubscriptionsClient.py
# Regenerate with: python scripts/generate_async_clients.py
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Subscription import Subscription
from paddle_billing.Entities.SubscriptionPreview import SubscriptionPreview
from paddle_billing.Entities.Transaction import Transaction
from paddle_billing.Entities.Collections import SubscriptionCollection

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException

from paddle_billing.Resources.Subscriptions.Operations import (
    CancelSubscription,
    CreateOneTimeCharge,
    SubscriptionIncludes,
    ListSubscriptions,
    PauseSubscription,
    PreviewOneTimeCharge,
    PreviewUpdateSubscription,
    ResumeSubscription,
    UpdateSubscription,
)

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient


class AsyncSubscriptionsClient:
    def __init__(self, client: "AsyncClient"):
        self.client = client
        self.response = None

    async def list(self, operation: ListSubscriptions | None = None) -> SubscriptionCollection:
        if operation is None:
            operation = ListSubscriptions()

        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            return SubscriptionCollection.from_list(
                parser.get_list(), self.client._make_paginator(parser.get_pagination(), SubscriptionCollection)
            )
        return await self.client._get("/subscriptions", operation.get_parameters(), parse)

    async def get(self, subscription_id: str, includes=None) -> Subscription:
        if includes is None:
            includes = []

        invalid_items = [item for item in includes if not isinstance(item, SubscriptionIncludes)]
        if invalid_items:
            raise InvalidArgumentException.array_contains_invalid_types(
                "includes", SubscriptionIncludes.__name__, invalid_items
            )

        params = {"include": ",".join(include.value for include in includes)} if includes else {}

        def parse(response):
            self.response = response
            return Subscription.from_dict(ResponseParser(response).get_dict())
        return await self.client._get(f"/subscriptions/{subscription_id}", params, parse)

    async def update(self, subscription_id: str, operation: UpdateSubscription) -> Subscription:
        def parse(response):
            self.response = response
            return Subscription.from_dict(ResponseParser(response).get_dict())
        return await self.client._patch(f"/subscriptions/{subscription_id}", operation, parse)

    async def pause(self, subscription_id: str, operation: PauseSubscription) -> Subscription:
        def parse(response):
            self.response = response
            return Subscription.from_dict(ResponseParser(response).get_dict())
        return await self.client._post(f"/subscriptions/{subscription_id}/pause", operation, parse)

    async def resume(self, subscription_id: str, operation: ResumeSubscription) -> Subscription:
        def parse(response):
            self.response = response
            return Subscription.from_dict(ResponseParser(response).get_dict())
        return await self.client._post(f"/subscriptions/{subscription_id}/resume", operation, parse)

    async def cancel(self, subscription_id: str, operation: CancelSubscription) -> Subscription:
        def parse(response):
            self.response = response
            return Subscription.from_dict(ResponseParser(response).get_dict())
        return await self.client._post(f"/subscriptions/{subscription_id}/cancel", operation, parse)

    async def get_payment_method_change_transaction(self, subscription_id: str) -> Transaction:
        def parse(response):
            self.response = response
            return Transaction.from_dict(ResponseParser(response).get_dict())
        return await self.client._get(f"/subscriptions/{subscription_id}/update-payment-method-transaction", None, parse)

    async def activate(self, subscription_id: str) -> Subscription:
        def parse(response):
            self.response = response
            return Subscription.from_dict(ResponseParser(response).get_dict())
        return await self.client._post(f"/subscriptions/{subscription_id}/activate", None, parse)

    async def create_one_time_charge(self, subscription_id: str, operation: CreateOneTimeCharge) -> Subscription:
        def parse(response):
            self.response = response
            return Subscription.from_dict(ResponseParser(response).get_dict())
        return await self.client._post(f"/subscriptions/{subscription_id}/charge", operation, parse)

    async def preview_update(self, subscription_id: str, operation: PreviewUpdateSubscription) -> SubscriptionPreview:
        def parse(response):
            self.response = response
            return SubscriptionPreview.from_dict(ResponseParser(response).get_dict())
        return await self.client._patch(f"/subscriptions/{subscription_id}/preview", operation, parse)

    async def preview_one_time_charge(self, subscription_id: str, operation: PreviewOneTimeCharge) -> SubscriptionPreview:
        def parse(response):
            self.response = response
            return SubscriptionPreview.from_dict(ResponseParser(response).get_dict())
        return await self.client._post(f"/subscriptions/{subscription_id}/charge/preview", operation, parse)
