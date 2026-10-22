from json import loads
from pytest import mark
from urllib.parse import unquote

from paddle_billing.Entities.Collections import VerificationCollection
from paddle_billing.Entities.Verification import Verification
from paddle_billing.Entities.Verifications import (
    VerificationStatus,
    VerificationStepKey,
    VerificationStepStatus,
    VerificationType,
)

from paddle_billing.Resources.Shared.Operations import Pager
from paddle_billing.Resources.Verifications.Operations import ListVerifications

from tests.Utils.ReadsFixture import ReadsFixtures


class TestVerificationsClient:
    @mark.parametrize(
        "operation, expected_url",
        [
            (ListVerifications(), "/verifications"),
            (ListVerifications(Pager()), "/verifications?order_by=id[asc]&per_page=50"),
            (
                ListVerifications(Pager(after="slrvrf_01jjr5d4c14h4y3lqlk9bedkw7")),
                "/verifications?after=slrvrf_01jjr5d4c14h4y3lqlk9bedkw7&order_by=id[asc]&per_page=50",
            ),
            (
                ListVerifications(ids=["slrvrf_01jjr5d4c14h4y3lqlk9bedkw7", "slrvrf_01jjr5d4c14h4y3lqlk9bedkw6"]),
                "/verifications?id=slrvrf_01jjr5d4c14h4y3lqlk9bedkw7,slrvrf_01jjr5d4c14h4y3lqlk9bedkw6",
            ),
            (
                ListVerifications(verification_type=VerificationType.Onboarding),
                "/verifications?verification_type=onboarding",
            ),
        ],
        ids=[
            "List verifications without pagination",
            "List verifications with default pagination",
            "List paginated verifications after specified id",
            "List verifications filtered by ids",
            "List verifications filtered by type",
        ],
    )
    def test_list_verifications_returns_expected_response(self, test_client, mock_requests, operation, expected_url):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.get(
            expected_url, status_code=200, text=ReadsFixtures.read_raw_json_fixture("response/list_default")
        )

        response = test_client.client.verifications.list(operation)
        last_request = mock_requests.last_request

        assert isinstance(response, VerificationCollection)
        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == 200
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"

        verifications = list(response)
        assert len(verifications) == 2
        assert verifications[1].status == VerificationStatus.Canceled
        assert verifications[1].verification_type == VerificationType.Domain
        assert verifications[1].steps[0].status == VerificationStepStatus.Canceled

    def test_list_verifications_can_paginate(self, test_client, mock_requests):
        mock_requests.get(
            f"{test_client.base_url}/verifications",
            status_code=200,
            text=ReadsFixtures.read_raw_json_fixture("response/list_paginated_page_one"),
        )
        mock_requests.get(
            f"{test_client.base_url}/verifications?after=slrvrf_01jjr5d4c14h4y3lqlk9bedkw6",
            status_code=200,
            text=ReadsFixtures.read_raw_json_fixture("response/list_paginated_page_two"),
        )

        response = test_client.client.verifications.list()

        assert isinstance(response, VerificationCollection)
        assert len(list(response)) == 2

    def test_get_verification_returns_expected_response(self, test_client, mock_requests):
        expected_body = ReadsFixtures.read_raw_json_fixture("response/full_entity")
        expected_url = f"{test_client.base_url}/verifications/slrvrf_01jjr5d4c14h4y3lqlk9bedkw7"
        mock_requests.get(expected_url, status_code=200, text=expected_body)

        response = test_client.client.verifications.get("slrvrf_01jjr5d4c14h4y3lqlk9bedkw7")
        response_json = test_client.client.verifications.response.json()
        last_request = mock_requests.last_request

        assert isinstance(response, Verification)
        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == 200
        assert unquote(last_request.url) == expected_url
        assert response_json == loads(str(expected_body))

        assert response.id == "slrvrf_01jjr5d4c14h4y3lqlk9bedkw7"
        assert response.status == VerificationStatus.ActionRequired
        assert response.verification_type == VerificationType.Onboarding
        assert len(response.steps) == 4
        assert response.steps[0].key == VerificationStepKey.AccountSetup
        assert response.steps[0].expires_at is None
        assert response.steps[2].key == VerificationStepKey.BusinessIdentification
        assert response.steps[2].status == VerificationStepStatus.ActionRequired
        assert response.steps[2].expires_at is not None
        assert response.steps[2].expires_at.year == 2025
        assert response.steps[3].status == VerificationStepStatus.Canceled
