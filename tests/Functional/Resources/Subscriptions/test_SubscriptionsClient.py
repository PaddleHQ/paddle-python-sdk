from json         import loads
from pytest       import mark
from urllib.parse import unquote

from paddle_billing_python_sdk.Entities.Collections.SubscriptionWithIncludesCollection import SubscriptionWithIncludesCollection

from paddle_billing_python_sdk.Entities.DateTime                 import DateTime
from paddle_billing_python_sdk.Entities.Subscription             import Subscription
from paddle_billing_python_sdk.Entities.SubscriptionPreview      import SubscriptionPreview
from paddle_billing_python_sdk.Entities.SubscriptionWithIncludes import SubscriptionWithIncludes

from paddle_billing_python_sdk.Entities.Shared.CollectionMode    import CollectionMode
from paddle_billing_python_sdk.Entities.Shared.CurrencyCode      import CurrencyCode
from paddle_billing_python_sdk.Entities.Shared.CustomData        import CustomData

from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionEffectiveFrom         import SubscriptionEffectiveFrom
from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionItems                 import SubscriptionItems
from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionOnPaymentFailure      import SubscriptionOnPaymentFailure
from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionProrationBillingMode  import SubscriptionProrationBillingMode
from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionScheduledChangeAction import SubscriptionScheduledChangeAction
from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionStatus                import SubscriptionStatus

from paddle_billing_python_sdk.Resources.Shared.Operations.List.Comparator     import Comparator
from paddle_billing_python_sdk.Resources.Shared.Operations.List.DateComparison import DateComparison
from paddle_billing_python_sdk.Resources.Shared.Operations.List.Pager          import Pager

from paddle_billing_python_sdk.Resources.Subscriptions.Operations.CancelSubscription        import CancelSubscription
from paddle_billing_python_sdk.Resources.Subscriptions.Operations.CreateOneTimeCharge       import CreateOneTimeCharge
from paddle_billing_python_sdk.Resources.Subscriptions.Operations.Get.Includes              import Includes
from paddle_billing_python_sdk.Resources.Subscriptions.Operations.PauseSubscription         import PauseSubscription
from paddle_billing_python_sdk.Resources.Subscriptions.Operations.PreviewOneTimeCharge      import PreviewOneTimeCharge
from paddle_billing_python_sdk.Resources.Subscriptions.Operations.PreviewUpdateSubscription import PreviewUpdateSubscription
from paddle_billing_python_sdk.Resources.Subscriptions.Operations.ResumeSubscription        import ResumeSubscription
from paddle_billing_python_sdk.Resources.Subscriptions.Operations.UpdateSubscription        import UpdateSubscription

from paddle_billing_python_sdk.Resources.Subscriptions.Operations.ListSubscriptions           import ListSubscriptions
from paddle_billing_python_sdk.Resources.Subscriptions.Operations.Update.SubscriptionDiscount import SubscriptionDiscount

from tests.Utils.TestClient   import mock_requests, test_client
from tests.Utils.ReadsFixture import ReadsFixtures


class TestSubscriptionsClient:
    @mark.parametrize(
        'operation, expected_request_body, expected_response_status, expected_response_body, expected_url',
        [
            (
                UpdateSubscription(proration_billing_mode=SubscriptionProrationBillingMode.ProratedNextBillingPeriod),
                ReadsFixtures.read_raw_json_fixture('request/update_single'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/subscriptions/sub_01h8bx8fmywym11t6swgzba704',
            ), (
                UpdateSubscription(
                    proration_billing_mode = SubscriptionProrationBillingMode.FullImmediately,
                    scheduled_change       = None,
                ),
                ReadsFixtures.read_raw_json_fixture('request/update_partial'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/subscriptions/sub_01h8bx8fmywym11t6swgzba704',
            ), (
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
        ids = [
            "Update subscription with single new value",
            "Update subscription with partial new values",
            "Update subscription with all new values",
        ],
    )
    def test_update_subscription_uses_expected_payload(
        self,
        test_client,
        mock_requests,
        operation,
        expected_request_body,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.patch(expected_url, status_code=expected_response_status, text=expected_response_body)

        response      = test_client.client.subscriptions.update('sub_01h8bx8fmywym11t6swgzba704', operation)
        request_json  = test_client.client.payload
        response_json = test_client.client.subscriptions.response.json()
        last_request  = mock_requests.last_request

        assert isinstance(response, Subscription)
        assert last_request is not None
        assert last_request.method            == 'PATCH'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"
        assert loads(request_json) == loads(expected_request_body), \
            "The request JSON doesn't match the expected fixture JSON"
        assert response_json == loads(expected_response_body), \
            "The response JSON doesn't match the expected fixture JSON"


    @mark.parametrize(
        'subscription_id, includes, expected_response_status, expected_response_body, expected_url',
        [
            (
                'sub_01h7zcgmdc6tmwtjehp3sh7azf',
                None,
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/subscriptions/sub_01h7zcgmdc6tmwtjehp3sh7azf',
            ),
            (
                'sub_01h7zcgmdc6tmwtjehp3sh7azf',
                [Includes.NextTransaction],
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/subscriptions/sub_01h7zcgmdc6tmwtjehp3sh7azf?include=next_transaction',
            ),
        ],
        ids = [
            "Get subscriptions",
            "Get subscriptions with includes",
        ],
    )
    def test_get_transactions_returns_expected_response(
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

        response      = test_client.client.subscriptions.get(subscription_id=subscription_id, includes=includes)
        response_json = test_client.client.subscriptions.response.json()
        last_request  = mock_requests.last_request

        assert isinstance(response, SubscriptionWithIncludes)
        assert last_request is not None
        assert last_request.method            == 'GET'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(expected_response_body), \
            "The response JSON generated by ResponseParser() doesn't match the expected fixture JSON"
