from json          import loads
from pytest        import mark
from requests_mock import Mocker
from urllib.parse  import unquote

from paddle_billing_python_sdk.Environment      import Environment
from paddle_billing_python_sdk.FiltersUndefined import FiltersUndefined

from paddle_billing_python_sdk.Entities.Product                       import Product
from paddle_billing_python_sdk.Entities.ProductWithIncludes           import ProductWithIncludes
from paddle_billing_python_sdk.Entities.Collections.ProductCollection import ProductCollection
from paddle_billing_python_sdk.Entities.Shared.CustomData             import CustomData
from paddle_billing_python_sdk.Entities.Shared.TaxCategory            import TaxCategory

from paddle_billing_python_sdk.Resources.Events.Operations.ListEvents      import ListEvents
from paddle_billing_python_sdk.Resources.Products.Operations.CreateProduct import CreateProduct
from paddle_billing_python_sdk.Resources.Shared.Operations.List.Pager      import Pager

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
                    f"{Environment.SANDBOX.base_url}/products",
            ),
            (
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
                f"{Environment.SANDBOX.base_url}/products"
            ),
        ],
        ids = [
            "Create product with basic data",
            "Create product with full data",
        ],
    )
    def test_it_uses_expected_payload_on_create(
        self,
        test_client,
        mock_requests,
        operation,
        expected_request_body,
        expected_response_status,
        expected_response_body,
        expected_url
    ):
        mock_requests.post(
            url         = expected_url,
            status_code = expected_response_status,
            text        = expected_response_body
        )

        request_json = test_client.client.serialize_json_payload(
            FiltersUndefined.filter_undefined_values(operation.get_parameters())
        )

        response     = test_client.client.products.create(operation)
        last_request = mock_requests.last_request

        assert isinstance(response, Product)
        assert last_request is not None
        assert last_request.method       == 'POST'
        assert unquote(last_request.url) == expected_url
        assert loads(request_json)       == loads(expected_request_body)
