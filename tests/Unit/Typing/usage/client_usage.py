from os import getenv

from paddle_billing import Client, Environment, Options
from paddle_billing.Entities.Shared.TaxCategory import TaxCategory
from paddle_billing.Exceptions.ApiError import ApiError
from paddle_billing.Resources.Products.Operations import CreateProduct, UpdateProduct

paddle = Client(getenv("PADDLE_API_SECRET_KEY", ""), options=Options(Environment.SANDBOX))

try:
    created = paddle.products.create(CreateProduct(name="My Product", tax_category=TaxCategory.Standard))
    updated = paddle.products.update(created.id, UpdateProduct(name="My Improved Product"))
    print(updated.name)

    for product in paddle.products.list():
        print(product.id)
except ApiError as error:
    print(error.error_code)

response = paddle.products.response
if response is not None:
    print(response.status_code)
