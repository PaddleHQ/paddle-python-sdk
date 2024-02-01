from json         import loads
from pytest       import mark
from urllib.parse import unquote

from paddle_billing.Entities.Collections import CreditBalanceCollection, CustomerCollection
from paddle_billing.Entities.Customer    import Customer
from paddle_billing.Entities.Shared      import CustomData, Status

from paddle_billing.Resources.Customers.Operations import CreateCustomer, ListCustomers, UpdateCustomer
from paddle_billing.Resources.Shared.Operations    import Pager

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
        ids=[
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
        response_json = test_client.client.customers.response.json()
        request_json  = test_client.client.payload
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


    @mark.parametrize(
        'customer_id, operation, expected_request_body, expected_response_status, expected_response_body, expected_url',
        [
            (
                'ctm_01h844p3h41s12zs5mn4axja51',
                UpdateCustomer(name='Alex Wilson'),
                ReadsFixtures.read_raw_json_fixture('request/update_single'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/customers/ctm_01h844p3h41s12zs5mn4axja51',
            ), (
                'ctm_01h844p3h41s12zs5mn4axja51',
                UpdateCustomer(name='Alex Wilson', email='test1@example.com'),
                ReadsFixtures.read_raw_json_fixture('request/update_partial'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/customers/ctm_01h844p3h41s12zs5mn4axja51',
            ), (
                'ctm_01h844p3h41s12zs5mn4axja51',
                UpdateCustomer(
                    name        ='Alex Wilson',
                    email       ='test1@example.com',
                    locale      = 'el',
                    custom_data = CustomData({'customer_reference_id': 'abcd1234'}),
                    status      = Status.Active,
                ),
                ReadsFixtures.read_raw_json_fixture('request/update_full'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/customers/ctm_01h844p3h41s12zs5mn4axja51',
            ),
        ],
        ids=[
            "Update customer with single new value",
            "Update customer with partial new values",
            "Update customer with all new values",
        ],
    )
    def test_update_customer_uses_expected_payload(
        self,
        test_client,
        mock_requests,
        customer_id,
        operation,
        expected_request_body,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.patch(expected_url, status_code=expected_response_status, text=expected_response_body)

        response      = test_client.client.customers.update(customer_id, operation)
        response_json = test_client.client.customers.response.json()
        request_json  = test_client.client.payload
        last_request  = mock_requests.last_request

        assert isinstance(response, Customer)
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
                ListCustomers(),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/customers',
            ), (
                ListCustomers(Pager()),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/customers?order_by=id[asc]&per_page=50',
            ), (
                ListCustomers(Pager(after='ctm_01h8441jn5pcwrfhwh78jqt8hk')),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/customers?after=ctm_01h8441jn5pcwrfhwh78jqt8hk&order_by=id[asc]&per_page=50',
            ), (
                ListCustomers(statuses=[Status.Archived]),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/customers?status=archived',
            ), (
                ListCustomers(ids=['ctm_01h8441jn5pcwrfhwh78jqt8hk']),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/customers?id=ctm_01h8441jn5pcwrfhwh78jqt8hk',
            ), (
                ListCustomers(ids=['ctm_01h8441jn5pcwrfhwh78jqt8hk', 'ctm_01h844p3h41s12zs5mn4axja51']),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/customers?id=ctm_01h8441jn5pcwrfhwh78jqt8hk,ctm_01h844p3h41s12zs5mn4axja51',
            ), (
                ListCustomers(search='Alex'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/customers?search=Alex',
            ), (
                ListCustomers(emails=['dx@paddle.com']),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/customers?email=dx@paddle.com',
            ),
        ],
        ids=[
            "List customers without pagination",
            "List customers with default pagination",
            "List paginated customers after specified transaction_id",
            "List customers filtered by status",
            "List customers filtered by id",
            "List customers filtered by multiple ids",
            "List customers filtered by search term",
            "List customers filtered by email addresses",
        ],
    )
    def test_list_customers_returns_expected_response(
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

        response     = test_client.client.customers.list(operation)
        last_request = mock_requests.last_request

        assert isinstance(response, CustomerCollection)
        assert last_request is not None
        assert last_request.method            == 'GET'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"


    @mark.parametrize(
        'customer_id, expected_response_status, expected_response_body, expected_url',
        [(
            'ctm_01h8441jn5pcwrfhwh78jqt8hk',
            200,
            ReadsFixtures.read_raw_json_fixture('response/full_entity'),
            '/customers/ctm_01h8441jn5pcwrfhwh78jqt8hk',
        )],
        ids=["Get customer by its id"],
    )
    def test_get_customers_returns_expected_response(
        self,
        test_client,
        mock_requests,
        customer_id,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.get(expected_url, status_code=expected_response_status, text=expected_response_body)

        response      = test_client.client.customers.get(customer_id)
        response_json = test_client.client.customers.response.json()
        last_request  = mock_requests.last_request

        assert isinstance(response, Customer)
        assert last_request is not None
        assert last_request.method            == 'GET'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(str(expected_response_body)), \
            "The response JSON generated by ResponseParser() doesn't match the expected fixture JSON"


    @mark.parametrize(
        'customer_id, expected_response_status, expected_response_body, expected_url',
        [(
            'ctm_01h8441jn5pcwrfhwh78jqt8hk',
            200,
            ReadsFixtures.read_raw_json_fixture('response/list_credit_balances'),
            '/customers/ctm_01h8441jn5pcwrfhwh78jqt8hk/credit-balances',
        )],
        ids=["List a customer's credit balances"],
    )
    def test_list_credit_balance_customers_returns_expected_response(
        self,
        test_client,
        mock_requests,
        customer_id,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.get(expected_url, status_code=expected_response_status, text=expected_response_body)

        response      = test_client.client.customers.credit_balances(customer_id)
        response_json = test_client.client.customers.response.json()
        last_request  = mock_requests.last_request

        assert isinstance(response, CreditBalanceCollection)
        assert last_request is not None
        assert last_request.method            == 'GET'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(str(expected_response_body)), \
            "The response JSON generated by ResponseParser() doesn't match the expected fixture JSON"
