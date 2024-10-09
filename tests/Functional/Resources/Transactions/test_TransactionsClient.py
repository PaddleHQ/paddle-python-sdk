from json import loads
from pytest import mark
from urllib.parse import unquote

from paddle_billing.Entities.Collections import TransactionCollection
from paddle_billing.Entities.DateTime import DateTime
from paddle_billing.Entities.Transaction import Transaction
from paddle_billing.Entities.TransactionData import TransactionData
from paddle_billing.Entities.TransactionPreview import TransactionPreview
from paddle_billing.Resources.Shared.Operations import Comparator, DateComparison, Pager
from paddle_billing.Entities.Discount import Discount, DiscountStatus

from paddle_billing.Entities.Shared import (
    AddressPreview,
    CollectionMode,
    CountryCode,
    CurrencyCode,
    CustomData,
    Duration,
    Interval,
    Money,
    PaymentMethodType,
    PriceQuantity,
    TaxCategory,
    TransactionStatus,
    TaxMode,
    Disposition,
)

from paddle_billing.Entities.Transactions import (
    TransactionCreateItem,
    TransactionCreateItemWithPrice,
    TransactionNonCatalogPrice,
    TransactionNonCatalogPriceWithProduct,
    TransactionNonCatalogProduct,
    TransactionItemPreviewWithNonCatalogPrice,
    TransactionItemPreviewWithPriceId,
)

from paddle_billing.Resources.Transactions.Operations import (
    CreateTransaction,
    ListTransactions,
    TransactionIncludes,
    TransactionOrigin,
    PreviewTransactionByAddress,
    PreviewTransactionByCustomer,
    PreviewTransactionByIP,
    UpdateTransaction,
    GetTransactionInvoice,
)

from paddle_billing.Resources.Transactions.Operations.Create import CreateBillingDetails
from paddle_billing.Resources.Transactions.Operations.Update import UpdateBillingDetails

from tests.Utils.ReadsFixture import ReadsFixtures


class TestTransactionsClient:
    @mark.parametrize("operation", [ListTransactions()])
    def test_list_transaction_can_paginate(self, test_client, mock_requests, operation):
        expected_response_status = 200
        expected_page_one_url = f"{test_client.base_url}/transactions"
        expected_page_one_response_body = ReadsFixtures.read_raw_json_fixture("response/list_paginated_page_one")

        # meta.pagination.next value is hardcoded in response/list_paginated_page_one, so this must be an absolute value
        expected_page_two_url = "https://api.paddle.com/transactions?after=txn_06h69ddtrb11km0wk46dn607ya"

        mock_requests.get(
            url=expected_page_one_url,
            status_code=expected_response_status,
            text=ReadsFixtures.read_raw_json_fixture("response/list_paginated_page_one"),
        )
        mock_requests.get(
            url=expected_page_two_url,
            status_code=expected_response_status,
            text=ReadsFixtures.read_raw_json_fixture("response/list_paginated_page_two"),
        )

        transactions = test_client.client.transactions.list(operation)
        response_json = test_client.client.transactions.response.json()

        # Assertions for first request
        assert len(mock_requests.request_history) > 0
        first_request = mock_requests.request_history[0]
        assert first_request is not None
        assert first_request.method == "GET"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(first_request.url) == expected_page_one_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(
            expected_page_one_response_body
        ), "The response JSON doesn't match the expected fixture JSON"

        # Iterate all transactions from page one and two.
        all_transactions: list[Transaction] = []
        for transaction in transactions:
            assert isinstance(transaction, Transaction)
            all_transactions.append(transaction)

        assert len(all_transactions) == 12

        assert all_transactions[0].id == "txn_01h8bm0f0gwa622zpcvw49hwc1"
        assert all_transactions[6].id == "txn_07h8bm0f0gwa622zpcvw49hwc1"
        assert all_transactions[11].id == "txn_12h69ddtrb11km0wk46dn607ya"

        # Assertions for second request
        second_request = mock_requests.request_history[1]
        assert second_request is not None
        assert second_request.method == "GET"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(second_request.url) == expected_page_two_url
        ), "The URL does not match the expected URL, verify the query string is correct"

    @mark.parametrize(
        "operation, expected_request_body, expected_response_status, expected_response_body, expected_url",
        [
            (
                CreateTransaction(items=[TransactionCreateItem(price_id="pri_01he5kxqey1k8ankgef29cj4bv", quantity=1)]),
                ReadsFixtures.read_raw_json_fixture("request/create_basic"),
                200,
                ReadsFixtures.read_raw_json_fixture("response/minimal_entity"),
                "/transactions",
            ),
            (
                CreateTransaction(
                    items=[
                        TransactionCreateItemWithPrice(
                            price=TransactionNonCatalogPrice(
                                description="Annual (per seat)",
                                name="Annual (per seat)",
                                billing_cycle=Duration(Interval.Year, 1),
                                trial_period=None,
                                tax_mode=TaxMode.AccountSetting,
                                unit_price=Money("30000", CurrencyCode.USD),
                                unit_price_overrides=[],
                                quantity=PriceQuantity(10, 999),
                                custom_data=None,
                                product_id="pro_01gsz4t5hdjse780zja8vvr7jg",
                            ),
                            quantity=20,
                        ),
                    ],
                ),
                ReadsFixtures.read_raw_json_fixture("request/create_with_non_catalog_price"),
                200,
                ReadsFixtures.read_raw_json_fixture("response/minimal_entity"),
                "/transactions",
            ),
            (
                CreateTransaction(
                    items=[TransactionCreateItem(price_id="pri_01gsz8x8sawmvhz1pv30nge1ke", quantity=1)],
                    status=TransactionStatus.Billed,
                    customer_id="ctm_01he849dseyj0zgrc589eeb1c7",
                    address_id="add_01hen28ebw1ew99y295jhd4n3n",
                    business_id="biz_01hen2ng2290g84twtefdn5s00",
                    currency_code=CurrencyCode.GBP,
                    collection_mode=CollectionMode.Manual,
                    discount_id="dsc_01hen7bjzh12m0v2peer15d9qt",
                    billing_details=CreateBillingDetails(
                        enable_checkout=True,
                        payment_terms=Duration(interval=Interval.Month, frequency=1),
                        purchase_order_number="10009",
                    ),
                ),
                ReadsFixtures.read_raw_json_fixture("request/create_manual"),
                200,
                ReadsFixtures.read_raw_json_fixture("response/full_entity"),
                "/transactions",
            ),
            (
                CreateTransaction(
                    items=[TransactionCreateItem(price_id="pri_01gsz8x8sawmvhz1pv30nge1ke", quantity=1)],
                    billing_details=CreateBillingDetails(
                        payment_terms=Duration(interval=Interval.Month, frequency=1),
                    ),
                ),
                ReadsFixtures.read_raw_json_fixture("request/create_minimal_billing_details"),
                200,
                ReadsFixtures.read_raw_json_fixture("response/full_entity"),
                "/transactions",
            ),
            (
                CreateTransaction(
                    items=[TransactionCreateItem(price_id="pri_01gsz8x8sawmvhz1pv30nge1ke", quantity=1)],
                    billing_details=CreateBillingDetails(
                        enable_checkout=True,
                        payment_terms=Duration(interval=Interval.Month, frequency=1),
                        purchase_order_number="10009",
                        additional_information="Some additional information",
                    ),
                ),
                ReadsFixtures.read_raw_json_fixture("request/create_full_billing_details"),
                200,
                ReadsFixtures.read_raw_json_fixture("response/full_entity"),
                "/transactions",
            ),
        ],
        ids=[
            "Create transaction with basic data",
            "Create transaction with non-catalog price",
            "Create transaction with manual collection mode",
            "Create transaction with minimal billing details",
            "Create transaction with full billing details",
        ],
    )
    def test_create_transaction_uses_expected_payload(
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

        response = test_client.client.transactions.create(operation)
        response_json = test_client.client.transactions.response.json()
        request_json = test_client.client.payload
        last_request = mock_requests.last_request

        assert isinstance(response, Transaction)
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
        "operation, includes, expected_response_status, expected_response_body, expected_url",
        [
            (
                CreateTransaction(items=[TransactionCreateItem(price_id="pri_01he5kxqey1k8ankgef29cj4bv", quantity=1)]),
                [TransactionIncludes.Customer, TransactionIncludes.Business],
                200,
                ReadsFixtures.read_raw_json_fixture("response/minimal_entity"),
                "/transactions?include=customer,business",
            )
        ],
        ids=["Create transaction with multiple includes"],
    )
    def test_create_transaction_with_includes_returns_expected_payload(
        self,
        test_client,
        mock_requests,
        operation,
        includes,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.post(expected_url, status_code=expected_response_status, text=expected_response_body)

        response = test_client.client.transactions.create(operation, includes=includes)
        response_json = test_client.client.transactions.response.json()
        last_request = mock_requests.last_request

        assert isinstance(response, Transaction)
        assert last_request is not None
        assert last_request.method == "POST"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(
            str(expected_response_body)
        ), "The response JSON doesn't match the expected fixture JSON"

    @mark.parametrize(
        "transaction_id, operation, expected_request_body, expected_response_status, expected_response_body, expected_url",
        [
            (
                "txn_01h7zcgmdc6tmwtjehp3sh7azf",
                UpdateTransaction(status=TransactionStatus.Billed),
                ReadsFixtures.read_raw_json_fixture("request/update_single"),
                200,
                ReadsFixtures.read_raw_json_fixture("response/full_entity"),
                "/transactions/txn_01h7zcgmdc6tmwtjehp3sh7azf",
            ),
            (
                "txn_01h7zcgmdc6tmwtjehp3sh7azf",
                UpdateTransaction(status=TransactionStatus.Billed, custom_data=CustomData({"completed_by": "Frank T"})),
                ReadsFixtures.read_raw_json_fixture("request/update_partial"),
                200,
                ReadsFixtures.read_raw_json_fixture("response/full_entity"),
                "/transactions/txn_01h7zcgmdc6tmwtjehp3sh7azf",
            ),
            (
                "txn_01h7zcgmdc6tmwtjehp3sh7azf",
                UpdateTransaction(
                    billing_details=UpdateBillingDetails(
                        payment_terms=Duration(interval=Interval.Month, frequency=1),
                    ),
                ),
                ReadsFixtures.read_raw_json_fixture("request/update_minimal_billing_details"),
                200,
                ReadsFixtures.read_raw_json_fixture("response/full_entity"),
                "/transactions/txn_01h7zcgmdc6tmwtjehp3sh7azf",
            ),
            (
                "txn_01h7zcgmdc6tmwtjehp3sh7azf",
                UpdateTransaction(
                    billing_details=UpdateBillingDetails(
                        enable_checkout=True,
                        payment_terms=Duration(interval=Interval.Month, frequency=1),
                        purchase_order_number="10009",
                        additional_information="Some additional information",
                    ),
                ),
                ReadsFixtures.read_raw_json_fixture("request/update_full_billing_details"),
                200,
                ReadsFixtures.read_raw_json_fixture("response/full_entity"),
                "/transactions/txn_01h7zcgmdc6tmwtjehp3sh7azf",
            ),
        ],
        ids=[
            "Update transaction with single new value",
            "Update transaction with partial new values",
            "Create transaction with minimal billing details",
            "Create transaction with full billing details",
        ],
    )
    def test_update_transaction_uses_expected_payload(
        self,
        test_client,
        mock_requests,
        transaction_id,
        operation,
        expected_request_body,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.patch(expected_url, status_code=expected_response_status, text=expected_response_body)

        response = test_client.client.transactions.update(transaction_id, operation)
        response_json = test_client.client.transactions.response.json()
        request_json = test_client.client.payload
        last_request = mock_requests.last_request

        assert isinstance(response, Transaction)
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
        "operation, expected_response_status, expected_response_body, expected_url",
        [
            (
                ListTransactions(),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/transactions",
            ),
            (
                ListTransactions(Pager()),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/transactions?order_by=id[asc]&per_page=50",
            ),
            (
                ListTransactions(Pager(after="pro_01gsz4s0w61y0pp88528f1wvvb")),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/transactions?after=pro_01gsz4s0w61y0pp88528f1wvvb&order_by=id[asc]&per_page=50",
            ),
            (
                ListTransactions(statuses=[TransactionStatus.Billed]),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/transactions?status=billed",
            ),
            (
                ListTransactions(statuses=[TransactionStatus.Billed, TransactionStatus.Completed]),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/transactions?status=billed,completed",
            ),
            (
                ListTransactions(ids=["txn_01gsz4s0w61y0pp88528f1wvvb"]),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/transactions?id=txn_01gsz4s0w61y0pp88528f1wvvb",
            ),
            (
                ListTransactions(ids=["txn_01gsz4s0w61y0pp88528f1wvvb", "txn_01h1vjes1y163xfj1rh1tkfb65"]),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/transactions?id=txn_01gsz4s0w61y0pp88528f1wvvb,txn_01h1vjes1y163xfj1rh1tkfb65",
            ),
            (
                ListTransactions(collection_mode=CollectionMode.Automatic),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/transactions?collection_mode=automatic",
            ),
            (
                ListTransactions(billed_at=DateComparison(DateTime("2023-11-06 14:00:00").as_datetime)),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/transactions?billed_at=2023-11-06T14:00:00.000000Z",
            ),
            (
                ListTransactions(billed_at=DateComparison(DateTime("2023-11-06 14:00:00").as_datetime, Comparator.GT)),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/transactions?billed_at[GT]=2023-11-06T14:00:00.000000Z",
            ),
            (
                ListTransactions(invoice_numbers=["inv_01gsz4s0w61y0pp88528f1wvvb"]),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/transactions?invoice_number=inv_01gsz4s0w61y0pp88528f1wvvb",
            ),
            (
                ListTransactions(invoice_numbers=["inv_01gsz4s0w61y0pp88528f1wvvb", "inv_01h1vjes1y163xfj1rh1tkfb65"]),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/transactions?invoice_number=inv_01gsz4s0w61y0pp88528f1wvvb,inv_01h1vjes1y163xfj1rh1tkfb65",
            ),
            (
                ListTransactions(subscription_ids=["sub_01gsz4s0w61y0pp88528f1wvvb"]),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/transactions?subscription_id=sub_01gsz4s0w61y0pp88528f1wvvb",
            ),
            (
                ListTransactions(subscription_ids=["sub_01gsz4s0w61y0pp88528f1wvvb", "sub_01h1vjes1y163xfj1rh1tkfb65"]),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/transactions?subscription_id=sub_01gsz4s0w61y0pp88528f1wvvb,sub_01h1vjes1y163xfj1rh1tkfb65",
            ),
            (
                ListTransactions(updated_at=DateComparison(DateTime("2023-11-06 14:00:00").as_datetime)),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/transactions?updated_at=2023-11-06T14:00:00.000000Z",
            ),
            (
                ListTransactions(updated_at=DateComparison(DateTime("2023-11-06 14:00:00").as_datetime, Comparator.GT)),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/transactions?updated_at[GT]=2023-11-06T14:00:00.000000Z",
            ),
            (
                ListTransactions(created_at=DateComparison(DateTime("2023-11-06 14:00:00").as_datetime)),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/transactions?created_at=2023-11-06T14:00:00.000000Z",
            ),
            (
                ListTransactions(created_at=DateComparison(DateTime("2023-11-06 14:00:00").as_datetime, Comparator.GT)),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/transactions?created_at[GT]=2023-11-06T14:00:00.000000Z",
            ),
            (
                ListTransactions(includes=[TransactionIncludes.Customer]),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/transactions?include=customer",
            ),
            (
                ListTransactions(
                    includes=[TransactionIncludes.Customer, TransactionIncludes.Address, TransactionIncludes.Discount]
                ),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/transactions?include=customer,address,discount",
            ),
            (
                ListTransactions(
                    origins=[TransactionOrigin.Web, TransactionOrigin.Api, TransactionOrigin.SubscriptionRecurring]
                ),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/transactions?origin=web,api,subscription_recurring",
            ),
        ],
        ids=[
            "List transactions without pagination",
            "List transactions with default pagination",
            "List paginated transactions after specified transaction_id",
            "List transactions filtered by status",
            "List transactions filtered by multiple statuses",
            "List transactions filtered by id",
            "List transactions filtered by multiple ids",
            "List transactions filtered by automatic collection_mode",
            "List transactions filtered by billed_at without a comparator",
            "List transactions filtered by billed at with a comparator",
            "List transactions filtered by invoice_number",
            "List transactions filtered by multiple invoice_numbers",
            "List transactions filtered by subscription_id",
            "List transactions filtered by multiple subscription_ids",
            "List transactions filtered by updated_at without a comparator",
            "List transactions filtered by updated_at with a comparator",
            "List transactions filtered by created_at without a comparator",
            "List transactions filtered by created_at with a comparator",
            "List transactions with includes",
            "List transactions with multiple includes",
            "List transactions with origins",
        ],
    )
    def test_list_transactions_returns_expected_response(
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

        response = test_client.client.transactions.list(operation)
        last_request = mock_requests.last_request

        assert isinstance(response, TransactionCollection)
        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"

    @mark.parametrize(
        "transaction_id, includes, expected_response_status, expected_response_body, expected_url",
        [
            (
                "txn_01hen7bxc1p8ep4yk7n5jbzk9r",
                None,
                200,
                ReadsFixtures.read_raw_json_fixture("response/full_entity"),
                "/transactions/txn_01hen7bxc1p8ep4yk7n5jbzk9r",
            ),
            (
                "txn_01hen7bxc1p8ep4yk7n5jbzk9r",
                [
                    TransactionIncludes.Customer,
                    TransactionIncludes.Address,
                    TransactionIncludes.Business,
                    TransactionIncludes.Discount,
                    TransactionIncludes.AvailablePaymentMethods,
                ],
                200,
                ReadsFixtures.read_raw_json_fixture("response/full_entity"),
                "/transactions/txn_01hen7bxc1p8ep4yk7n5jbzk9r?include=customer,address,business,discount,available_payment_methods",
            ),
        ],
        ids=[
            "Get transaction",
            "Get transaction with includes",
        ],
    )
    def test_get_transactions_returns_expected_response(
        self,
        test_client,
        mock_requests,
        transaction_id,
        includes,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.get(expected_url, status_code=expected_response_status, text=expected_response_body)

        response = test_client.client.transactions.get(transaction_id, includes=includes)
        response_json = test_client.client.transactions.response.json()
        last_request = mock_requests.last_request

        assert isinstance(response, Transaction)
        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(
            str(expected_response_body)
        ), "The response JSON generated by ResponseParser() doesn't match the expected fixture JSON"

    def test_get_transaction_returns_transaction_with_discount(
        self,
        test_client,
        mock_requests,
    ):
        mock_requests.get(
            f"{test_client.base_url}/transactions/txn_01hen7bxc1p8ep4yk7n5jbzk9r",
            status_code=200,
            text=ReadsFixtures.read_raw_json_fixture("response/full_entity"),
        )

        response = test_client.client.transactions.get("txn_01hen7bxc1p8ep4yk7n5jbzk9r")

        assert isinstance(response, Transaction)

        discount = response.discount
        assert isinstance(discount, Discount)
        assert discount.id == "dsc_01h83xenpcfjyhkqr4x214m02x"
        assert discount.status == DiscountStatus.Active
        assert discount.description == "Nonprofit discount"
        assert discount.enabled_for_checkout is True
        assert discount.code == "ABCDE12345"
        assert discount.type == "percentage"
        assert discount.amount == "10"
        assert discount.recur is True
        assert discount.maximum_recurring_intervals == 5
        assert discount.usage_limit == 1000
        assert discount.restrict_to == ["pro_01gsz4t5hdjse780zja8vvr7jg", "pro_01gsz4s0w61y0pp88528f1wvvb"]
        assert discount.expires_at.isoformat() == "2024-08-18T08:51:07.596000+00:00"
        assert discount.times_used == 0
        assert discount.created_at.isoformat() == "2023-08-18T08:51:07.596000+00:00"
        assert discount.updated_at.isoformat() == "2023-08-18T08:51:07.596000+00:00"
        assert isinstance(discount.custom_data, CustomData)
        assert discount.custom_data.data.get("key") == "value"

    def test_get_transaction_returns_transaction_with_available_payment_methods(
        self,
        test_client,
        mock_requests,
    ):
        mock_requests.get(
            f"{test_client.base_url}/transactions/txn_01hen7bxc1p8ep4yk7n5jbzk9r",
            status_code=200,
            text=ReadsFixtures.read_raw_json_fixture("response/full_entity"),
        )

        response = test_client.client.transactions.get("txn_01hen7bxc1p8ep4yk7n5jbzk9r")

        assert isinstance(response, Transaction)

        available_payment_methods = response.available_payment_methods
        assert available_payment_methods[0] == PaymentMethodType.Alipay
        assert available_payment_methods[1] == PaymentMethodType.ApplePay
        assert available_payment_methods[2] == PaymentMethodType.Bancontact
        assert available_payment_methods[3] == PaymentMethodType.Card
        assert available_payment_methods[4] == PaymentMethodType.GooglePay
        assert available_payment_methods[5] == PaymentMethodType.Ideal
        assert available_payment_methods[6] == PaymentMethodType.Offline
        assert available_payment_methods[7] == PaymentMethodType.Paypal
        assert available_payment_methods[8] == PaymentMethodType.Unknown
        assert available_payment_methods[9] == PaymentMethodType.WireTransfer

    def test_get_transaction_with_and_without_payment_method_id(
        self,
        test_client,
        mock_requests,
    ):
        mock_requests.get(
            f"{test_client.base_url}/transactions/txn_01hen7bxc1p8ep4yk7n5jbzk9r",
            status_code=200,
            text=ReadsFixtures.read_raw_json_fixture("response/full_entity"),
        )

        response = test_client.client.transactions.get("txn_01hen7bxc1p8ep4yk7n5jbzk9r")

        assert isinstance(response, Transaction)

        payment_with_payment_method_id = response.payments[0]
        assert payment_with_payment_method_id.payment_method_id == "paymtd_01hkm9xwqpbbpr1ksmvg3sx3v1"

        payment_without_payment_method_id = response.payments[1]
        assert payment_without_payment_method_id.payment_method_id is None

    @mark.parametrize(
        "operation, expected_request_body, expected_response_status, expected_response_body, expected_url",
        [
            (
                PreviewTransactionByAddress(
                    address=AddressPreview(
                        postal_code="12345",
                        country_code=CountryCode.US,
                    ),
                    items=[
                        TransactionItemPreviewWithPriceId(
                            price_id="pri_01he5kxqey1k8ankgef29cj4bv",
                            quantity=1,
                            include_in_totals=True,
                        )
                    ],
                ),
                ReadsFixtures.read_raw_json_fixture("request/preview_by_address_basic"),
                200,
                ReadsFixtures.read_raw_json_fixture("response/preview_entity"),
                "/transactions/preview",
            ),
            (
                PreviewTransactionByAddress(
                    address=AddressPreview(
                        postal_code="12345",
                        country_code=CountryCode.US,
                    ),
                    customer_id="ctm_01h844q4mznqpgqgm6evgw1w63",
                    currency_code=CurrencyCode.USD,
                    discount_id="dsc_01gtgztp8fpchantd5g1wrksa3",
                    ignore_trials=True,
                    items=[
                        TransactionItemPreviewWithNonCatalogPrice(
                            quantity=20,
                            include_in_totals=True,
                            price=TransactionNonCatalogPrice(
                                description="Annual (per seat)",
                                name="Annual (per seat)",
                                billing_cycle=Duration(Interval.Year, 1),
                                trial_period=None,
                                tax_mode=TaxMode.AccountSetting,
                                unit_price=Money("30000", CurrencyCode.USD),
                                unit_price_overrides=[],
                                quantity=PriceQuantity(minimum=10, maximum=999),
                                custom_data=None,
                                product_id="pro_01gsz4t5hdjse780zja8vvr7jg",
                            ),
                        ),
                        TransactionItemPreviewWithNonCatalogPrice(
                            quantity=20,
                            include_in_totals=True,
                            price=TransactionNonCatalogPriceWithProduct(
                                description="Annual (per seat)",
                                name="Annual (per seat)",
                                billing_cycle=Duration(Interval.Year, 1),
                                trial_period=None,
                                tax_mode=TaxMode.AccountSetting,
                                unit_price=Money("30000", CurrencyCode.USD),
                                unit_price_overrides=[],
                                quantity=PriceQuantity(minimum=10, maximum=999),
                                custom_data=None,
                                product=TransactionNonCatalogProduct(
                                    name="Analytics addon",
                                    description="Some Description",
                                    image_url="https://paddle.s3.amazonaws.com/user/165798/97dRpA6SXzcE6ekK9CAr_analytics.png",
                                    tax_category=TaxCategory.Standard,
                                    custom_data=CustomData({"key": "value"}),
                                ),
                            ),
                        ),
                    ],
                ),
                ReadsFixtures.read_raw_json_fixture("request/preview_by_address_full"),
                200,
                ReadsFixtures.read_raw_json_fixture("response/preview_entity"),
                "/transactions/preview",
            ),
            (
                PreviewTransactionByCustomer(
                    address_id="add_01hv8h6jj90jjz0d71m6hj4r9z",
                    customer_id="ctm_01h844q4mznqpgqgm6evgw1w63",
                    items=[
                        TransactionItemPreviewWithPriceId(
                            price_id="pri_01he5kxqey1k8ankgef29cj4bv",
                            quantity=1,
                            include_in_totals=True,
                        )
                    ],
                ),
                ReadsFixtures.read_raw_json_fixture("request/preview_by_customer_basic"),
                200,
                ReadsFixtures.read_raw_json_fixture("response/preview_entity"),
                "/transactions/preview",
            ),
            (
                PreviewTransactionByCustomer(
                    address_id="add_01hv8h6jj90jjz0d71m6hj4r9z",
                    customer_id="ctm_01h844q4mznqpgqgm6evgw1w63",
                    business_id="biz_01hv8j0z17hv4ew8teebwjmfcb",
                    currency_code=CurrencyCode.USD,
                    discount_id="dsc_01gtgztp8fpchantd5g1wrksa3",
                    ignore_trials=True,
                    items=[
                        TransactionItemPreviewWithNonCatalogPrice(
                            quantity=20,
                            include_in_totals=True,
                            price=TransactionNonCatalogPrice(
                                description="Annual (per seat)",
                                name="Annual (per seat)",
                                billing_cycle=Duration(Interval.Year, 1),
                                trial_period=None,
                                tax_mode=TaxMode.AccountSetting,
                                unit_price=Money("30000", CurrencyCode.USD),
                                unit_price_overrides=[],
                                quantity=PriceQuantity(minimum=10, maximum=999),
                                custom_data=None,
                                product_id="pro_01gsz4t5hdjse780zja8vvr7jg",
                            ),
                        ),
                        TransactionItemPreviewWithNonCatalogPrice(
                            quantity=20,
                            include_in_totals=True,
                            price=TransactionNonCatalogPriceWithProduct(
                                description="Annual (per seat)",
                                name="Annual (per seat)",
                                billing_cycle=Duration(Interval.Year, 1),
                                trial_period=None,
                                tax_mode=TaxMode.AccountSetting,
                                unit_price=Money("30000", CurrencyCode.USD),
                                unit_price_overrides=[],
                                quantity=PriceQuantity(minimum=10, maximum=999),
                                custom_data=None,
                                product=TransactionNonCatalogProduct(
                                    name="Analytics addon",
                                    description="Some Description",
                                    image_url="https://paddle.s3.amazonaws.com/user/165798/97dRpA6SXzcE6ekK9CAr_analytics.png",
                                    tax_category=TaxCategory.Standard,
                                    custom_data=CustomData({"key": "value"}),
                                ),
                            ),
                        ),
                    ],
                ),
                ReadsFixtures.read_raw_json_fixture("request/preview_by_customer_full"),
                200,
                ReadsFixtures.read_raw_json_fixture("response/preview_entity"),
                "/transactions/preview",
            ),
            (
                PreviewTransactionByIP(
                    customer_ip_address="203.0.113.0",
                    items=[
                        TransactionItemPreviewWithPriceId(
                            price_id="pri_01he5kxqey1k8ankgef29cj4bv",
                            quantity=1,
                            include_in_totals=True,
                        )
                    ],
                ),
                ReadsFixtures.read_raw_json_fixture("request/preview_by_ip_basic"),
                200,
                ReadsFixtures.read_raw_json_fixture("response/preview_entity"),
                "/transactions/preview",
            ),
            (
                PreviewTransactionByIP(
                    customer_ip_address="203.0.113.0",
                    customer_id="ctm_01h844q4mznqpgqgm6evgw1w63",
                    currency_code=CurrencyCode.USD,
                    discount_id="dsc_01gtgztp8fpchantd5g1wrksa3",
                    ignore_trials=True,
                    items=[
                        TransactionItemPreviewWithNonCatalogPrice(
                            quantity=20,
                            include_in_totals=True,
                            price=TransactionNonCatalogPrice(
                                description="Annual (per seat)",
                                name="Annual (per seat)",
                                billing_cycle=Duration(Interval.Year, 1),
                                trial_period=None,
                                tax_mode=TaxMode.AccountSetting,
                                unit_price=Money("30000", CurrencyCode.USD),
                                unit_price_overrides=[],
                                quantity=PriceQuantity(minimum=10, maximum=999),
                                custom_data=None,
                                product_id="pro_01gsz4t5hdjse780zja8vvr7jg",
                            ),
                        ),
                        TransactionItemPreviewWithNonCatalogPrice(
                            quantity=20,
                            include_in_totals=True,
                            price=TransactionNonCatalogPriceWithProduct(
                                description="Annual (per seat)",
                                name="Annual (per seat)",
                                billing_cycle=Duration(Interval.Year, 1),
                                trial_period=None,
                                tax_mode=TaxMode.AccountSetting,
                                unit_price=Money("30000", CurrencyCode.USD),
                                unit_price_overrides=[],
                                quantity=PriceQuantity(minimum=10, maximum=999),
                                custom_data=None,
                                product=TransactionNonCatalogProduct(
                                    name="Analytics addon",
                                    description="Some Description",
                                    image_url="https://paddle.s3.amazonaws.com/user/165798/97dRpA6SXzcE6ekK9CAr_analytics.png",
                                    tax_category=TaxCategory.Standard,
                                    custom_data=CustomData({"key": "value"}),
                                ),
                            ),
                        ),
                    ],
                ),
                ReadsFixtures.read_raw_json_fixture("request/preview_by_ip_full"),
                200,
                ReadsFixtures.read_raw_json_fixture("response/preview_entity"),
                "/transactions/preview",
            ),
        ],
        ids=[
            "Basic transaction preview by address",
            "Full transaction preview by address",
            "Basic transaction preview by customer",
            "Full transaction preview by customer",
            "Basic transaction preview by IP",
            "Full transaction preview by IP",
        ],
    )
    def test_preview_transaction_returns_expected_response(
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

        response = test_client.client.transactions.preview(operation)
        response_json = test_client.client.transactions.response.json()
        request_json = test_client.client.payload
        last_request = mock_requests.last_request

        assert isinstance(response, TransactionPreview)
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

    def test_get_transaction_invoice_pdf_returns_expected_response(self, test_client, mock_requests):
        transaction_id = "txn_01hen7bxc1p8ep4yk7n5jbzk9r"
        expected_response_status = 200
        expected_response_body = ReadsFixtures.read_raw_json_fixture("response/get_invoice_pdf_default")
        expected_url = f"{test_client.base_url}/transactions/{transaction_id}/invoice"

        mock_requests.get(expected_url, status_code=expected_response_status, text=expected_response_body)

        response = test_client.client.transactions.get_invoice_pdf(transaction_id)
        response_json = test_client.client.transactions.response.json()
        last_request = mock_requests.last_request

        assert isinstance(response, TransactionData)
        assert (
            response.url
            == "https://paddle-invoice-service-pdfs.s3.amazonaws.com/invoices/00000/f64658f0-d8ef-41cb-a916-d24d9b1e33bf/invoice_325-10001_Bluth.pdf"
        )

        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(
            str(expected_response_body)
        ), "The response JSON doesn't match the expected fixture JSON"

    @mark.parametrize(
        "transaction_id, operation, expected_path",
        [
            (
                "txn_01hen7bxc1p8ep4yk7n5jbzk9r",
                None,
                "/transactions/txn_01hen7bxc1p8ep4yk7n5jbzk9r/invoice",
            ),
            (
                "txn_01hen7bxc1p8ep4yk7n5jbzk9r",
                GetTransactionInvoice(disposition=Disposition.Inline),
                "/transactions/txn_01hen7bxc1p8ep4yk7n5jbzk9r/invoice?disposition=inline",
            ),
            (
                "txn_01hen7bxc1p8ep4yk7n5jbzk9r",
                GetTransactionInvoice(disposition=Disposition.Attachment),
                "/transactions/txn_01hen7bxc1p8ep4yk7n5jbzk9r/invoice?disposition=attachment",
            ),
        ],
        ids=[
            "Get invoice default",
            "Get invoice with inline disposition",
            "Get invoice with attachment disposition",
        ],
    )
    def test_get_transaction_invoice_pdf_hits_expected_url(
        self,
        test_client,
        mock_requests,
        transaction_id,
        operation,
        expected_path,
    ):
        expected_url = f"{test_client.base_url}{expected_path}"

        mock_requests.get(
            expected_url,
            status_code=200,
            text=ReadsFixtures.read_raw_json_fixture("response/get_invoice_pdf_default"),
        )

        response = test_client.client.transactions.get_invoice_pdf(transaction_id, operation)
        last_request = mock_requests.last_request

        assert isinstance(response, TransactionData)
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
