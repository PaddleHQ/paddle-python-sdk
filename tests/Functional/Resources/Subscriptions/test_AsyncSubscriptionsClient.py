from json import loads
from pytest import mark
from urllib.parse import unquote

import respx

from paddle_billing.Entities.Collections import SubscriptionCollection
from paddle_billing.Entities.Subscription import Subscription
from paddle_billing.Entities.SubscriptionPreview import SubscriptionPreview
from paddle_billing.Entities.Transaction import Transaction

from paddle_billing.Entities.Subscriptions import SubscriptionEffectiveFrom, SubscriptionProrationBillingMode

from paddle_billing.Resources.Shared.Operations import Pager
from paddle_billing.Resources.Subscriptions.Operations import (
    CancelSubscription,
    ListSubscriptions,
    PauseSubscription,
    ResumeSubscription,
    SubscriptionIncludes,
    UpdateSubscription,
)

from tests.Utils.ReadsFixture import ReadsFixtures


SUBSCRIPTION_ID = "sub_01hp463gxfvndqjjyqn2n7tkth"


class TestAsyncSubscriptionsClient:
    @mark.parametrize(
        "operation, expected_response_status, expected_response_body, expected_url",
        [
            (ListSubscriptions(), 200, ReadsFixtures.read_raw_json_fixture("response/list_default"), "/subscriptions"),
            (
                ListSubscriptions(Pager()),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/subscriptions?order_by=id[asc]&per_page=50",
            ),
        ],
        ids=[
            "List subscriptions without pagination",
            "List subscriptions with default pagination",
        ],
    )
    async def test_list_subscriptions_returns_expected_response(
        self,
        async_test_client,
        operation,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{async_test_client.base_url}{expected_url}"

        with respx.mock() as mock:
            mock.get(expected_url).respond(
                status_code=expected_response_status,
                json=loads(expected_response_body),
            )

            response = await async_test_client.client.subscriptions.list(operation)
            last_request = mock.calls.last.request

        assert isinstance(response, SubscriptionCollection)
        assert last_request is not None
        assert last_request.method == "GET"
        assert async_test_client.client.status_code == expected_response_status
        assert (
            unquote(str(last_request.url)) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"

    @mark.parametrize(
        "subscription_id, includes, expected_response_status, expected_response_body, expected_url",
        [
            (
                SUBSCRIPTION_ID,
                None,
                200,
                ReadsFixtures.read_raw_json_fixture("response/full_entity"),
                f"/subscriptions/{SUBSCRIPTION_ID}",
            ),
            (
                SUBSCRIPTION_ID,
                [SubscriptionIncludes.NextTransaction],
                200,
                ReadsFixtures.read_raw_json_fixture("response/full_entity"),
                f"/subscriptions/{SUBSCRIPTION_ID}?include=next_transaction",
            ),
        ],
        ids=[
            "Get subscription",
            "Get subscription with includes",
        ],
    )
    async def test_get_subscription_returns_expected_response(
        self,
        async_test_client,
        subscription_id,
        includes,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{async_test_client.base_url}{expected_url}"

        with respx.mock() as mock:
            mock.get(expected_url).respond(
                status_code=expected_response_status,
                json=loads(expected_response_body),
            )

            response = await async_test_client.client.subscriptions.get(subscription_id, includes=includes)
            response_json = async_test_client.client.subscriptions.response.json()
            last_request = mock.calls.last.request

        assert isinstance(response, Subscription)
        assert last_request.method == "GET"
        assert async_test_client.client.status_code == expected_response_status
        assert (
            unquote(str(last_request.url)) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(str(expected_response_body))

    @mark.parametrize(
        "subscription_id, operation, expected_request_body, expected_response_status, expected_response_body, expected_url",
        [
            (
                SUBSCRIPTION_ID,
                UpdateSubscription(
                    proration_billing_mode=SubscriptionProrationBillingMode.ProratedNextBillingPeriod
                ),
                ReadsFixtures.read_raw_json_fixture("request/update_single"),
                200,
                ReadsFixtures.read_raw_json_fixture("response/full_entity"),
                f"/subscriptions/{SUBSCRIPTION_ID}",
            ),
            (
                SUBSCRIPTION_ID,
                UpdateSubscription(
                    proration_billing_mode=SubscriptionProrationBillingMode.FullImmediately,
                    scheduled_change=None,
                ),
                ReadsFixtures.read_raw_json_fixture("request/update_partial"),
                200,
                ReadsFixtures.read_raw_json_fixture("response/full_entity"),
                f"/subscriptions/{SUBSCRIPTION_ID}",
            ),
        ],
        ids=[
            "Update subscription with single value",
            "Update subscription with partial values",
        ],
    )
    async def test_update_subscription_uses_expected_payload(
        self,
        async_test_client,
        subscription_id,
        operation,
        expected_request_body,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{async_test_client.base_url}{expected_url}"

        with respx.mock() as mock:
            mock.patch(expected_url).respond(
                status_code=expected_response_status,
                json=loads(expected_response_body),
            )

            response = await async_test_client.client.subscriptions.update(subscription_id, operation)
            response_json = async_test_client.client.subscriptions.response.json()
            request_json = async_test_client.client.payload
            last_request = mock.calls.last.request

        assert isinstance(response, Subscription)
        assert last_request.method == "PATCH"
        assert async_test_client.client.status_code == expected_response_status
        assert (
            unquote(str(last_request.url)) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert loads(request_json) == loads(
            expected_request_body
        ), "The request JSON doesn't match the expected fixture JSON"
        assert response_json == loads(str(expected_response_body))

    @mark.parametrize(
        "subscription_id, operation, expected_request_body, expected_url",
        [
            (
                SUBSCRIPTION_ID,
                CancelSubscription(),
                ReadsFixtures.read_raw_json_fixture("request/cancel_none"),
                f"/subscriptions/{SUBSCRIPTION_ID}/cancel",
            ),
            (
                SUBSCRIPTION_ID,
                CancelSubscription(SubscriptionEffectiveFrom.NextBillingPeriod),
                ReadsFixtures.read_raw_json_fixture("request/cancel_single"),
                f"/subscriptions/{SUBSCRIPTION_ID}/cancel",
            ),
        ],
        ids=[
            "Cancel subscription immediately",
            "Cancel subscription at next billing period",
        ],
    )
    async def test_cancel_subscription_uses_expected_payload(
        self,
        async_test_client,
        subscription_id,
        operation,
        expected_request_body,
        expected_url,
    ):
        expected_url = f"{async_test_client.base_url}{expected_url}"
        response_body = ReadsFixtures.read_raw_json_fixture("response/full_entity")

        with respx.mock() as mock:
            mock.post(expected_url).respond(status_code=200, json=loads(response_body))

            response = await async_test_client.client.subscriptions.cancel(subscription_id, operation)
            request_json = async_test_client.client.payload
            last_request = mock.calls.last.request

        assert isinstance(response, Subscription)
        assert last_request.method == "POST"
        assert (
            unquote(str(last_request.url)) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert loads(request_json) == loads(
            expected_request_body
        ), "The request JSON doesn't match the expected fixture JSON"

    @mark.parametrize(
        "subscription_id, operation, expected_request_body, expected_url",
        [
            (
                SUBSCRIPTION_ID,
                PauseSubscription(),
                ReadsFixtures.read_raw_json_fixture("request/pause_none"),
                f"/subscriptions/{SUBSCRIPTION_ID}/pause",
            ),
            (
                SUBSCRIPTION_ID,
                PauseSubscription(SubscriptionEffectiveFrom.NextBillingPeriod),
                ReadsFixtures.read_raw_json_fixture("request/pause_single"),
                f"/subscriptions/{SUBSCRIPTION_ID}/pause",
            ),
        ],
        ids=[
            "Pause subscription with no options",
            "Pause subscription at next billing period",
        ],
    )
    async def test_pause_subscription_uses_expected_payload(
        self,
        async_test_client,
        subscription_id,
        operation,
        expected_request_body,
        expected_url,
    ):
        expected_url = f"{async_test_client.base_url}{expected_url}"
        response_body = ReadsFixtures.read_raw_json_fixture("response/full_entity")

        with respx.mock() as mock:
            mock.post(expected_url).respond(status_code=200, json=loads(response_body))

            response = await async_test_client.client.subscriptions.pause(subscription_id, operation)
            request_json = async_test_client.client.payload
            last_request = mock.calls.last.request

        assert isinstance(response, Subscription)
        assert last_request.method == "POST"
        assert (
            unquote(str(last_request.url)) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert loads(request_json) == loads(
            expected_request_body
        ), "The request JSON doesn't match the expected fixture JSON"

    async def test_activate_subscription_sends_post_with_no_body(self, async_test_client):
        expected_url = f"{async_test_client.base_url}/subscriptions/{SUBSCRIPTION_ID}/activate"
        response_body = ReadsFixtures.read_raw_json_fixture("response/full_entity")

        with respx.mock() as mock:
            mock.post(expected_url).respond(status_code=200, json=loads(response_body))

            response = await async_test_client.client.subscriptions.activate(SUBSCRIPTION_ID)
            last_request = mock.calls.last.request

        assert isinstance(response, Subscription)
        assert last_request.method == "POST"
        assert unquote(str(last_request.url)) == expected_url

    async def test_get_payment_method_change_transaction_returns_transaction(self, async_test_client):
        expected_url = (
            f"{async_test_client.base_url}"
            f"/subscriptions/{SUBSCRIPTION_ID}/update-payment-method-transaction"
        )
        response_body = ReadsFixtures.read_raw_json_fixture(
            "response/get_payment_method_change_transaction_entity"
        )

        with respx.mock() as mock:
            mock.get(expected_url).respond(status_code=200, json=loads(response_body))

            response = await async_test_client.client.subscriptions.get_payment_method_change_transaction(
                SUBSCRIPTION_ID
            )
            last_request = mock.calls.last.request

        assert isinstance(response, Transaction)
        assert last_request.method == "GET"
        assert unquote(str(last_request.url)) == expected_url
