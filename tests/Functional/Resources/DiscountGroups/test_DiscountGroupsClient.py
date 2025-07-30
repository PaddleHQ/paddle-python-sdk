from json import dumps, loads
from pytest import mark
from urllib.parse import unquote

from paddle_billing.Client import PayloadEncoder
from paddle_billing.Entities.DiscountGroup import DiscountGroup, DiscountGroupStatus
from paddle_billing.Entities.Collections import DiscountGroupCollection

from paddle_billing.Resources.DiscountGroups.Operations import (
    CreateDiscountGroup,
    ListDiscountGroups,
    UpdateDiscountGroup,
)
from paddle_billing.Resources.Shared.Operations import Pager

from tests.Utils.ReadsFixture import ReadsFixtures


class TestDiscountsClient:
    @mark.parametrize(
        "operation, expected_request_body, expected_response_body",
        [
            (
                CreateDiscountGroup(
                    "Black Friday 2024",
                ),
                ReadsFixtures.read_raw_json_fixture("request/create_full"),
                ReadsFixtures.read_raw_json_fixture("response/full_entity"),
            ),
        ],
        ids=[
            "Create discount with full data",
        ],
    )
    def test_create_discount_uses_expected_payload(
        self,
        test_client,
        mock_requests,
        operation,
        expected_request_body,
        expected_response_body,
    ):
        expected_url = f"{test_client.base_url}/discount-groups"
        mock_requests.post(expected_url, status_code=201, text=expected_response_body)

        response = test_client.client.discount_groups.create(operation)
        response_json = test_client.client.discount_groups.response.json()
        request_json = test_client.client.payload
        last_request = mock_requests.last_request

        assert isinstance(response, DiscountGroup)
        assert last_request is not None
        assert last_request.method == "POST"
        assert test_client.client.status_code == 201
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert loads(request_json) == loads(
            expected_request_body
        ), "The request JSON doesn't match the expected fixture JSON"
        assert response_json == loads(
            str(expected_response_body)
        ), "The response JSON doesn't match the expected fixture JSON"
        assert (
            loads(dumps(response, cls=PayloadEncoder)) == loads(str(expected_response_body))["data"]
        ), "The discount group doesn't match the expected fixture JSON"

    @mark.parametrize(
        "operation, expected_response_body, expected_url",
        [
            (
                ListDiscountGroups(),
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/discount-groups",
            ),
            (
                ListDiscountGroups(Pager()),
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/discount-groups?order_by=id[asc]&per_page=50",
            ),
            (
                ListDiscountGroups(Pager(after="dsg_01gtf15svsqzgp9325ss4ebmwt")),
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/discount-groups?after=dsg_01gtf15svsqzgp9325ss4ebmwt&order_by=id[asc]&per_page=50",
            ),
            (
                ListDiscountGroups(ids=["dsg_01gtf15svsqzgp9325ss4ebmwt"]),
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/discount-groups?id=dsg_01gtf15svsqzgp9325ss4ebmwt",
            ),
            (
                ListDiscountGroups(ids=["dsg_01gtf15svsqzgp9325ss4ebmwt", "dsg_02gtf15svsqzgp9325ss4ebmwt"]),
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/discount-groups?id=dsg_01gtf15svsqzgp9325ss4ebmwt,dsg_02gtf15svsqzgp9325ss4ebmwt",
            ),
        ],
        ids=[
            "List discounts without pagination",
            "List discounts with default pagination",
            "List paginated discounts after specified discount id",
            "List discounts filtered by id",
            "List discounts filtered by multiple ids",
        ],
    )
    def test_list_discount_groups_returns_expected_response(
        self,
        test_client,
        mock_requests,
        operation,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.get(expected_url, status_code=200, text=expected_response_body)

        response = test_client.client.discount_groups.list(operation)
        response_json = test_client.client.discount_groups.response.json()
        last_request = mock_requests.last_request

        assert isinstance(response, DiscountGroupCollection)
        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == 200
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(
            str(expected_response_body)
        ), "The response JSON doesn't match the expected fixture JSON"

    @mark.parametrize(
        "discount_group_id, operation, expected_request_body, expected_response_status, expected_response_body, expected_url",
        [
            (
                "dsg_01gtf15svsqzgp9325ss4ebmwt",
                UpdateDiscountGroup(name="Some Discount Group"),
                ReadsFixtures.read_raw_json_fixture("request/update_partial"),
                200,
                ReadsFixtures.read_raw_json_fixture("response/full_entity"),
                "/discount-groups/dsg_01gtf15svsqzgp9325ss4ebmwt",
            ),
            (
                "dsg_01gtf15svsqzgp9325ss4ebmwt",
                UpdateDiscountGroup(name="Some Discount Group", status=DiscountGroupStatus.Archived),
                ReadsFixtures.read_raw_json_fixture("request/update_full"),
                200,
                ReadsFixtures.read_raw_json_fixture("response/full_entity"),
                "/discount-groups/dsg_01gtf15svsqzgp9325ss4ebmwt",
            ),
        ],
        ids=[
            "Update discount group with minimal",
            "Update discount with with full",
        ],
    )
    def test_update_discount_group_uses_expected_payload(
        self,
        test_client,
        mock_requests,
        discount_group_id,
        operation,
        expected_request_body,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.patch(expected_url, status_code=expected_response_status, text=expected_response_body)

        response = test_client.client.discount_groups.update(discount_group_id, operation)
        response_json = test_client.client.discount_groups.response.json()
        request_json = test_client.client.payload
        last_request = mock_requests.last_request

        assert isinstance(response, DiscountGroup)
        assert last_request is not None
        assert last_request.method == "PATCH"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert loads(request_json) == loads(
            expected_request_body
        ), "The request JSON doesn't match the expected fixture JSON"
        assert response_json == loads(
            str(expected_response_body)
        ), "The response JSON doesn't match the expected fixture JSON"

    @mark.parametrize(
        "discount_group_id, expected_request_body, expected_response_status, expected_response_body, expected_url",
        [
            (
                "dsg_01gtf15svsqzgp9325ss4ebmwt",
                ReadsFixtures.read_raw_json_fixture("request/archive"),
                200,
                ReadsFixtures.read_raw_json_fixture("response/full_entity"),
                "/discount-groups/dsg_01gtf15svsqzgp9325ss4ebmwt",
            ),
        ],
        ids=[
            "Archive discount group",
        ],
    )
    def test_archive_discount_group_uses_expected_payload(
        self,
        test_client,
        mock_requests,
        discount_group_id,
        expected_request_body,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.patch(expected_url, status_code=expected_response_status, text=expected_response_body)

        response = test_client.client.discount_groups.archive(discount_group_id)
        response_json = test_client.client.discount_groups.response.json()
        request_json = test_client.client.payload
        last_request = mock_requests.last_request

        assert isinstance(response, DiscountGroup)
        assert last_request is not None
        assert last_request.method == "PATCH"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert loads(request_json) == loads(
            expected_request_body
        ), "The request JSON doesn't match the expected fixture JSON"
        assert response_json == loads(
            str(expected_response_body)
        ), "The response JSON doesn't match the expected fixture JSON"

    @mark.parametrize(
        "discount_group_id, expected_response_status, expected_response_body, expected_url",
        [
            (
                "dsg_01gtf15svsqzgp9325ss4ebmwt",
                200,
                ReadsFixtures.read_raw_json_fixture("response/full_entity"),
                "/discount-groups/dsg_01gtf15svsqzgp9325ss4ebmwt",
            )
        ],
        ids=["Get discount group"],
    )
    def test_get_discount_group_returns_expected_response(
        self,
        test_client,
        mock_requests,
        discount_group_id,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.get(expected_url, status_code=expected_response_status, text=expected_response_body)

        response = test_client.client.discount_groups.get(discount_group_id)
        response_json = test_client.client.discount_groups.response.json()
        last_request = mock_requests.last_request

        assert isinstance(response, DiscountGroup)
        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(
            str(expected_response_body)
        ), "The response JSON generated by ResponseParser() doesn't match the expected fixture JSON"
