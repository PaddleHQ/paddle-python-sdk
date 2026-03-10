from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import AsyncPaginator, ProductCollection
from paddle_billing.Entities.Product import Product
from paddle_billing.Entities.Shared import Status

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException

from paddle_billing.Resources.Products.Operations import CreateProduct, ListProducts, UpdateProduct, ProductIncludes

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient


class AsyncProductsClient:
    def __init__(self, client: "AsyncClient"):
        self.client = client
        self.response = None

    async def list(self, operation: ListProducts | None = None) -> ProductCollection:
        if operation is None:
            operation = ListProducts()

        self.response = await self.client.get_raw("/products", operation.get_parameters())
        parser = ResponseParser(self.response)

        return ProductCollection.from_list(
            parser.get_list(), AsyncPaginator(self.client, parser.get_pagination(), ProductCollection)
        )

    async def get(self, product_id: str, includes=None) -> Product:
        if product_id is None:
            raise ValueError("product_id is required")
        if not isinstance(product_id, str):
            raise ValueError("product_id must be a string")

        if includes is None:
            includes = []

        invalid_items = [item for item in includes if not isinstance(item, ProductIncludes)]
        if invalid_items:
            raise InvalidArgumentException.array_contains_invalid_types(
                "includes", ProductIncludes.__name__, invalid_items
            )

        params = {"include": ",".join(include.value for include in includes)} if includes else {}
        self.response = await self.client.get_raw(f"/products/{product_id}", params)
        parser = ResponseParser(self.response)

        return Product.from_dict(parser.get_dict())

    async def create(self, operation: CreateProduct) -> Product:
        self.response = await self.client.post_raw("/products", operation)
        parser = ResponseParser(self.response)

        return Product.from_dict(parser.get_dict())

    async def update(self, product_id: str, operation: UpdateProduct) -> Product:
        self.response = await self.client.patch_raw(f"/products/{product_id}", operation)
        parser = ResponseParser(self.response)

        return Product.from_dict(parser.get_dict())

    async def archive(self, product_id: str) -> Product:
        return await self.update(product_id, UpdateProduct(status=Status.Archived))
