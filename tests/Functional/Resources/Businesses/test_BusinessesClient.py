from json         import loads
from pytest       import mark
from urllib.parse import unquote

from paddle_billing.Entities.Business    import Business
from paddle_billing.Entities.Collections import BusinessCollection
from paddle_billing.Entities.Shared      import Contacts, CustomData, Status

from paddle_billing.Resources.Businesses.Operations import CreateBusiness, ListBusinesses, UpdateBusiness
from paddle_billing.Resources.Shared.Operations     import Pager

from tests.Utils.TestClient   import mock_requests, test_client
from tests.Utils.ReadsFixture import ReadsFixtures


class TestBusinessesClient:
    @mark.parametrize(
        'customer_id, operation, expected_request_body, expected_response_status, expected_response_body, expected_url',
        [
            (
                'ctm_01h844p3h41s12zs5mn4axja51',
                CreateBusiness('ChatApp Inc.'),
                ReadsFixtures.read_raw_json_fixture('request/create_basic'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/minimal_entity'),
                '/customers/ctm_01h844p3h41s12zs5mn4axja51/businesses',
            ), (
                'ctm_01h844p3h41s12zs5mn4axja51',
                CreateBusiness(
                    name           = 'ChatApp Inc.',
                    company_number = '555775291485',
                    tax_identifier = '555952383',
                    contacts       = [Contacts('Parker Jones', 'parker@example.com')],
                    custom_data    = CustomData({'customer_reference_id': 'abcd1234'}),
                ),
                ReadsFixtures.read_raw_json_fixture('request/create_full'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/customers/ctm_01h844p3h41s12zs5mn4axja51/businesses',
            ),
        ],
        ids=[
            "Create business with basic data",
            "Create business with full data",
        ],
    )
    def test_create_business_uses_expected_payload(
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

        response      = test_client.client.businesses.create(customer_id, operation)
        response_json = test_client.client.businesses.response.json()
        request_json  = test_client.client.payload
        last_request  = mock_requests.last_request

        assert isinstance(response, Business)
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
        'customer_id, business_id, operation, expected_request_body, expected_response_status, expected_response_body, expected_url',
        [
            (
                'ctm_01h844p3h41s12zs5mn4axja51',
                'biz_01h84a7hr4pzhsajkm8tev89ev',
                UpdateBusiness(name='ChatApp Inc.'),
                ReadsFixtures.read_raw_json_fixture('request/update_single'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/minimal_entity'),
                '/customers/ctm_01h844p3h41s12zs5mn4axja51/businesses/biz_01h84a7hr4pzhsajkm8tev89ev',
            ), (
                'ctm_01h844p3h41s12zs5mn4axja51',
                'biz_01h84a7hr4pzhsajkm8tev89ev',
                UpdateBusiness(
                    name     = 'ChatApp Inc.',
                    contacts = [
                        Contacts('Parker Jones', 'parker@example.com'),
                        Contacts('Jo Riley',     'jo@example.com'),
                        Contacts('Jesse Garcia', 'jo@example.com'),
                    ],
                ),
                ReadsFixtures.read_raw_json_fixture('request/update_partial'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/customers/ctm_01h844p3h41s12zs5mn4axja51/businesses/biz_01h84a7hr4pzhsajkm8tev89ev',
            ), (
                'ctm_01h844p3h41s12zs5mn4axja51',
                'biz_01h84a7hr4pzhsajkm8tev89ev',
                UpdateBusiness(
                    name           = 'ChatApp Inc.',
                    company_number = '555775291485',
                    tax_identifier = '555952383',
                    status         = Status.Active,
                    custom_data    = CustomData({'customer_reference_id': 'abcd1234'}),
                    contacts = [
                        Contacts('Parker Jones', 'parker@example.com'),
                        Contacts('Jo Riley',     'jo@example.com'),
                        Contacts('Jesse Garcia', 'jo@example.com'),
                    ],
                ),
                ReadsFixtures.read_raw_json_fixture('request/update_full'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/customers/ctm_01h844p3h41s12zs5mn4axja51/businesses/biz_01h84a7hr4pzhsajkm8tev89ev',
            ),
        ],
        ids=[
            "Update business with basic data",
            "Update business with partial data",
            "Update business with full data",
        ],
    )
    def test_update_business_uses_expected_payload(
        self,
        test_client,
        mock_requests,
        customer_id,
        business_id,
        operation,
        expected_request_body,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.patch(expected_url, status_code=expected_response_status, text=expected_response_body)

        response      = test_client.client.businesses.update(customer_id, business_id, operation)
        response_json = test_client.client.businesses.response.json()
        request_json  = test_client.client.payload
        last_request  = mock_requests.last_request

        assert isinstance(response, Business)
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
                ListBusinesses(),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/customers/ctm_01h8441jn5pcwrfhwh78jqt8hk/businesses',
            ), (
                'ctm_01h8441jn5pcwrfhwh78jqt8hk',
                ListBusinesses(Pager()),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/customers/ctm_01h8441jn5pcwrfhwh78jqt8hk/businesses?order_by=id[asc]&per_page=50',
            ), (
                'ctm_01h8441jn5pcwrfhwh78jqt8hk',
                ListBusinesses(Pager(after='biz_01h84a7hr4pzhsajkm8tev89ev')),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/customers/ctm_01h8441jn5pcwrfhwh78jqt8hk/businesses?after=biz_01h84a7hr4pzhsajkm8tev89ev&order_by=id[asc]&per_page=50',
            ), (
                'ctm_01h8441jn5pcwrfhwh78jqt8hk',
                ListBusinesses(statuses=[Status.Archived]),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/customers/ctm_01h8441jn5pcwrfhwh78jqt8hk/businesses?status=archived',
            ), (
                'ctm_01h8441jn5pcwrfhwh78jqt8hk',
                ListBusinesses(ids=['biz_01h84a7hr4pzhsajkm8tev89ev']),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/customers/ctm_01h8441jn5pcwrfhwh78jqt8hk/businesses?id=biz_01h84a7hr4pzhsajkm8tev89ev',
            ), (
                'ctm_01h8441jn5pcwrfhwh78jqt8hk',
                ListBusinesses(ids=['biz_01h84a7hr4pzhsajkm8tev89ev', 'biz_01hf6pv0tmnw1cs0bcj2z8nmqx']),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/customers/ctm_01h8441jn5pcwrfhwh78jqt8hk/businesses?id=biz_01h84a7hr4pzhsajkm8tev89ev,biz_01hf6pv0tmnw1cs0bcj2z8nmqx',
            ), (
                'ctm_01h8441jn5pcwrfhwh78jqt8hk',
                ListBusinesses(search='ChatApp'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/list_default'),
                '/customers/ctm_01h8441jn5pcwrfhwh78jqt8hk/businesses?search=ChatApp',
            ),
        ],
        ids=[
            "List businesses without pagination",
            "List businesses with default pagination",
            "List paginated businesses after specified product id",
            "List businesses filtered by status",
            "List businesses filtered by id",
            "List businesses filtered by multiple ids",
            "List businesses with includes",
        ],
    )
    def test_list_businesses_returns_expected_response(
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

        response     = test_client.client.businesses.list(customer_id, operation)
        last_request = mock_requests.last_request

        assert isinstance(response, BusinessCollection)
        assert last_request is not None
        assert last_request.method            == 'GET'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"


    @mark.parametrize(
        'customer_id, business_id, expected_response_status, expected_response_body, expected_url',
        [(
                'ctm_01h844p3h41s12zs5mn4axja51',
                'biz_01h84a7hr4pzhsajkm8tev89ev',
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/customers/ctm_01h844p3h41s12zs5mn4axja51/businesses/biz_01h84a7hr4pzhsajkm8tev89ev',
        )],
        ids=["Get a business by its id"],
    )
    def test_get_businesses_returns_expected_response(
        self,
        test_client,
        mock_requests,
        customer_id,
        business_id,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.get(expected_url, status_code=expected_response_status, text=expected_response_body)

        response      = test_client.client.businesses.get(customer_id, business_id)
        response_json = test_client.client.businesses.response.json()
        last_request  = mock_requests.last_request

        assert isinstance(response, Business)
        assert last_request is not None
        assert last_request.method            == 'GET'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(str(expected_response_body)), \
            "The response JSON generated by ResponseParser() doesn't match the expected fixture JSON"
