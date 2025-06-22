from json import loads
from pytest import mark
from urllib.parse import unquote

from paddle_billing.Entities.Collections import PaymentMethodCollection
from paddle_billing.Entities.PaymentMethod import PaymentMethod

from paddle_billing.Resources.Shared.Operations import Pager

from paddle_billing.Resources.PaymentMethods.Operations import (
    ListPaymentMethods,
)

from paddle_billing.Entities.Shared import (
    Card,
    KoreaLocalPaymentMethodType,
    PaymentMethodUnderlyingDetails,
    Paypal,
    SavedPaymentMethodOrigin,
    SavedPaymentMethodType,
)

from tests.Utils.ReadsFixture import ReadsFixtures


class TestPaymentMethodsClient:
    @mark.parametrize(
        "customer_id, expected_response_status, expected_response_body, expected_path",
        [
            (
                "ctm_01hv6y1jedq4p1n0yqn5ba3ky4",
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/customers/ctm_01hv6y1jedq4p1n0yqn5ba3ky4/payment-methods",
            )
        ],
        ids=["List payment-methods"],
    )
    def test_list_payment_methods_returns_expected_response(
        self,
        test_client,
        mock_requests,
        customer_id,
        expected_response_status,
        expected_response_body,
        expected_path,
    ):
        expected_url = f"{test_client.base_url}{expected_path}"
        mock_requests.get(expected_url, status_code=expected_response_status, text=expected_response_body)

        response = test_client.client.payment_methods.list(customer_id)
        last_request = mock_requests.last_request

        assert isinstance(response, PaymentMethodCollection)
        assert all(isinstance(item, PaymentMethod) for item in response.items), "Not all items are PaymentMethod"
        assert last_request is not None

        assert last_request.method == "GET"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"

    @mark.parametrize(
        "customer_id, operation, expected_path",
        [
            (
                "ctm_01hv6y1jedq4p1n0yqn5ba3ky4",
                None,
                "/customers/ctm_01hv6y1jedq4p1n0yqn5ba3ky4/payment-methods",
            ),
            (
                "ctm_01hv6y1jedq4p1n0yqn5ba3ky4",
                ListPaymentMethods(
                    pager=None,
                    address_ids=["add_01hv8h6jj90jjz0d71m6hj4r9z", "add_02hv8h6jj90jjz0d71m6hj4r9z"],
                ),
                "/customers/ctm_01hv6y1jedq4p1n0yqn5ba3ky4/payment-methods?address_id=add_01hv8h6jj90jjz0d71m6hj4r9z,add_02hv8h6jj90jjz0d71m6hj4r9z",
            ),
            (
                "ctm_01hv6y1jedq4p1n0yqn5ba3ky4",
                ListPaymentMethods(
                    pager=None,
                    supports_checkout=False,
                ),
                "/customers/ctm_01hv6y1jedq4p1n0yqn5ba3ky4/payment-methods?supports_checkout=false",
            ),
            (
                "ctm_01hv6y1jedq4p1n0yqn5ba3ky4",
                ListPaymentMethods(
                    pager=None,
                    supports_checkout=True,
                ),
                "/customers/ctm_01hv6y1jedq4p1n0yqn5ba3ky4/payment-methods?supports_checkout=true",
            ),
            (
                "ctm_01hv6y1jedq4p1n0yqn5ba3ky4",
                ListPaymentMethods(
                    pager=None,
                    supports_checkout=True,
                    address_ids=["add_01hv8h6jj90jjz0d71m6hj4r9z", "add_02hv8h6jj90jjz0d71m6hj4r9z"],
                ),
                "/customers/ctm_01hv6y1jedq4p1n0yqn5ba3ky4/payment-methods?address_id=add_01hv8h6jj90jjz0d71m6hj4r9z,add_02hv8h6jj90jjz0d71m6hj4r9z&supports_checkout=true",
            ),
            (
                "ctm_01hv6y1jedq4p1n0yqn5ba3ky4",
                ListPaymentMethods(
                    pager=Pager(),
                ),
                "/customers/ctm_01hv6y1jedq4p1n0yqn5ba3ky4/payment-methods?order_by=id[asc]&per_page=50",
            ),
            (
                "ctm_01hv6y1jedq4p1n0yqn5ba3ky4",
                ListPaymentMethods(
                    pager=Pager(
                        after="paymtd_01hs8zx6x377xfsfrt2bqsevbw",
                        order_by="id[desc]",
                        per_page=100,
                    ),
                ),
                "/customers/ctm_01hv6y1jedq4p1n0yqn5ba3ky4/payment-methods?after=paymtd_01hs8zx6x377xfsfrt2bqsevbw&order_by=id[desc]&per_page=100",
            ),
        ],
        ids=[
            "List all payment-methods",
            "List by address IDs",
            "List supports_checkout false",
            "List supports_checkout true",
            "List by address IDs and supports_checkout",
            "List payment-methods with pagination",
            "List payment-methods with pagination after",
        ],
    )
    def test_list_payment_methods_hits_expected_url(
        self,
        test_client,
        mock_requests,
        customer_id,
        operation,
        expected_path,
    ):
        expected_url = f"{test_client.base_url}{expected_path}"

        mock_requests.get(
            expected_url,
            status_code=200,
            text=ReadsFixtures.read_raw_json_fixture("response/list_default"),
        )

        response = test_client.client.payment_methods.list(customer_id, operation)
        last_request = mock_requests.last_request

        assert isinstance(response, PaymentMethodCollection)
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"

    def test_list_payment_methods_can_paginate(
        self,
        test_client,
        mock_requests,
    ):
        mock_requests.get(
            f"{test_client.base_url}/customers/ctm_01hv6y1jedq4p1n0yqn5ba3ky4/payment-methods",
            status_code=200,
            text=ReadsFixtures.read_raw_json_fixture("response/list_paginated_page_one"),
        )

        mock_requests.get(
            f"{test_client.base_url}/customers/ctm_01hv6y1jedq4p1n0yqn5ba3ky4/payment-methods?after=paymtd_02hs8zx6x377xfsfrt2bqsevbw",
            status_code=200,
            text=ReadsFixtures.read_raw_json_fixture("response/list_paginated_page_two"),
        )

        response = test_client.client.payment_methods.list("ctm_01hv6y1jedq4p1n0yqn5ba3ky4")

        assert isinstance(response, PaymentMethodCollection)

        allPaymentMethods = []
        for paymentMethod in response:
            allPaymentMethods.append(paymentMethod)

        assert len(allPaymentMethods) == 4

    def test_get_payment_methods_returns_expected_card_response(
        self,
        test_client,
        mock_requests,
    ):
        customer_id = "ctm_01hv6y1jedq4p1n0yqn5ba3ky4"
        payment_method_id = "paymtd_01hs8zx6x377xfsfrt2bqsevbw"
        expected_response_status = 200
        expected_response_body = ReadsFixtures.read_raw_json_fixture("response/full_entity_card")
        expected_path = "/customers/ctm_01hv6y1jedq4p1n0yqn5ba3ky4/payment-methods/paymtd_01hs8zx6x377xfsfrt2bqsevbw"

        expected_url = f"{test_client.base_url}{expected_path}"
        mock_requests.get(expected_url, status_code=expected_response_status, text=expected_response_body)

        response = test_client.client.payment_methods.get(customer_id, payment_method_id)
        response_json = test_client.client.payment_methods.response.json()
        last_request = mock_requests.last_request

        assert isinstance(response, PaymentMethod)
        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(
            str(expected_response_body)
        ), "The response JSON generated by ResponseParser() doesn't match the expected fixture JSON"

        assert response.id == "paymtd_01hs8zx6x377xfsfrt2bqsevbw"
        assert response.customer_id == "ctm_01hv6y1jedq4p1n0yqn5ba3ky4"
        assert response.address_id == "add_01hv8h6jj90jjz0d71m6hj4r9z"
        assert response.paypal is None
        assert response.type == SavedPaymentMethodType.Card
        assert response.origin == SavedPaymentMethodOrigin.Subscription
        assert response.saved_at.isoformat() == "2024-05-03T11:50:23.422000+00:00"
        assert response.updated_at.isoformat() == "2024-05-04T11:50:23.422000+00:00"

        card = response.card
        assert isinstance(card, Card)
        assert card.type == "visa"
        assert card.last4 == "0002"
        assert card.expiry_month == 1
        assert card.expiry_year == 2025
        assert card.cardholder_name == "Sam Miller"

    def test_get_payment_methods_returns_expected_paypal_response(
        self,
        test_client,
        mock_requests,
    ):
        customer_id = "ctm_01hv6y1jedq4p1n0yqn5ba3ky4"
        payment_method_id = "paymtd_01hs8zx6x377xfsfrt2bqsevbw"
        expected_response_status = 200
        expected_response_body = ReadsFixtures.read_raw_json_fixture("response/full_entity_paypal")
        expected_path = "/customers/ctm_01hv6y1jedq4p1n0yqn5ba3ky4/payment-methods/paymtd_01hs8zx6x377xfsfrt2bqsevbw"

        expected_url = f"{test_client.base_url}{expected_path}"
        mock_requests.get(expected_url, status_code=expected_response_status, text=expected_response_body)

        response = test_client.client.payment_methods.get(customer_id, payment_method_id)
        response_json = test_client.client.payment_methods.response.json()
        last_request = mock_requests.last_request

        assert isinstance(response, PaymentMethod)
        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(
            str(expected_response_body)
        ), "The response JSON generated by ResponseParser() doesn't match the expected fixture JSON"

        assert response.id == "paymtd_01hs8zx6x377xfsfrt2bqsevbw"
        assert response.customer_id == "ctm_01hv6y1jedq4p1n0yqn5ba3ky4"
        assert response.address_id == "add_01hv8h6jj90jjz0d71m6hj4r9z"
        assert response.card is None
        assert response.type == SavedPaymentMethodType.Paypal
        assert response.origin == SavedPaymentMethodOrigin.SavedDuringPurchase
        assert response.saved_at.isoformat() == "2024-05-03T11:50:23.422000+00:00"
        assert response.updated_at.isoformat() == "2024-05-04T11:50:23.422000+00:00"

        paypal = response.paypal
        assert isinstance(paypal, Paypal)
        assert paypal.email == "sam@example.com"
        assert paypal.reference == "some-reference"

    def test_get_payment_methods_returns_expected_korea_local_response(
        self,
        test_client,
        mock_requests,
    ):
        customer_id = "ctm_01hv6y1jedq4p1n0yqn5ba3ky4"
        payment_method_id = "paymtd_01hs8zx6x377xfsfrt2bqsevbw"
        expected_response_status = 200
        expected_response_body = ReadsFixtures.read_raw_json_fixture("response/full_entity_korea_local")
        expected_path = "/customers/ctm_01hv6y1jedq4p1n0yqn5ba3ky4/payment-methods/paymtd_01hs8zx6x377xfsfrt2bqsevbw"

        expected_url = f"{test_client.base_url}{expected_path}"
        mock_requests.get(expected_url, status_code=expected_response_status, text=expected_response_body)

        response = test_client.client.payment_methods.get(customer_id, payment_method_id)
        response_json = test_client.client.payment_methods.response.json()
        last_request = mock_requests.last_request

        assert isinstance(response, PaymentMethod)
        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(
            str(expected_response_body)
        ), "The response JSON generated by ResponseParser() doesn't match the expected fixture JSON"

        assert response.id == "paymtd_01hs8zx6x377xfsfrt2bqsevbw"
        assert response.customer_id == "ctm_01hv6y1jedq4p1n0yqn5ba3ky4"
        assert response.address_id == "add_01hv8h6jj90jjz0d71m6hj4r9z"
        assert response.card is None
        assert response.type == SavedPaymentMethodType.KoreaLocal
        assert response.origin == SavedPaymentMethodOrigin.Subscription
        assert response.saved_at.isoformat() == "2024-05-03T11:50:23.422000+00:00"
        assert response.updated_at.isoformat() == "2024-05-04T11:50:23.422000+00:00"

        underlying_details = response.underlying_details
        assert isinstance(underlying_details, PaymentMethodUnderlyingDetails)
        assert underlying_details.korea_local.type == KoreaLocalPaymentMethodType.KakaoBank

    def test_delete_payment_method_returns_expected_response(
        self,
        test_client,
        mock_requests,
    ):
        customer_id = "ctm_01hv6y1jedq4p1n0yqn5ba3ky4"
        payment_method_id = "paymtd_01hs8zx6x377xfsfrt2bqsevbw"
        expected_response_status = 204
        expected_path = "/customers/ctm_01hv6y1jedq4p1n0yqn5ba3ky4/payment-methods/paymtd_01hs8zx6x377xfsfrt2bqsevbw"

        expected_url = f"{test_client.base_url}{expected_path}"
        mock_requests.delete(expected_url, status_code=expected_response_status)

        response = test_client.client.payment_methods.delete(customer_id, payment_method_id)
        last_request = mock_requests.last_request

        assert response is None
        assert last_request is not None
        assert last_request.method == "DELETE"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
