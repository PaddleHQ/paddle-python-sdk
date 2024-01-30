from json         import loads
from pytest       import mark
from urllib.parse import unquote

from paddle_billing_python_sdk.Entities.Collections.SubscriptionWithIncludesCollection import SubscriptionWithIncludesCollection

from paddle_billing_python_sdk.Entities.Customer                 import Customer
from paddle_billing_python_sdk.Entities.CustomerIncludes         import CustomerIncludes
from paddle_billing_python_sdk.Entities.DateTime                 import DateTime
from paddle_billing_python_sdk.Entities.Subscription             import Subscription
from paddle_billing_python_sdk.Entities.SubscriptionPreview      import SubscriptionPreview
from paddle_billing_python_sdk.Entities.SubscriptionWithIncludes import SubscriptionWithIncludes

from paddle_billing_python_sdk.Entities.Shared.CollectionMode import CollectionMode
from paddle_billing_python_sdk.Entities.Shared.CurrencyCode   import CurrencyCode
from paddle_billing_python_sdk.Entities.Shared.CustomData     import CustomData

from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionEffectiveFrom         import SubscriptionEffectiveFrom
from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionItems                 import SubscriptionItems
from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionOnPaymentFailure      import SubscriptionOnPaymentFailure
from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionProrationBillingMode  import SubscriptionProrationBillingMode
from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionScheduledChangeAction import SubscriptionScheduledChangeAction
from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionStatus                import SubscriptionStatus

from paddle_billing_python_sdk.Resources.Shared.Operations.List.Pager import Pager

from paddle_billing_python_sdk.Resources.Customers.Operations.CreateCustomer import CreateCustomer
from paddle_billing_python_sdk.Resources.Customers.Operations.ListCustomers  import ListCustomers
from paddle_billing_python_sdk.Resources.Customers.Operations.UpdateCustomer import UpdateCustomer

from paddle_billing_python_sdk.Resources.Subscriptions.Operations.ListSubscriptions           import ListSubscriptions
from paddle_billing_python_sdk.Resources.Subscriptions.Operations.Update.SubscriptionDiscount import SubscriptionDiscount

from tests.Utils.TestClient   import mock_requests, test_client
from tests.Utils.ReadsFixture import ReadsFixtures


class TestCustomersClient:
    @mark.parametrize(
        'operation, expected_request_body, expected_response_status, expected_response_body, expected_url',
        [
            (
                CreateCustomer('test2@example.com'),
                ReadsFixtures.read_raw_json_fixture('request/create_basic'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/minimal_entity'),
                '/customers',
            ), (
                CreateCustomer(
                    email       = 'test2@example.com',
                    name        = 'Alex Wilson',
                    custom_data = CustomData({'customer_reference_id': 'abcd1234'}),
                    locale      = 'en',
                ),
                ReadsFixtures.read_raw_json_fixture('request/create_full'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/customers',
            ),
        ],
        ids = [
            "Create customer with just an email address",
            "Create customer with basic information",
        ],
    )
    def test_create_customer_uses_expected_payload(
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
        mock_requests.post(expected_url, status_code=expected_response_status, text=expected_response_body)

        response      = test_client.client.customers.create(operation)
        request_json  = test_client.client.payload
        response_json = test_client.client.customers.response.json()
        last_request  = mock_requests.last_request

        assert isinstance(response, Customer)
        assert last_request is not None
        assert last_request.method            == 'POST'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"
        assert loads(request_json) == loads(expected_request_body), \
            "The request JSON doesn't match the expected fixture JSON"
        assert response_json == loads(str(expected_response_body)), \
            "The response JSON doesn't match the expected fixture JSON"













