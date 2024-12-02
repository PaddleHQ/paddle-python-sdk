from json import loads
from pytest import mark
from urllib.parse import unquote

from paddle_billing.Entities.CustomerPortalSession import CustomerPortalSession
from paddle_billing.Entities.CustomerPortalSessions import (
    CustomerPortalSessionUrls,
    CustomerPortalSessionGeneralUrl,
    CustomerPortalSessionSubscriptionUrl,
)

from paddle_billing.Resources.CustomerPortalSessions.Operations import CreateCustomerPortalSession

from tests.Utils.ReadsFixture import ReadsFixtures


class TestAddressesClient:
    @mark.parametrize(
        "customer_id, operation, expected_request_body, expected_response_body, expected_path",
        [
            (
                "ctm_01gysfvfy7vqhpzkq8rjmrq7an",
                CreateCustomerPortalSession(["sub_01h04vsc0qhwtsbsxh3422wjs4"]),
                ReadsFixtures.read_raw_json_fixture("request/create_single"),
                ReadsFixtures.read_raw_json_fixture("response/full_entity_single"),
                "/customers/ctm_01gysfvfy7vqhpzkq8rjmrq7an/portal-sessions",
            ),
            (
                "ctm_01gysfvfy7vqhpzkq8rjmrq7an",
                CreateCustomerPortalSession(["sub_01h04vsc0qhwtsbsxh3422wjs4", "sub_02h04vsc0qhwtsbsxh3422wjs4"]),
                ReadsFixtures.read_raw_json_fixture("request/create_multiple"),
                ReadsFixtures.read_raw_json_fixture("response/full_entity_multiple"),
                "/customers/ctm_01gysfvfy7vqhpzkq8rjmrq7an/portal-sessions",
            ),
        ],
        ids=[
            "Create portal session with single subscription ID",
            "Create portal session with multiple subscription IDs",
        ],
    )
    def test_create_uses_expected_payload(
        self,
        test_client,
        mock_requests,
        customer_id,
        operation,
        expected_request_body,
        expected_response_body,
        expected_path,
    ):
        expected_url = f"{test_client.base_url}{expected_path}"
        mock_requests.post(expected_url, status_code=201, text=expected_response_body)

        response = test_client.client.customer_portal_sessions.create(customer_id, operation)
        response_json = test_client.client.customer_portal_sessions.response.json()
        request_json = test_client.client.payload
        last_request = mock_requests.last_request

        assert isinstance(response, CustomerPortalSession)
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

    def test_create_returns_expected_response(
        self,
        test_client,
        mock_requests,
    ):
        customer_id = "ctm_01gysfvfy7vqhpzkq8rjmrq7an"
        expected_path = "/customers/ctm_01gysfvfy7vqhpzkq8rjmrq7an/portal-sessions"
        expected_response_body = ReadsFixtures.read_raw_json_fixture("response/full_entity_multiple")

        expected_url = f"{test_client.base_url}{expected_path}"
        mock_requests.post(expected_url, status_code=201, text=expected_response_body)

        response = test_client.client.customer_portal_sessions.create(
            customer_id,
            CreateCustomerPortalSession(["sub_01h04vsc0qhwtsbsxh3422wjs4", "sub_02h04vsc0qhwtsbsxh3422wjs4"]),
        )

        assert isinstance(response, CustomerPortalSession)
        assert response.id == "cpls_01h4ge9r64c22exjsx0fy8b48b"
        assert response.customer_id == customer_id
        assert response.created_at.isoformat() == "2024-10-25T06:53:58+00:00"

        urls = response.urls
        assert isinstance(urls, CustomerPortalSessionUrls)

        general = urls.general
        assert isinstance(general, CustomerPortalSessionGeneralUrl)
        assert (
            general.overview
            == "https://customer-portal.paddle.com/cpl_01j7zbyqs3vah3aafp4jf62qaw?action=overview&token=pga_eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJjdG1fMDFncm5uNHp0YTVhMW1mMDJqanplN3kyeXMiLCJuYW1lIjoiSm9obiBEb2UiLCJpYXQiOjE3Mjc2NzkyMzh9._oO12IejzdKmyKTwb7BLjmiILkx4_cSyGjXraOBUI_g"
        )

        subscription1 = urls.subscriptions[0]
        assert isinstance(subscription1, CustomerPortalSessionSubscriptionUrl)
        assert subscription1.id == "sub_01h04vsc0qhwtsbsxh3422wjs4"
        assert (
            subscription1.cancel_subscription
            == "https://customer-portal.paddle.com/cpl_01j7zbyqs3vah3aafp4jf62qaw?action=cancel_subscription&subscription_id=sub_01h04vsc0qhwtsbsxh3422wjs4&token=pga_eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJjdG1fMDFncm5uNHp0YTVhMW1mMDJqanplN3kyeXMiLCJuYW1lIjoiSm9obiBEb2UiLCJpYXQiOjE3Mjc2NzkyMzh9._oO12IejzdKmyKTwb7BLjmiILkx4_cSyGjXraOBUI_g"
        )
        assert (
            subscription1.update_subscription_payment_method
            == "https://customer-portal.paddle.com/cpl_01j7zbyqs3vah3aafp4jf62qaw?action=update_subscription_payment_method&subscription_id=sub_01h04vsc0qhwtsbsxh3422wjs4&token=pga_eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJjdG1fMDFncm5uNHp0YTVhMW1mMDJqanplN3kyeXMiLCJuYW1lIjoiSm9obiBEb2UiLCJpYXQiOjE3Mjc2NzkyMzh9._oO12IejzdKmyKTwb7BLjmiILkx4_cSyGjXraOBUI_g"
        )

        subscription2 = urls.subscriptions[1]
        assert isinstance(subscription2, CustomerPortalSessionSubscriptionUrl)
        assert subscription2.id == "sub_02h04vsc0qhwtsbsxh3422wjs4"
        assert (
            subscription2.cancel_subscription
            == "https://customer-portal.paddle.com/cpl_01j7zbyqs3vah3aafp4jf62qaw?action=cancel_subscription&subscription_id=sub_02h04vsc0qhwtsbsxh3422wjs4&token=pga_eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJjdG1fMDFncm5uNHp0YTVhMW1mMDJqanplN3kyeXMiLCJuYW1lIjoiSm9obiBEb2UiLCJpYXQiOjE3Mjc2NzkyMzh9._oO12IejzdKmyKTwb7BLjmiILkx4_cSyGjXraOBUI_g"
        )
        assert (
            subscription2.update_subscription_payment_method
            == "https://customer-portal.paddle.com/cpl_01j7zbyqs3vah3aafp4jf62qaw?action=update_subscription_payment_method&subscription_id=sub_02h04vsc0qhwtsbsxh3422wjs4&token=pga_eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJjdG1fMDFncm5uNHp0YTVhMW1mMDJqanplN3kyeXMiLCJuYW1lIjoiSm9obiBEb2UiLCJpYXQiOjE3Mjc2NzkyMzh9._oO12IejzdKmyKTwb7BLjmiILkx4_cSyGjXraOBUI_g"
        )
