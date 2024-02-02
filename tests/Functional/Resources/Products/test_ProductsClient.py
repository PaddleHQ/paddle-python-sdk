from json         import loads
from pytest       import mark
from urllib.parse import unquote

from paddle_billing.Entities.Collections import ProductCollection
from paddle_billing.Entities.Product     import Product
from paddle_billing.Entities.Shared      import CustomData, Status, TaxCategory

from paddle_billing.Resources.Products.Operations import CreateProduct, ListProducts, UpdateProduct, ProductIncludes
from paddle_billing.Resources.Shared.Operations   import Pager

from tests.Utils.TestClient   import mock_requests, test_client
from tests.Utils.ReadsFixture import ReadsFixtures


class TestProductsClient:
    @mark.parametrize(
        'operation, expected_request_body, expected_response_status, expected_response_body, expected_url',
        [
            (
                CreateProduct(
                    name         = 'ChatApp Basic',
                    tax_category = TaxCategory.Standard,
                ),
                ReadsFixtures.read_raw_json_fixture('request/create_basic'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/minimal_entity'),
                '/products',
            ), (
                CreateProduct(
                    name         = 'ChatApp Full',
                    tax_category = TaxCategory.Standard,
                    description  = 'Spend more time engaging with students with ChataApp Education.',
                    image_url    = 'https://paddle-sandbox.s3.amazonaws.com/user/10889/2nmP8MQSret0aWeDemRw_icon1.png',
                    custom_data  = CustomData({
                        'features': {
                            'reports':        True,
                            'crm':            False,
                            'data_retention': True,
                        },
                    }),
                ),
                ReadsFixtures.read_raw_json_fixture('request/create_full'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/products',
            ),
        ],
        ids=[
            "Create product with basic data",
            "Create product with full data",
        ],
    )
    def test_create_product_uses_expected_payload(
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

        response      = test_client.client.products.create(operation)
        response_json = test_client.client.products.response.json()
        request_json  = test_client.client.payload
        last_request  = mock_requests.last_request

        assert isinstance(response, Product)
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
        'operation, expected_request_body, expected_response_status, expected_response_body, expected_url',
        [
            (
                UpdateProduct(name='ChatApp Pro'),
                ReadsFixtures.read_raw_json_fixture('request/update_single'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/products/pro_01h7zcgmdc6tmwtjehp3sh7azf',
            ), (
                UpdateProduct(name='ChatApp Pro', tax_category=TaxCategory.Saas),
                ReadsFixtures.read_raw_json_fixture('request/update_partial'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/products/pro_01h7zcgmdc6tmwtjehp3sh7azf',
            ), (
                UpdateProduct(
                    name         = 'ChatApp Pro',
                    tax_category = TaxCategory.Saas,
                    description  = 'Spend more time engaging with students with ChatApp Pro.',
                    image_url    = 'https://paddle-sandbox.s3.amazonaws.com/pro.png',
                    custom_data  = CustomData({
                        'features': {
                            'reports':        True,
                            'crm':            True,
                            'data_retention': True,
                        },
                    }),
                ),
                ReadsFixtures.read_raw_json_fixture('request/update_full'),
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/products/pro_01h7zcgmdc6tmwtjehp3sh7azf',
            ),
        ],
        ids=[
            "Update product with single new value",
            "Update product with partial new values",
            "Update product with completely new values",
        ],
    )
    def test_update_product_uses_expected_payload(
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
        mock_requests.patch(expected_url, status_code=expected_response_status, text=expected_response_body)

        response      = test_client.client.products.update('pro_01h7zcgmdc6tmwtjehp3sh7azf', operation)
        response_json = test_client.client.products.response.json()
        request_json  = test_client.client.payload
        last_request  = mock_requests.last_request

        assert isinstance(response, Product)
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
        'operation, expected_response_status, expected_url',
        [
            (
                ListProducts(),
                200,
                '/products'
            ), (
                ListProducts(Pager()),
                200,
                '/products?order_by=id[asc]&per_page=50'
            ), (
                ListProducts(Pager(after='pro_01gsz4s0w61y0pp88528f1wvvb')),
                200,
                '/products?after=pro_01gsz4s0w61y0pp88528f1wvvb&order_by=id[asc]&per_page=50'
            ), (
                ListProducts(statuses=[Status.Archived]),
                200,
                '/products?status=archived'
            ), (
                ListProducts(ids=['pro_01gsz4s0w61y0pp88528f1wvvb']),
                200,
                '/products?id=pro_01gsz4s0w61y0pp88528f1wvvb'
            ), (
                ListProducts(ids=['pro_01gsz4s0w61y0pp88528f1wvvb', 'pro_01h1vjes1y163xfj1rh1tkfb65']),
                200,
                '/products?id=pro_01gsz4s0w61y0pp88528f1wvvb,pro_01h1vjes1y163xfj1rh1tkfb65'
            ), (
                ListProducts(tax_categories=[TaxCategory.DigitalGoods, TaxCategory.Standard]),
                200,
                '/products?tax_category=digital-goods,standard'
            ), (
                ListProducts(includes=[ProductIncludes.Prices]),
                200,
                '/products?include=prices'
            ),
        ],
        ids=[
            "List products without pagination",
            "List products with default pagination",
            "List paginated products after specified product id",
            "List products filtered by status",
            "List products filtered by id",
            "List products filtered by multiple ids",
            "List products filtered by tax categories",
            "List products with includes",
        ],
    )
    def test_list_products_returns_expected_response(
        self,
        test_client,
        mock_requests,
        operation,
        expected_response_status,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.get(expected_url, status_code=expected_response_status)

        response     = test_client.client.products.list(operation)
        last_request = mock_requests.last_request

        assert isinstance(response, ProductCollection)
        assert last_request is not None
        assert last_request.method            == 'GET'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"


    @mark.parametrize(
        'product_id, includes, expected_response_status, expected_response_body, expected_url',
        [
            (
                'pro_01h7zcgmdc6tmwtjehp3sh7azf',
                None,
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity'),
                '/products/pro_01h7zcgmdc6tmwtjehp3sh7azf'
            ), (
                'pro_01h7zcgmdc6tmwtjehp3sh7azf',
                [ProductIncludes.Prices],
                200,
                ReadsFixtures.read_raw_json_fixture('response/full_entity_with_includes'),
                '/products/pro_01h7zcgmdc6tmwtjehp3sh7azf?include=prices'
            ),
        ],
        ids=[
            "Get product",
            "Get product with includes",
        ],
    )
    def test_get_products_returns_expected_response(
        self,
        test_client,
        mock_requests,
        product_id,
        includes,
        expected_response_status,
        expected_response_body,
        expected_url,
    ):
        expected_url = f"{test_client.base_url}{expected_url}"
        mock_requests.get(expected_url, status_code=expected_response_status,  text=expected_response_body)

        response      = test_client.client.products.get(product_id, includes=includes)
        response_json = test_client.client.products.response.json()
        last_request  = mock_requests.last_request

        assert isinstance(response, Product) if includes else isinstance(response, Product)
        assert last_request is not None
        assert last_request.method            == 'GET'
        assert test_client.client.status_code == expected_response_status
        assert unquote(last_request.url)      == expected_url, \
            "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(str(expected_response_body)), \
            "The response JSON generated by ResponseParser() doesn't match the expected fixture JSON"
