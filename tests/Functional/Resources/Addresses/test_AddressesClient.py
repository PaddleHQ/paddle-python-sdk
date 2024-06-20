from json         import loads, dumps
from pytest       import mark, raises
from urllib.parse import unquote

from paddle_billing.Entities.Address     import Address
from paddle_billing.Entities.Collections import AddressCollection
from paddle_billing.Entities.Shared      import CountryCode, CustomData, Status
from paddle_billing.Exceptions.ApiError  import ApiError

from paddle_billing.Resources.Addresses.Operations import CreateAddress, ListAddresses, UpdateAddress
from paddle_billing.Resources.Shared.Operations    import Pager

from requests.exceptions import RequestException, HTTPError

from tests.Utils.TestClient   import mock_requests, test_client
from tests.Utils.ReadsFixture import ReadsFixtures


class TestAddressesClient:
    @mark.parametrize(
        'customer_id, operation, expected_request_body, expected_response_status, expected_response_body, expected_url',
        [
            (
                'ctm_01h844p3h41s12zs5mn4axja51',
                CreateAddress(CountryCode.AG),
                ReadsFixtures.read_raw_json_fixture('request/create_basic'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/minimal_entity'),
                '/customers/ctm_01h844p3h41s12zs5mn4axja51/addresses',
            ), (
                'ctm_01h844p3h41s12zs5mn4axja51',
                CreateAddress(
                    country_code = CountryCode.US,
                    description  = 'Head Office',
                    first_line   = '4050 Jefferson Plaza, 41st Floor',
                    second_line  = None,
                    city         = 'New York',
                    postal_code  = '10021',
                    region       = 'NY',
                    custom_data  = CustomData({'shippable': True}),
                ),
                ReadsFixtures.read_raw_json_fixture('request/create_full'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/customers/ctm_01h844p3h41s12zs5mn4axja51/addresses',
            ),
        ],
        ids=[
            "Create address with basic data",
            "Create address with full data",
        ],
    )
    def test_create_address_uses_expected_payload(
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
        mock_requests.post(expected_url, status_code=expected_response_status, text=expected_response_body)

        response      = test_client.client.addresses.create(customer_id, operation)
        response_json = test_client.client.addresses.response.json()
        request_json  = test_client.client.payload
        last_request  = mock_requests.last_request

        assert isinstance(response, Address)
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
        [
            'customer_id',
            'operation',
            'expected_request_body',
            'expected_response_status',
            'expected_reason',
            'expected_response_body',
            'expected_url_path',
        ],
        [
            (
                'ctm_01h844p3h41s12zs5mn4axja51',
                CreateAddress(CountryCode.AG),
                ReadsFixtures.read_raw_json_fixture('request/create_basic'),
                400,
                'Bad Request',
                {
                    "error": {
                        "type": "request_error",
                        "code": "bad_request",
                        "detail": "Invalid request",
                        "documentation_url": "https://developer.paddle.com/v1/errors/shared/bad_request",
                        "errors": [
                        {
                            "field": "postal_code",
                            "message": "US postal_code must be 5 digits only"
                        }
                        ]
                    },
                    "meta": {
                        "request_id": "f00bb3ca-399d-4686-889c-50b028f4c911"
                    }
                },
                '/customers/ctm_01h844p3h41s12zs5mn4axja51/addresses'
            ),
        ],
        ids=[
            "Returns 400 response for postal code",
        ],
    )
    def test_create_address_returns_error_response(
        self,
        test_client,
        mock_requests,
        customer_id,
        operation,
        expected_request_body,
        expected_response_status,
        expected_reason,
        expected_response_body,
        expected_url_path,
    ):
        expected_url = f"{test_client.base_url}{expected_url_path}"
        mock_requests.post(expected_url, status_code=expected_response_status, text=dumps(expected_response_body), reason=expected_reason)

        with raises(ApiError) as exception_info:
            test_client.client.addresses.create(customer_id, operation)

        request_json = test_client.client.payload
        last_request = mock_requests.last_request
        api_error    = exception_info.value

        assert unquote(last_request.url) == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"

        assert loads(request_json) == loads(expected_request_body), \
            "The request JSON doesn't match the expected fixture JSON"

        assert isinstance(api_error, ApiError)
        assert isinstance(api_error, HTTPError)
        assert isinstance(api_error, RequestException)
        assert api_error.response.status_code == expected_response_status, 'Unexpected status code'
        assert api_error.error_type == expected_response_body['error']['type']
        assert api_error.error_code == expected_response_body['error']['code']
        assert api_error.detail == expected_response_body['error']['detail']
        assert api_error.docs_url == expected_response_body['error']['documentation_url']

        assert len(api_error.field_errors) == len(expected_response_body['error']['errors'])

        for i, expected_field_error in enumerate(expected_response_body['error']['errors']):
            assert api_error.field_errors[i].field == expected_field_error['field']
            assert api_error.field_errors[i].error == expected_field_error['message']

        assert str(api_error) == api_error.detail
        assert repr(api_error) == ("ApiError("
            f"error_type='{api_error.error_type}', "
            f"error_code='{api_error.error_code}', "
            f"detail='{api_error.detail}', "
            f"docs_url='{api_error.docs_url}', "
            f"field_errors={api_error.field_errors}"
            ")")


    @mark.parametrize(
        'customer_id, address_id, operation, expected_request_body, expected_response_status, expected_response_body, expected_url',
        [
            (
                'ctm_01h844p3h41s12zs5mn4axja51',
                'add_01h848pep46enq8y372x7maj0p',
                UpdateAddress(description='Head Office'),
                ReadsFixtures.read_raw_json_fixture('request/update_single'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/minimal_entity'),
                '/customers/ctm_01h844p3h41s12zs5mn4axja51/addresses/add_01h848pep46enq8y372x7maj0p',
            ), (
                'ctm_01h844p3h41s12zs5mn4axja51',
                'add_01h848pep46enq8y372x7maj0p',
                UpdateAddress(description='Head Office', city='New York'),
                ReadsFixtures.read_raw_json_fixture('request/update_partial'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/customers/ctm_01h844p3h41s12zs5mn4axja51/addresses/add_01h848pep46enq8y372x7maj0p',
            ), (
                'ctm_01h844p3h41s12zs5mn4axja51',
                'add_01h848pep46enq8y372x7maj0p',
                UpdateAddress(
                    description  = 'Head Office',
                    first_line   = '4050 Jefferson Plaza, 41st Floor',
                    second_line  = None,
                    city         = 'New York',
                    postal_code  = '10021',
                    region       = 'NY',
                    country_code = CountryCode.US,
                    custom_data  = CustomData({'shippable': True}),
                    status       = Status.Active,
                ),
                ReadsFixtures.read_raw_json_fixture('request/update_full'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/customers/ctm_01h844p3h41s12zs5mn4axja51/addresses/add_01h848pep46enq8y372x7maj0p',
            ),
        ],
        ids=[
            "Update address with basic data",
            "Update address with partial data",
            "Update address with full data",
        ],
    )
    def test_update_address_uses_expected_payload(
        self,
        test_client,
        mock_requests,
        customer_id,
        address_id,
        operation,
        expected_request_body,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.patch(expected_url, status_code=expected_response_status, text=expected_response_body)

        response      = test_client.client.addresses.update(customer_id, address_id, operation)
        response_json = test_client.client.addresses.response.json()
        request_json  = test_client.client.payload
        last_request  = mock_requests.last_request

        assert isinstance(response, Address)
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
        'customer_id, operation, expected_response_status, expected_response_body, expected_url',
        [
            (
                'ctm_01h8441jn5pcwrfhwh78jqt8hk',
                ListAddresses(),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/customers/ctm_01h8441jn5pcwrfhwh78jqt8hk/addresses',
            ), (
                'ctm_01h8441jn5pcwrfhwh78jqt8hk',
                ListAddresses(Pager()),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/customers/ctm_01h8441jn5pcwrfhwh78jqt8hk/addresses?order_by=id[asc]&per_page=50',
            ), (
                'ctm_01h8441jn5pcwrfhwh78jqt8hk',
                ListAddresses(Pager(after='add_01h848pep46enq8y372x7maj0p')),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/customers/ctm_01h8441jn5pcwrfhwh78jqt8hk/addresses?after=add_01h848pep46enq8y372x7maj0p&order_by=id[asc]&per_page=50',
            ), (
                'ctm_01h8441jn5pcwrfhwh78jqt8hk',
                ListAddresses(statuses=[Status.Archived]),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/customers/ctm_01h8441jn5pcwrfhwh78jqt8hk/addresses?status=archived',
            ), (
                'ctm_01h8441jn5pcwrfhwh78jqt8hk',
                ListAddresses(ids=['add_01h848pep46enq8y372x7maj0p']),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/customers/ctm_01h8441jn5pcwrfhwh78jqt8hk/addresses?id=add_01h848pep46enq8y372x7maj0p',
            ), (
                'ctm_01h8441jn5pcwrfhwh78jqt8hk',
                ListAddresses(ids=['add_01h8494f4w5rwfp8b12yqh8fp1', 'add_01h848pep46enq8y372x7maj0p']),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/customers/ctm_01h8441jn5pcwrfhwh78jqt8hk/addresses?id=add_01h8494f4w5rwfp8b12yqh8fp1,add_01h848pep46enq8y372x7maj0p',
            ), (
                'ctm_01h8441jn5pcwrfhwh78jqt8hk',
                ListAddresses(search='Office'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/customers/ctm_01h8441jn5pcwrfhwh78jqt8hk/addresses?search=Office',
            ),
        ],
        ids=[
            "List addresses without pagination",
            "List addresses with default pagination",
            "List paginated addresses after specified product id",
            "List addresses filtered by status",
            "List addresses filtered by id",
            "List addresses filtered by multiple ids",
            "List addresses with includes",
        ],
    )
    def test_list_addresses_returns_expected_response(
        self,
        test_client,
        mock_requests,
        customer_id,
        operation,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.get(expected_url, status_code=expected_response_status)

        response     = test_client.client.addresses.list(customer_id, operation)
        last_request = mock_requests.last_request

        assert isinstance(response, AddressCollection)
        assert last_request is not None
        assert last_request.method            == 'GET'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"


    @mark.parametrize(
        'customer_id, address_id, expected_response_status, expected_response_body, expected_url',
        [(
            'ctm_01h844p3h41s12zs5mn4axja51',
            'add_01h848pep46enq8y372x7maj0p',
            200,
            ReadsFixtures.read_raw_json_fixture('response/full_entity'),
            '/customers/ctm_01h844p3h41s12zs5mn4axja51/addresses/add_01h848pep46enq8y372x7maj0p',
        )],
        ids=[ "Get address"],
    )
    def test_get_addresses_returns_expected_response(
        self,
        test_client,
        mock_requests,
        customer_id,
        address_id,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.get(expected_url, status_code=expected_response_status, text=expected_response_body)

        response      = test_client.client.addresses.get(customer_id, address_id)
        response_json = test_client.client.addresses.response.json()
        last_request  = mock_requests.last_request

        assert isinstance(response, Address)
        assert last_request is not None
        assert last_request.method            == 'GET'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(str(expected_response_body)), \
            "The response JSON generated by ResponseParser() doesn't match the expected fixture JSON"
