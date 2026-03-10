from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Price import Price
from paddle_billing.Entities.Collections import PriceCollection
from paddle_billing.Entities.Shared import Status

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException

from paddle_billing.Resources.Prices.Operations import CreatePrice, ListPrices, UpdatePrice, PriceIncludes

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.Client import Client


class PricesClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response = None

    def list(self, operation: ListPrices | None = None) -> PriceCollection:
        if operation is None:
            operation = ListPrices()

        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            return PriceCollection.from_list(
                parser.get_list(), self.client._make_paginator(parser.get_pagination(), PriceCollection)
            )
        return self.client._get("/prices", operation.get_parameters(), parse)

    def get(self, price_id: str, includes=None) -> Price:
        if includes is None:
            includes = []

        invalid_items = [item for item in includes if not isinstance(item, PriceIncludes)]
        if invalid_items:
            raise InvalidArgumentException.array_contains_invalid_types(
                "includes", PriceIncludes.__name__, invalid_items
            )

        params = {"include": ",".join(include.value for include in includes)} if includes else {}

        def parse(response):
            self.response = response
            return Price.from_dict(ResponseParser(response).get_dict())
        return self.client._get(f"/prices/{price_id}", params, parse)

    def create(self, operation: CreatePrice) -> Price:
        def parse(response):
            self.response = response
            return Price.from_dict(ResponseParser(response).get_dict())
        return self.client._post("/prices", operation, parse)

    def update(self, price_id: str, operation: UpdatePrice) -> Price:
        def parse(response):
            self.response = response
            return Price.from_dict(ResponseParser(response).get_dict())
        return self.client._patch(f"/prices/{price_id}", operation, parse)

    def archive(self, price_id: str) -> Price:
        return self.update(price_id, UpdatePrice(status=Status.Archived))
