from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Price import Price
from paddle_billing.Entities.Collections import AsyncPaginator, PriceCollection
from paddle_billing.Entities.Shared import Status

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException

from paddle_billing.Resources.Prices.Operations import CreatePrice, ListPrices, UpdatePrice, PriceIncludes

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient


class AsyncPricesClient:
    def __init__(self, client: "AsyncClient"):
        self.client = client
        self.response = None

    async def list(self, operation: ListPrices | None = None) -> PriceCollection:
        if operation is None:
            operation = ListPrices()

        self.response = await self.client.get_raw("/prices", operation.get_parameters())
        parser = ResponseParser(self.response)

        return PriceCollection.from_list(
            parser.get_list(), AsyncPaginator(self.client, parser.get_pagination(), PriceCollection)
        )

    async def get(self, price_id: str, includes=None) -> Price:
        if includes is None:
            includes = []

        invalid_items = [item for item in includes if not isinstance(item, PriceIncludes)]
        if invalid_items:
            raise InvalidArgumentException.array_contains_invalid_types(
                "includes", PriceIncludes.__name__, invalid_items
            )

        params = {"include": ",".join(include.value for include in includes)} if includes else {}
        self.response = await self.client.get_raw(f"/prices/{price_id}", params)
        parser = ResponseParser(self.response)

        return Price.from_dict(parser.get_dict())

    async def create(self, operation: CreatePrice) -> Price:
        self.response = await self.client.post_raw("/prices", operation)
        parser = ResponseParser(self.response)

        return Price.from_dict(parser.get_dict())

    async def update(self, price_id: str, operation: UpdatePrice) -> Price:
        self.response = await self.client.patch_raw(f"/prices/{price_id}", operation)
        parser = ResponseParser(self.response)

        return Price.from_dict(parser.get_dict())

    async def archive(self, price_id: str) -> Price:
        return await self.update(price_id, UpdatePrice(status=Status.Archived))
