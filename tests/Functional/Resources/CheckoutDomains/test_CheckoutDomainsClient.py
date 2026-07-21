from json import dumps, loads
from pytest import mark
from urllib.parse import unquote

from paddle_billing.Json import PayloadEncoder

from paddle_billing.Entities.CheckoutDomain import CheckoutDomain
from paddle_billing.Entities.CheckoutDomains import CheckoutDomainPaymentMethod, CheckoutDomainStatus
from paddle_billing.Entities.Collections import CheckoutDomainCollection

from paddle_billing.Resources.CheckoutDomains.Operations import ListCheckoutDomains, VerifyCheckoutDomainPaymentMethod
from paddle_billing.Resources.Shared.Operations import Pager

from tests.Utils.ReadsFixture import ReadsFixtures


class TestCheckoutDomainsClient:
    @mark.parametrize(
        "operation, expected_response_status, expected_url",
        [
            (ListCheckoutDomains(), 200, "/checkout-domains"),
            (ListCheckoutDomains(Pager()), 200, "/checkout-domains?order_by=id[asc]&per_page=50"),
            (
                ListCheckoutDomains(Pager(after="chedom_01hv8h6jj90jjz0d71m6hj4r9z")),
                200,
                "/checkout-domains?after=chedom_01hv8h6jj90jjz0d71m6hj4r9z&order_by=id[asc]&per_page=50",
            ),
            (ListCheckoutDomains(domain="example.com"), 200, "/checkout-domains?domain=example.com"),
            (
                ListCheckoutDomains(statuses=[CheckoutDomainStatus.Approved]),
                200,
                "/checkout-domains?status=approved",
            ),
            (
                ListCheckoutDomains(statuses=[CheckoutDomainStatus.Approved, CheckoutDomainStatus.PendingReview]),
                200,
                "/checkout-domains?status=approved,pending_review",
            ),
        ],
        ids=[
            "List checkout domains without pagination",
            "List checkout domains with default pagination",
            "List paginated checkout domains after specified id",
            "List checkout domains filtered by domain",
            "List checkout domains filtered by status",
            "List checkout domains filtered by multiple statuses",
        ],
    )
    def test_list_checkout_domains_returns_expected_response(
        self,
        test_client,
        mock_requests,
        operation,
        expected_response_status,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.get(
            expected_url,
            status_code=expected_response_status,
            text=ReadsFixtures.read_raw_json_fixture("response/list_default"),
        )

        response = test_client.client.checkout_domains.list(operation)
        last_request = mock_requests.last_request

        assert isinstance(response, CheckoutDomainCollection)
        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"

    def test_list_checkout_domains_can_paginate(
        self,
        test_client,
        mock_requests,
    ):
        mock_requests.get(
            f"{test_client.base_url}/checkout-domains",
            status_code=200,
            text=ReadsFixtures.read_raw_json_fixture("response/list_paginated_page_one"),
        )

        mock_requests.get(
            f"{test_client.base_url}/checkout-domains?after=chedom_01hv8h6jj90jjz0d71m6hj4r9z",
            status_code=200,
            text=ReadsFixtures.read_raw_json_fixture("response/list_paginated_page_two"),
        )

        response = test_client.client.checkout_domains.list()

        assert isinstance(response, CheckoutDomainCollection)

        all_checkout_domains = []
        for checkout_domain in response:
            all_checkout_domains.append(checkout_domain)

        assert len(all_checkout_domains) == 2

    @mark.parametrize(
        "checkout_domain_id, expected_response_status, expected_response_body, expected_url",
        [
            (
                "chedom_01hv8h6jj90jjz0d71m6hj4r9z",
                200,
                ReadsFixtures.read_raw_json_fixture("response/full_entity"),
                "/checkout-domains/chedom_01hv8h6jj90jjz0d71m6hj4r9z",
            ),
        ],
        ids=["Get a checkout domain by its id"],
    )
    def test_get_checkout_domain_returns_expected_response(
        self,
        test_client,
        mock_requests,
        checkout_domain_id,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.get(expected_url, status_code=expected_response_status, text=expected_response_body)

        response = test_client.client.checkout_domains.get(checkout_domain_id)
        response_json = test_client.client.checkout_domains.response.json()
        last_request = mock_requests.last_request

        assert isinstance(response, CheckoutDomain)
        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(
            str(expected_response_body)
        ), "The response JSON generated by ResponseParser() doesn't match the expected fixture JSON"

    @mark.parametrize(
        "checkout_domain_id, expected_response_status, expected_path",
        [
            (
                "chedom_01hv8h6jj90jjz0d71m6hj4r9z",
                204,
                "/checkout-domains/chedom_01hv8h6jj90jjz0d71m6hj4r9z",
            )
        ],
        ids=["Delete a checkout domain by its id"],
    )
    def test_delete_checkout_domain_returns_expected_response(
        self,
        test_client,
        mock_requests,
        checkout_domain_id,
        expected_response_status,
        expected_path,
    ):
        expected_url = f"{test_client.base_url}{expected_path}"
        mock_requests.delete(expected_url, status_code=expected_response_status)

        response = test_client.client.checkout_domains.delete(checkout_domain_id)
        last_request = mock_requests.last_request

        assert response is None
        assert last_request is not None
        assert last_request.method == "DELETE"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"

    @mark.parametrize(
        "checkout_domain_id, operation, expected_request_body, expected_response_status, expected_response_body, expected_url",
        [
            (
                "chedom_01hv8h6jj90jjz0d71m6hj4r9z",
                VerifyCheckoutDomainPaymentMethod(payment_method=CheckoutDomainPaymentMethod.ApplePay),
                ReadsFixtures.read_raw_json_fixture("request/verify_payment_method"),
                200,
                ReadsFixtures.read_raw_json_fixture("response/full_entity"),
                "/checkout-domains/chedom_01hv8h6jj90jjz0d71m6hj4r9z/verify-payment-method",
            ),
        ],
        ids=["Verify apple_pay payment method for a checkout domain"],
    )
    def test_verify_payment_method_uses_expected_payload(
        self,
        test_client,
        mock_requests,
        checkout_domain_id,
        operation,
        expected_request_body,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.post(expected_url, status_code=expected_response_status, text=expected_response_body)

        response = test_client.client.checkout_domains.verify_payment_method(checkout_domain_id, operation)
        request_json = test_client.client.payload
        last_request = mock_requests.last_request

        assert isinstance(response, CheckoutDomain)
        assert last_request is not None
        assert last_request.method == "POST"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert loads(request_json) == loads(
            expected_request_body
        ), "The request JSON doesn't match the expected fixture JSON"
        assert (
            loads(dumps(response, cls=PayloadEncoder)) == loads(str(expected_response_body))["data"]
        ), "The response entity doesn't match the expected fixture JSON"
