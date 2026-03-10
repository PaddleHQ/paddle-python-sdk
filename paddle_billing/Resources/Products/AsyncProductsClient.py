# AUTO-GENERATED FILE — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/Products/ProductsClient.py
# Regenerate with: python scripts/generate_async_clients.py
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import ProductCollection
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

        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            return ProductCollection.from_list(
                parser.get_list(), self.client._make_paginator(parser.get_pagination(), ProductCollection)
            )
        return await self.client._get("/products", operation.get_parameters(), parse)

    async def get(self, product_id: str, includes=None) -> Product | Product:
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

        def parse(response):
            self.response = response
            return Product.from_dict(ResponseParser(response).get_dict())
        return await self.client._get(f"/products/{product_id}", params, parse)

    async def create(self, operation: CreateProduct) -> Product:
        def parse(response):
            self.response = response
            return Product.from_dict(ResponseParser(response).get_dict())
        return await self.client._post("/products", operation, parse)

    async def update(self, product_id: str, operation: UpdateProduct) -> Product:
        def parse(response):
            self.response = response
            return Product.from_dict(ResponseParser(response).get_dict())
        return await self.client._patch(f"/products/{product_id}", operation, parse)

    async def archive(self, product_id: str) -> Product:
        return await self.update(product_id, UpdateProduct(status=Status.Archived))
