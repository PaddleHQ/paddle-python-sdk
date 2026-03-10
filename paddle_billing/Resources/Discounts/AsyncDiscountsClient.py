from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import AsyncPaginator, DiscountCollection
from paddle_billing.Entities.Discount import Discount
from paddle_billing.Entities.Discounts import DiscountStatus

from paddle_billing.Resources.Discounts.Operations import CreateDiscount, GetDiscount, ListDiscounts, UpdateDiscount

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient


class AsyncDiscountsClient:
    def __init__(self, client: "AsyncClient"):
        self.client = client
        self.response = None

    async def list(self, operation: ListDiscounts | None = None) -> DiscountCollection:
        if operation is None:
            operation = ListDiscounts()

        self.response = await self.client.get_raw("/discounts", operation.get_parameters())
        parser = ResponseParser(self.response)

        return DiscountCollection.from_list(
            parser.get_list(), AsyncPaginator(self.client, parser.get_pagination(), DiscountCollection)
        )

    async def get(self, discount_id: str, operation: GetDiscount | None = None) -> Discount:
        if operation is None:
            operation = GetDiscount()

        self.response = await self.client.get_raw(f"/discounts/{discount_id}", operation.get_parameters())
        parser = ResponseParser(self.response)

        return Discount.from_dict(parser.get_dict())

    async def create(self, operation: CreateDiscount) -> Discount:
        self.response = await self.client.post_raw("/discounts", operation)
        parser = ResponseParser(self.response)

        return Discount.from_dict(parser.get_dict())

    async def update(self, discount_id: str, operation: UpdateDiscount) -> Discount:
        self.response = await self.client.patch_raw(f"/discounts/{discount_id}", operation)
        parser = ResponseParser(self.response)

        return Discount.from_dict(parser.get_dict())

    async def archive(self, discount_id: str) -> Discount:
        return await self.update(discount_id, UpdateDiscount(status=DiscountStatus.Archived))
