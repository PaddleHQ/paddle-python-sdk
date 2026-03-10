from json import loads
from pytest import mark
from urllib.parse import unquote

import respx

from paddle_billing.Entities.Address import Address
from paddle_billing.Entities.Collections import AddressCollection
from paddle_billing.Entities.Shared import CountryCode, CustomData, Status

from paddle_billing.Resources.Addresses.Operations import CreateAddress, ListAddresses, UpdateAddress
from paddle_billing.Resources.Shared.Operations import Pager

from tests.Utils.ReadsFixture import ReadsFixtures


CUSTOMER_ID = "ctm_01h844p3h41s12zs5mn4axja51"
ADDRESS_ID = "add_01h848pep46enq8y372x7maj0p"


class TestAsyncAddressesClient:
    @mark.parametrize(
        "customer_id, operation, expected_request_body, expected_response_status, expected_response_body, expected_url",
        [
            (
                CUSTOMER_ID,
                CreateAddress(CountryCode.AG),
                ReadsFixtures.read_raw_json_fixture("request/create_basic"),
                200,
                ReadsFixtures.read_raw_json_fixture("response/minimal_entity"),
                f"/customers/{CUSTOMER_ID}/addresses",
            ),
            (
                CUSTOMER_ID,
                CreateAddress(
                    country_code=CountryCode.US,
                    description="Head Office",
                    first_line="4050 Jefferson Plaza, 41st Floor",
                    second_line=None,
                    city="New York",
                    postal_code="10021",
                    region="NY",
                    custom_data=CustomData({"shippable": True}),
                ),
                ReadsFixtures.read_raw_json_fixture("request/create_full"),
                200,
                ReadsFixtures.read_raw_json_fixture("response/full_entity"),
                f"/customers/{CUSTOMER_ID}/addresses",
            ),
        ],
        ids=[
            "Create address with basic data",
            "Create address with full data",
        ],
    )
    async def test_create_address_uses_expected_payload(
        self,
        async_test_client,
        customer_id,
        operation,
        expected_request_body,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{async_test_client.base_url}{expected_url}"

        with respx.mock() as mock:
            mock.post(expected_url).respond(
                status_code=expected_response_status,
                json=loads(expected_response_body),
            )

            response = await async_test_client.client.addresses.create(customer_id, operation)
            response_json = async_test_client.client.addresses.response.json()
            request_json = async_test_client.client.payload
            last_request = mock.calls.last.request

        assert isinstance(response, Address)
        assert last_request is not None
        assert last_request.method == "POST"
        assert async_test_client.client.status_code == expected_response_status
        assert (
            unquote(str(last_request.url)) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert loads(request_json) == loads(
            expected_request_body
        ), "The request JSON doesn't match the expected fixture JSON"
        assert response_json == loads(
            str(expected_response_body)
        ), "The response JSON doesn't match the expected fixture JSON"

    @mark.parametrize(
        "customer_id, address_id, operation, expected_request_body, expected_response_status, expected_response_body, expected_url",
        [
            (
                CUSTOMER_ID,
                ADDRESS_ID,
                UpdateAddress(description="Head Office"),
                ReadsFixtures.read_raw_json_fixture("request/update_single"),
                200,
                ReadsFixtures.read_raw_json_fixture("response/full_entity"),
                f"/customers/{CUSTOMER_ID}/addresses/{ADDRESS_ID}",
            ),
            (
                CUSTOMER_ID,
                ADDRESS_ID,
                UpdateAddress(
                    description="Head Office",
                    first_line="4050 Jefferson Plaza, 41st Floor",
                    second_line=None,
                    city="New York",
                    postal_code="10021",
                    region="NY",
                    country_code=CountryCode.US,
                    custom_data=CustomData({"shippable": True}),
                    status=Status.Active,
                ),
                ReadsFixtures.read_raw_json_fixture("request/update_full"),
                200,
                ReadsFixtures.read_raw_json_fixture("response/full_entity"),
                f"/customers/{CUSTOMER_ID}/addresses/{ADDRESS_ID}",
            ),
        ],
        ids=[
            "Update address with single new value",
            "Update address with completely new values",
        ],
    )
    async def test_update_address_uses_expected_payload(
        self,
        async_test_client,
        customer_id,
        address_id,
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

            response = await async_test_client.client.addresses.update(customer_id, address_id, operation)
            response_json = async_test_client.client.addresses.response.json()
            request_json = async_test_client.client.payload
            last_request = mock.calls.last.request

        assert isinstance(response, Address)
        assert last_request is not None
        assert last_request.method == "PATCH"
        assert async_test_client.client.status_code == expected_response_status
        assert (
            unquote(str(last_request.url)) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert loads(request_json) == loads(
            expected_request_body
        ), "The request JSON doesn't match the expected fixture JSON"
        assert response_json == loads(
            str(expected_response_body)
        ), "The response JSON doesn't match the expected fixture JSON"

    @mark.parametrize(
        "customer_id, operation, expected_response_status, expected_response_body, expected_url",
        [
            (
                CUSTOMER_ID,
                ListAddresses(),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                f"/customers/{CUSTOMER_ID}/addresses",
            ),
            (
                CUSTOMER_ID,
                ListAddresses(Pager()),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                f"/customers/{CUSTOMER_ID}/addresses?order_by=id[asc]&per_page=50",
            ),
            (
                CUSTOMER_ID,
                ListAddresses(statuses=[Status.Archived]),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                f"/customers/{CUSTOMER_ID}/addresses?status=archived",
            ),
        ],
        ids=[
            "List addresses without pagination",
            "List addresses with default pagination",
            "List addresses filtered by status",
        ],
    )
    async def test_list_addresses_returns_expected_response(
        self,
        async_test_client,
        customer_id,
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

            response = await async_test_client.client.addresses.list(customer_id, operation)
            last_request = mock.calls.last.request

        assert isinstance(response, AddressCollection)
        assert last_request is not None
        assert last_request.method == "GET"
        assert async_test_client.client.status_code == expected_response_status
        assert (
            unquote(str(last_request.url)) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"

    async def test_get_address_returns_expected_response(self, async_test_client):
        expected_url = f"{async_test_client.base_url}/customers/{CUSTOMER_ID}/addresses/{ADDRESS_ID}"
        response_body = ReadsFixtures.read_raw_json_fixture("response/full_entity")

        with respx.mock() as mock:
            mock.get(expected_url).respond(status_code=200, json=loads(response_body))

            response = await async_test_client.client.addresses.get(CUSTOMER_ID, ADDRESS_ID)
            response_json = async_test_client.client.addresses.response.json()
            last_request = mock.calls.last.request

        assert isinstance(response, Address)
        assert last_request.method == "GET"
        assert async_test_client.client.status_code == 200
        assert response_json == loads(response_body)

    async def test_archive_address_sends_patch_with_archived_status(self, async_test_client):
        expected_url = f"{async_test_client.base_url}/customers/{CUSTOMER_ID}/addresses/{ADDRESS_ID}"
        response_body = ReadsFixtures.read_raw_json_fixture("response/full_entity")

        with respx.mock() as mock:
            mock.patch(expected_url).respond(status_code=200, json=loads(response_body))

            response = await async_test_client.client.addresses.archive(CUSTOMER_ID, ADDRESS_ID)
            request_json = async_test_client.client.payload
            last_request = mock.calls.last.request

        assert isinstance(response, Address)
        assert last_request.method == "PATCH"
        assert loads(request_json) == {"status": "archived"}
