from json         import loads
from pytest       import mark
from urllib.parse import unquote

from paddle_billing.Entities.Collections         import SubscriptionCollection
from paddle_billing.Entities.DateTime            import DateTime
from paddle_billing.Entities.Subscription        import Subscription
from paddle_billing.Entities.SubscriptionPreview import SubscriptionPreview
from paddle_billing.Entities.Transaction         import Transaction

from paddle_billing.Entities.Shared        import CollectionMode, CurrencyCode, CustomData
from paddle_billing.Entities.Subscriptions import (
    SubscriptionEffectiveFrom,
    SubscriptionItems,
    SubscriptionOnPaymentFailure,
    SubscriptionProrationBillingMode,
    SubscriptionResumeEffectiveFrom,
    SubscriptionScheduledChangeAction,
    SubscriptionStatus,
)

from paddle_billing.Resources.Shared.Operations        import Pager
from paddle_billing.Resources.Subscriptions.Operations import (
    CancelSubscription,
    CreateOneTimeCharge,
    ListSubscriptions,
    PauseSubscription,
    PreviewOneTimeCharge,
    PreviewUpdateSubscription,
    ResumeSubscription,
    SubscriptionDiscount,
    SubscriptionIncludes,
    UpdateSubscription,
)

from tests.Utils.TestClient   import mock_requests, test_client
from tests.Utils.ReadsFixture import ReadsFixtures


class TestSubscriptionsClient:
    @mark.parametrize(
        'subscription_id, operation, expected_request_body, expected_response_status, expected_response_body, expected_url',
        [
            (
                'sub_01h8bx8fmywym11t6swgzba704',
                UpdateSubscription(proration_billing_mode=SubscriptionProrationBillingMode.ProratedNextBillingPeriod),
                ReadsFixtures.read_raw_json_fixture('request/update_single'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/subscriptions/sub_01h8bx8fmywym11t6swgzba704',
            ), (
                'sub_01h8bx8fmywym11t6swgzba704',
                UpdateSubscription(
                    proration_billing_mode = SubscriptionProrationBillingMode.FullImmediately,
                    scheduled_change       = None,
                ),
                ReadsFixtures.read_raw_json_fixture('request/update_partial'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/subscriptions/sub_01h8bx8fmywym11t6swgzba704',
            ), (
                'sub_01h8bx8fmywym11t6swgzba704',
                UpdateSubscription(
                    customer_id            = 'ctm_01h8441jn5pcwrfhwh78jqt8hk',
                    address_id             = 'add_01h848pep46enq8y372x7maj0p',
                    business_id            = None,
                    currency_code          = CurrencyCode.GBP,
                    next_billed_at         = DateTime('2023-11-06 14:00:00'),
                    collection_mode        = CollectionMode.Automatic,
                    billing_details        = None,
                    scheduled_change       = None,
                    proration_billing_mode = SubscriptionProrationBillingMode.FullImmediately,
                    custom_data            = CustomData({'early_access': True}),
                    discount               = SubscriptionDiscount(
                        'dsc_01h848pep46enq8y372x7maj0p',
                        SubscriptionEffectiveFrom.NextBillingPeriod,
                    ),
                    items = [
                        SubscriptionItems('pri_01gsz91wy9k1yn7kx82aafwvea', 1),
                        SubscriptionItems('pri_01gsz91wy9k1yn7kx82bafwvea', 5),
                    ],
                ),
                ReadsFixtures.read_raw_json_fixture('request/update_full'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/subscriptions/sub_01h8bx8fmywym11t6swgzba704',
            ),
        ],
        ids=[
            "Update subscription with a single new value",
            "Update subscription with partial new values",
            "Update subscription with all new values",
        ],
    )
    def test_update_subscription_uses_expected_payload(
        self,
        test_client,
        mock_requests,
        subscription_id,
        operation,
        expected_request_body,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.patch(expected_url, status_code=expected_response_status, text=expected_response_body)

        response      = test_client.client.subscriptions.update(subscription_id, operation=operation)
        response_json = test_client.client.subscriptions.response.json()
        request_json  = test_client.client.payload
        last_request  = mock_requests.last_request

        assert isinstance(response, Subscription)
        assert last_request is not None
        assert last_request.method            == 'PATCH'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"
        assert loads(request_json) == loads(expected_request_body), \
            "The request JSON doesn't match the expected fixture JSON"
        assert response_json == loads(str(expected_response_body)), \
            "The response JSON doesn't match the expected fixture JSON"


    @mark.parametrize(
        'operation, expected_response_status, expected_response_body, expected_url',
        [
            (
                ListSubscriptions(),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/subscriptions',
            ), (
                ListSubscriptions(Pager()),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/subscriptions?order_by=id[asc]&per_page=50',
            ), (
                ListSubscriptions(Pager(after='sub_01h848pep46enq8y372x7maj0p')),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/subscriptions?after=sub_01h848pep46enq8y372x7maj0p&order_by=id[asc]&per_page=50',
            ), (
                ListSubscriptions(statuses=[SubscriptionStatus.Paused]),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/subscriptions?status=paused',
            ), (
                ListSubscriptions(ids=['sub_01h848pep46enq8y372x7maj0p']),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/subscriptions?id=sub_01h848pep46enq8y372x7maj0p',
            ), (
                ListSubscriptions(ids=['sub_01h8494f4w5rwfp8b12yqh8fp1', 'sub_01h848pep46enq8y372x7maj0p']),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/subscriptions?id=sub_01h8494f4w5rwfp8b12yqh8fp1,sub_01h848pep46enq8y372x7maj0p',
            ), (
                ListSubscriptions(collection_mode=CollectionMode.Automatic),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/subscriptions?collection_mode=automatic',
            ), (
                ListSubscriptions(address_ids=['add_01h8494f4w5rwfp8b12yqh8fp1']),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/subscriptions?address_id=add_01h8494f4w5rwfp8b12yqh8fp1',
            ), (
                ListSubscriptions(address_ids=['add_01h8494f4w5rwfp8b12yqh8fp1', 'add_01h848pep46enq8y372x7maj0p']),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/subscriptions?address_id=add_01h8494f4w5rwfp8b12yqh8fp1,add_01h848pep46enq8y372x7maj0p',
            ), (
                ListSubscriptions(price_ids=['pri_01h8494f4w5rwfp8b12yqh8fp1']),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/subscriptions?price_id=pri_01h8494f4w5rwfp8b12yqh8fp1',
            ), (
                ListSubscriptions(price_ids=['pri_01h8494f4w5rwfp8b12yqh8fp1', 'pri_01h848pep46enq8y372x7maj0p']),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/subscriptions?price_id=pri_01h8494f4w5rwfp8b12yqh8fp1,pri_01h848pep46enq8y372x7maj0p',
            ), (
                ListSubscriptions(scheduled_change_actions=[SubscriptionScheduledChangeAction.Pause]),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                "/subscriptions?scheduled_change_action=pause",
            ), (
                ListSubscriptions(scheduled_change_actions=[
                    SubscriptionScheduledChangeAction.Pause,
                    SubscriptionScheduledChangeAction.Cancel,
                ]),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/subscriptions?scheduled_change_action=pause,cancel',
            ),
        ],
        ids=[
            "List subscriptions without pagination",
            "List subscriptions with default pagination",
            "List paginated subscriptions after specified subscription_id",
            "List subscriptions filtered by status",
            "List subscriptions filtered by id",
            "List subscriptions filtered by multiple ids",
            "List subscriptions filtered by automatic collection_mode",
            "List subscriptions filtered by address_id",
            "List subscriptions filtered by multiple address_ids",
            "List subscriptions filtered by price_id",
            "List subscriptions filtered by multiple price_ids",
            "List subscriptions with scheduled_change_actions",
            "List subscriptions with multiple scheduled_change_actions",
        ],
    )
    def test_list_subscriptions_returns_expected_response(
        self,
        test_client,
        mock_requests,
        operation,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.get(expected_url, status_code=expected_response_status, text=expected_response_body)

        response      = test_client.client.subscriptions.list(operation)
        response_json = test_client.client.subscriptions.response.json()
        last_request  = mock_requests.last_request

        assert isinstance(response, SubscriptionCollection)
        assert last_request is not None
        assert last_request.method            == 'GET'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(str(expected_response_body)), \
            "The response JSON generated by ResponseParser() doesn't match the expected fixture JSON"


    @mark.parametrize(
        'subscription_id, includes, expected_response_status, expected_response_body, expected_url',
        [
            (
                'sub_01h7zcgmdc6tmwtjehp3sh7azf',
                None,
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/subscriptions/sub_01h7zcgmdc6tmwtjehp3sh7azf',
            ), (
                'sub_01h7zcgmdc6tmwtjehp3sh7azf',
                [SubscriptionIncludes.NextTransaction],
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/subscriptions/sub_01h7zcgmdc6tmwtjehp3sh7azf?include=next_transaction',
            ),
        ],
        ids=[
            "Get subscriptions",
            "Get subscriptions with includes",
        ],
    )
    def test_get_subscriptions_returns_expected_response(
        self,
        test_client,
        mock_requests,
        subscription_id,
        includes,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.get(expected_url, status_code=expected_response_status, text=expected_response_body)

        response      = test_client.client.subscriptions.get(subscription_id, includes=includes)
        response_json = test_client.client.subscriptions.response.json()
        last_request  = mock_requests.last_request

        assert isinstance(response, Subscription)
        assert last_request is not None
        assert last_request.method            == 'GET'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(str(expected_response_body)), \
            "The response JSON generated by ResponseParser() doesn't match the expected fixture JSON"


    @mark.parametrize(
        'subscription_id, operation, expected_request_body, expected_response_status, expected_response_body, expected_url',
        [
            (
                'sub_01h8bx8fmywym11t6swgzba704',
                PauseSubscription(),
                ReadsFixtures.read_raw_json_fixture('request/pause_none'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/subscriptions/sub_01h8bx8fmywym11t6swgzba704/pause',
            ), (
                'sub_01h8bx8fmywym11t6swgzba704',
                PauseSubscription(SubscriptionEffectiveFrom.NextBillingPeriod),
                ReadsFixtures.read_raw_json_fixture('request/pause_single'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/subscriptions/sub_01h8bx8fmywym11t6swgzba704/pause',
            ), (
                'sub_01h8bx8fmywym11t6swgzba704',
                PauseSubscription(SubscriptionEffectiveFrom.NextBillingPeriod, DateTime('2023-10-09T16:30:00Z')),
                ReadsFixtures.read_raw_json_fixture('request/pause_full'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/subscriptions/sub_01h8bx8fmywym11t6swgzba704/pause',
            ),
        ],
        ids=[
            "Pause subscription",
            "Pause subscription as of next billing period",
            "Pause subscription as of next billing period and resume at date",
        ],
    )
    def test_pause_subscription_uses_expected_payload(
        self,
        test_client,
        mock_requests,
        subscription_id,
        operation,
        expected_request_body,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.post(expected_url, status_code=expected_response_status, text=expected_response_body)

        response      = test_client.client.subscriptions.pause(subscription_id, operation=operation)
        response_json = test_client.client.subscriptions.response.json()
        request_json  = test_client.client.payload
        last_request  = mock_requests.last_request

        assert isinstance(response, Subscription)
        assert last_request is not None
        assert last_request.method            == 'POST'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"
        assert loads(request_json) == loads(expected_request_body), \
            "The request JSON doesn't match the expected fixture JSON"
        assert response_json == loads(str(expected_response_body)), \
            "The response JSON doesn't match the expected fixture JSON"


    @mark.parametrize(
        'subscription_id, operation, expected_request_body, expected_response_status, expected_response_body, expected_url',
        [
            (
                'sub_01h8bx8fmywym11t6swgzba704',
                ResumeSubscription(),
                ReadsFixtures.read_raw_json_fixture('request/resume_none'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/subscriptions/sub_01h8bx8fmywym11t6swgzba704/resume',
            ), (
                'sub_01h8bx8fmywym11t6swgzba704',
                ResumeSubscription(SubscriptionResumeEffectiveFrom.Immediately),
                ReadsFixtures.read_raw_json_fixture('request/resume_single_as_enum'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/subscriptions/sub_01h8bx8fmywym11t6swgzba704/resume',
            ), (
                'sub_01h8bx8fmywym11t6swgzba704',
                ResumeSubscription(DateTime('2023-10-09T16:30:00Z')),
                ReadsFixtures.read_raw_json_fixture('request/resume_single_as_date'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/subscriptions/sub_01h8bx8fmywym11t6swgzba704/resume',
            ),
        ],
        ids=[
            "Resume subscription",
            "Resume subscription with a billing period",
            "Resume subscription with a new date",
        ],
    )
    def test_resume_subscription_uses_expected_payload(
        self,
        test_client,
        mock_requests,
        subscription_id,
        operation,
        expected_request_body,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.post(expected_url, status_code=expected_response_status, text=expected_response_body)

        response      = test_client.client.subscriptions.resume(subscription_id, operation)
        response_json = test_client.client.subscriptions.response.json()
        request_json  = test_client.client.payload
        last_request  = mock_requests.last_request

        assert isinstance(response, Subscription)
        assert last_request is not None
        assert last_request.method            == 'POST'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"
        assert loads(request_json) == loads(expected_request_body), \
            "The request JSON doesn't match the expected fixture JSON"
        assert response_json == loads(str(expected_response_body)), \
            "The response JSON doesn't match the expected fixture JSON"


    @mark.parametrize(
        'subscription_id, operation, expected_request_body, expected_response_status, expected_response_body, expected_url',
        [
            (
                'sub_01h8bx8fmywym11t6swgzba704',
                CancelSubscription(),
                ReadsFixtures.read_raw_json_fixture('request/cancel_none'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/subscriptions/sub_01h8bx8fmywym11t6swgzba704/cancel',
            ), (
                'sub_01h8bx8fmywym11t6swgzba704',
                CancelSubscription(SubscriptionEffectiveFrom.NextBillingPeriod),
                ReadsFixtures.read_raw_json_fixture('request/cancel_single'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/subscriptions/sub_01h8bx8fmywym11t6swgzba704/cancel',
            ),
        ],
        ids=[
            "Cancel subscription",
            "Cancel subscription with a billing period",
        ],
    )
    def test_cancel_subscription_uses_expected_payload(
        self,
        test_client,
        mock_requests,
        subscription_id,
        operation,
        expected_request_body,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.post(expected_url, status_code=expected_response_status, text=expected_response_body)

        response      = test_client.client.subscriptions.cancel(subscription_id, operation)
        response_json = test_client.client.subscriptions.response.json()
        request_json  = test_client.client.payload
        last_request  = mock_requests.last_request

        assert isinstance(response, Subscription)
        assert last_request is not None
        assert last_request.method            == 'POST'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"
        assert loads(request_json) == loads(expected_request_body), \
            "The request JSON doesn't match the expected fixture JSON"
        assert response_json == loads(str(expected_response_body)), \
            "The response JSON doesn't match the expected fixture JSON"


    @mark.parametrize(
        'subscription_id, operation, expected_response_status, expected_response_body, expected_url',
        [(
            'sub_01h7zcgmdc6tmwtjehp3sh7azf',
            CancelSubscription(),
            200,
            ReadsFixtures.read_raw_json_fixture('response/get_payment_method_change_transaction_entity'),
            '/subscriptions/sub_01h7zcgmdc6tmwtjehp3sh7azf/update-payment-method-transaction',
        )],
        ids=["Cancel subscription"],
    )
    def test_get_payment_method_change_transaction_returns_expected_response(
        self,
        test_client,
        mock_requests,
        subscription_id,
        operation,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.get(expected_url, status_code=expected_response_status, text=expected_response_body)

        response      = test_client.client.subscriptions.get_payment_method_change_transaction(subscription_id)
        response_json = test_client.client.subscriptions.response.json()
        last_request  = mock_requests.last_request

        assert isinstance(response, Transaction)
        assert last_request is not None
        assert last_request.method            == 'GET'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(str(expected_response_body)), \
            "The response JSON doesn't match the expected fixture JSON"


    @mark.parametrize(
        'subscription_id, expected_response_status, expected_response_body, expected_url',
        [(
            'sub_01h8bx8fmywym11t6swgzba704',
            200,
            ReadsFixtures.read_raw_json_fixture('response/full_entity'),
            '/subscriptions/sub_01h8bx8fmywym11t6swgzba704/activate',
        )],
        ids=["Activate trialing subscription"],
    )
    def test_activate_subscription_returns_expected_response(
        self,
        test_client,
        mock_requests,
        subscription_id,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.post(expected_url, status_code=expected_response_status, text=expected_response_body)

        response      = test_client.client.subscriptions.activate(subscription_id)
        response_json = test_client.client.subscriptions.response.json()
        last_request  = mock_requests.last_request

        assert isinstance(response, Subscription)
        assert last_request is not None
        assert last_request.method            == 'POST'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(str(expected_response_body)), \
            "The response JSON doesn't match the expected fixture JSON"


    @mark.parametrize(
        'subscription_id, operation, expected_request_body, expected_response_status, expected_response_body, expected_url',
        [
            (
                'sub_01h8bx8fmywym11t6swgzba704',
                CreateOneTimeCharge(
                    SubscriptionEffectiveFrom.NextBillingPeriod,
                    [SubscriptionItems('pri_01gsz98e27ak2tyhexptwc58yk', 1)],
                ),
                ReadsFixtures.read_raw_json_fixture('request/create_one_time_charge_minimal'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/subscriptions/sub_01h8bx8fmywym11t6swgzba704/charge',
            ), (
                'sub_01h8bx8fmywym11t6swgzba704',
                CreateOneTimeCharge(
                    SubscriptionEffectiveFrom.Immediately,
                    [
                        SubscriptionItems('pri_01gsz98e27ak2tyhexptwc58yk', 1),
                        SubscriptionItems('pri_01h7zdqstxe6djaefkqbkjy4k2', 10),
                        SubscriptionItems('pri_01h7zd9mzfq79850w4ryc39v38', 845),
                    ],
                    SubscriptionOnPaymentFailure.ApplyChange,
                ),
                ReadsFixtures.read_raw_json_fixture('request/create_one_time_charge_full'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/subscriptions/sub_01h8bx8fmywym11t6swgzba704/charge',
            ),
        ],
        ids=[
            "Create subscription one-time payment for one item effective next billing period",
            "Create subscription one-time payment for multiple items effective immediately",
        ],
    )
    def test_create_subscription_one_time_charge_uses_expected_payload(
        self,
        test_client,
        mock_requests,
        subscription_id,
        operation,
        expected_request_body,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.post(expected_url, status_code=expected_response_status, text=expected_response_body)

        response      = test_client.client.subscriptions.create_one_time_charge(subscription_id, operation)
        response_json = test_client.client.subscriptions.response.json()
        request_json  = test_client.client.payload
        last_request  = mock_requests.last_request

        assert isinstance(response, Subscription)
        assert last_request is not None
        assert last_request.method            == 'POST'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"
        assert loads(request_json) == loads(expected_request_body), \
            "The request JSON doesn't match the expected fixture JSON"
        assert response_json == loads(str(expected_response_body)), \
            "The response JSON doesn't match the expected fixture JSON"


    @mark.parametrize(
        'subscription_id, operation, expected_request_body, expected_response_status, expected_response_body, expected_url',
        [
            (
                'sub_01h8bx8fmywym11t6swgzba704',
                PreviewUpdateSubscription(proration_billing_mode=SubscriptionProrationBillingMode.ProratedNextBillingPeriod),
                ReadsFixtures.read_raw_json_fixture('request/preview_update_single'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/preview_update_full_entity'),
                '/subscriptions/sub_01h8bx8fmywym11t6swgzba704/preview',
            ), (
                'sub_01h8bx8fmywym11t6swgzba704',
                PreviewUpdateSubscription(
                    proration_billing_mode = SubscriptionProrationBillingMode.FullImmediately,
                    scheduled_change       = None,
                ),
                ReadsFixtures.read_raw_json_fixture('request/preview_update_partial'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/preview_update_full_entity'),
                '/subscriptions/sub_01h8bx8fmywym11t6swgzba704/preview',
            ), (
                'sub_01h8bx8fmywym11t6swgzba704',
                PreviewUpdateSubscription(
                    customer_id            = 'ctm_01h8441jn5pcwrfhwh78jqt8hk',
                    address_id             = 'add_01h848pep46enq8y372x7maj0p',
                    business_id            = None,
                    currency_code          = CurrencyCode.GBP,
                    next_billed_at         = DateTime('2023-11-06 14:00:00'),
                    collection_mode        = CollectionMode.Automatic,
                    billing_details        = None,
                    scheduled_change       = None,
                    proration_billing_mode = SubscriptionProrationBillingMode.FullImmediately,
                    custom_data            = CustomData({'early_access': True}),
                    discount               = SubscriptionDiscount(
                        'dsc_01h848pep46enq8y372x7maj0p',
                        SubscriptionEffectiveFrom.NextBillingPeriod,
                    ),
                    items = [
                        SubscriptionItems('pri_01gsz91wy9k1yn7kx82aafwvea', 1),
                        SubscriptionItems('pri_01gsz91wy9k1yn7kx82bafwvea', 5),
                    ],
                ),
                ReadsFixtures.read_raw_json_fixture('request/preview_update_full'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/preview_update_full_entity'),
                '/subscriptions/sub_01h8bx8fmywym11t6swgzba704/preview',
            ),
        ],
        ids=[
            "Preview updating a subscription with a single new value",
            "Preview updating a subscription with partial new values",
            "Preview updating a subscription with all new values",
        ],
    )
    def test_preview_update_subscription_uses_expected_payload(
        self,
        test_client,
        mock_requests,
        subscription_id,
        operation,
        expected_request_body,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.patch(expected_url, status_code=expected_response_status, text=expected_response_body)

        response      = test_client.client.subscriptions.preview_update(subscription_id, operation)
        response_json = test_client.client.subscriptions.response.json()
        request_json  = test_client.client.payload
        last_request  = mock_requests.last_request

        assert isinstance(response, SubscriptionPreview)
        assert last_request is not None
        assert last_request.method            == 'PATCH'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"
        assert loads(request_json) == loads(expected_request_body), \
            "The request JSON doesn't match the expected fixture JSON"
        assert response_json == loads(str(expected_response_body)), \
            "The response JSON doesn't match the expected fixture JSON"


    @mark.parametrize(
        'subscription_id, operation, expected_request_body, expected_response_status, expected_response_body, expected_url',
        [
            (
                'sub_01h8bx8fmywym11t6swgzba704',
                PreviewOneTimeCharge(
                    SubscriptionEffectiveFrom.NextBillingPeriod,
                    [SubscriptionItems('pri_01gsz98e27ak2tyhexptwc58yk', 1)]
                ),
                ReadsFixtures.read_raw_json_fixture('request/preview_one_time_charge_minimal'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/preview_update_full_entity'),
                '/subscriptions/sub_01h8bx8fmywym11t6swgzba704/charge/preview',
            ), (
                'sub_01h8bx8fmywym11t6swgzba704',
                PreviewOneTimeCharge(
                    SubscriptionEffectiveFrom.Immediately,
                    [
                        SubscriptionItems('pri_01gsz98e27ak2tyhexptwc58yk', 1),
                        SubscriptionItems('pri_01h7zdqstxe6djaefkqbkjy4k2', 10),
                        SubscriptionItems('pri_01h7zd9mzfq79850w4ryc39v38', 845),
                    ],
                ),
                ReadsFixtures.read_raw_json_fixture('request/preview_one_time_charge_full'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/preview_update_full_entity'),
                '/subscriptions/sub_01h8bx8fmywym11t6swgzba704/charge/preview',
            ),
        ],
        ids=[
            "Preview creating a subscription one-time payment for one item effective next billing period",
            "Preview creating a subscription one-time payment for multiple items effective immediately",
        ],
    )
    def test_preview_create_subscription_one_time_charge_uses_expected_payload(
        self,
        test_client,
        mock_requests,
        subscription_id,
        operation,
        expected_request_body,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.post(expected_url, status_code=expected_response_status, text=expected_response_body)

        response      = test_client.client.subscriptions.preview_one_time_charge(subscription_id, operation)
        response_json = test_client.client.subscriptions.response.json()
        request_json  = test_client.client.payload
        last_request  = mock_requests.last_request

        assert isinstance(response, SubscriptionPreview)
        assert last_request is not None
        assert last_request.method            == 'POST'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"
        assert loads(request_json) == loads(expected_request_body), \
            "The request JSON doesn't match the expected fixture JSON"
        assert response_json == loads(str(expected_response_body)), \
            "The response JSON doesn't match the expected fixture JSON"
