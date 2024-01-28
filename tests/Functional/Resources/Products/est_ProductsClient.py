import pytest
import requests_mock
import json
from paddle_billing_python_sdk.Entities.Shared.TaxCategory                 import TaxCategory
from paddle_billing_python_sdk.Resources.Products.Operations.CreateProduct import CreateProduct


@pytest.mark.parametrize("operation, expected_response, expected_body", [
    (
        CreateProduct(
            name         = 'ChatApp Basic',
            tax_category = TaxCategory('Standard'),
        ),
        {"status": "success"},
        '{"key": "value"}'
    ),
])
def test_it_uses_expected_payload_on_create(client, requests_mock, operation, expected_response, expected_body):
    expected_url = "https://sandbox-environment-url.com/products"

    # Set up mock response
    requests_mock.post(expected_url, json=expected_response)

    # Perform the operation
    response = client.products.create(operation)

    # Assertions
    assert response.json() == expected_response
    last_request = requests_mock.last_request
    assert last_request.method == 'POST'
    assert last_request.url == expected_url
    assert json.loads(last_request.text) == json.loads(expected_body)


# # Override the init_client fixture for this test if necessary
# @pytest.fixture
# def init_client(init_client):
#     # Modify the client or return as is, depending on your needs
#     return init_client
