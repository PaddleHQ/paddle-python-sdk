from json import loads
from pytest import mark
from urllib.parse import unquote

from paddle_billing.Json import PayloadEncoder
from paddle_billing.Entities.Collections import ClientTokenCollection
from paddle_billing.Entities.ClientToken import ClientToken
from paddle_billing.Entities.ClientTokens import ClientTokenStatus

from paddle_billing.Resources.ClientTokens.Operations import CreateClientToken, ListClientTokens, UpdateClientToken
from paddle_billing.Resources.Shared.Operations import Pager

from tests.Utils.ReadsFixture import ReadsFixtures


class TestClientTokensClient:
    @mark.parametrize(
        "operation, expected_request_body, expected_response_status, expected_response_body, expected_url",
        [
            (
                CreateClientToken(
                    "Pricing page integration",
                    None,
                ),
                ReadsFixtures.read_raw_json_fixture("request/create_basic"),
                200,
                ReadsFixtures.read_raw_json_fixture("response/minimal_entity"),
                "/client-tokens",
            ),
            (
                CreateClientToken(
                    "Pricing page integration",
                    None,
                ),
                ReadsFixtures.read_raw_json_fixture("request/create_null_description"),
                200,
                ReadsFixtures.read_raw_json_fixture("response/minimal_entity"),
                "/client-tokens",
            ),
            (
                CreateClientToken(
                    "Pricing page integration",
                    "Used to display prices and open checkout within our pricing page on our marketing domain.",
                ),
                ReadsFixtures.read_raw_json_fixture("request/create_full"),
                200,
                ReadsFixtures.read_raw_json_fixture("response/full_entity"),
                "/client-tokens",
            ),
        ],
        ids=[
            "Create client token with basic data",
            "Create client token with basic data - null description",
            "Create client token with full data",
        ],
    )
    def test_create_client_token_uses_expected_payload(
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

        response = test_client.client.client_tokens.create(operation)
        response_json = test_client.client.client_tokens.response.json()
        request_json = test_client.client.payload
        last_request = mock_requests.last_request

        assert isinstance(response, ClientToken)
        assert last_request is not None
        assert last_request.method == "POST"
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
        "client_token_id, operation, expected_request_body, expected_response_status, expected_response_body, expected_url",
        [
            (
                "ctkn_01ghbkd0frb9k95cnhwd1bxpvk",
                UpdateClientToken(status=ClientTokenStatus.Revoked),
                ReadsFixtures.read_raw_json_fixture("request/revoke"),
                200,
                ReadsFixtures.read_raw_json_fixture("response/revoked_entity"),
                "/client-tokens/ctkn_01ghbkd0frb9k95cnhwd1bxpvk",
            ),
        ],
        ids=["Revoke client token"],
    )
    def test_update_client_token_uses_expected_payload(
        self,
        test_client,
        mock_requests,
        client_token_id,
        operation,
        expected_request_body,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.patch(expected_url, status_code=expected_response_status, text=expected_response_body)

        response = test_client.client.client_tokens.update(client_token_id, operation)
        response_json = test_client.client.client_tokens.response.json()
        request_json = test_client.client.payload
        last_request = mock_requests.last_request

        assert isinstance(response, ClientToken)
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

    def test_revoke_client_token_uses_expected_payload(
        self,
        test_client,
        mock_requests,
    ):
        client_token_id = "ctkn_01ghbkd0frb9k95cnhwd1bxpvk"
        expected_request_body = ReadsFixtures.read_raw_json_fixture("request/revoke")
        expected_response_body = ReadsFixtures.read_raw_json_fixture("response/revoked_entity")
        expected_url = "/client-tokens/ctkn_01ghbkd0frb9k95cnhwd1bxpvk"

        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.patch(expected_url, status_code=200, text=expected_response_body)

        response = test_client.client.client_tokens.revoke(client_token_id)
        response_json = test_client.client.client_tokens.response.json()
        request_json = test_client.client.payload
        last_request = mock_requests.last_request

        assert isinstance(response, ClientToken)
        assert last_request is not None
        assert last_request.method == "PATCH"
        assert test_client.client.status_code == 200
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
        "operation, expected_response_status, expected_response_body, expected_url",
        [
            (
                ListClientTokens(),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_page_one"),
                "/client-tokens",
            ),
            (
                ListClientTokens(Pager()),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_page_one"),
                "/client-tokens?order_by=id[asc]&per_page=50",
            ),
            (
                ListClientTokens(Pager(after="ctkn_01ghbkd0frb9k95cnhwd1bxpvk")),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_page_one"),
                "/client-tokens?after=ctkn_01ghbkd0frb9k95cnhwd1bxpvk&order_by=id[asc]&per_page=50",
            ),
            (
                ListClientTokens(statuses=[ClientTokenStatus.Active]),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_page_one"),
                "/client-tokens?status=active",
            ),
            (
                ListClientTokens(statuses=[ClientTokenStatus.Revoked]),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_page_one"),
                "/client-tokens?status=revoked",
            ),
        ],
        ids=[
            "List client tokens without pagination",
            "List client tokens with default pagination",
            "List paginated client tokens after specified client token id",
            "List client tokens filtered by active status",
            "List client tokens filtered by revoked status",
        ],
    )
    def test_list_client_tokens_returns_expected_response(
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

        response = test_client.client.client_tokens.list(operation)
        last_request = mock_requests.last_request

        assert isinstance(response, ClientTokenCollection)
        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert loads(PayloadEncoder().encode(response.items[0])) == loads(expected_response_body)["data"][0]

    def test_list_client_tokens_can_paginate(
        self,
        test_client,
        mock_requests,
    ):
        mock_requests.get(
            f"{test_client.base_url}/client-tokens",
            status_code=200,
            text=ReadsFixtures.read_raw_json_fixture("response/list_page_one"),
        )

        mock_requests.get(
            f"{test_client.base_url}/client-tokens?after=ctkn_03ghbkd0frb9k95cnhwd1bxpvk",
            status_code=200,
            text=ReadsFixtures.read_raw_json_fixture("response/list_page_two"),
        )

        response = test_client.client.client_tokens.list()

        assert isinstance(response, ClientTokenCollection)

        all = []
        for client_token in response:
            all.append(client_token)

        assert len(all) == 6

    @mark.parametrize(
        "client_token_id, expected_response_status, expected_response_body, expected_url",
        [
            (
                "dsc_01h83xenpcfjyhkqr4x214m02x",
                200,
                ReadsFixtures.read_raw_json_fixture("response/full_entity"),
                "/client-tokens/dsc_01h83xenpcfjyhkqr4x214m02x",
            )
        ],
        ids=["Get client token"],
    )
    def test_get_client_tokens_returns_expected_response(
        self,
        test_client,
        mock_requests,
        client_token_id,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.get(expected_url, status_code=expected_response_status, text=expected_response_body)

        response = test_client.client.client_tokens.get(client_token_id)
        response_json = test_client.client.client_tokens.response.json()
        last_request = mock_requests.last_request

        assert isinstance(response, ClientToken)
        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(
            str(expected_response_body)
        ), "The response JSON generated by ResponseParser() doesn't match the expected fixture JSON"
