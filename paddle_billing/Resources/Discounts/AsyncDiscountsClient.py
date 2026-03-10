# AUTO-GENERATED FILE — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/Discounts/DiscountsClient.py
# Regenerate with: python scripts/generate_async_clients.py
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import DiscountCollection
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

        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            return DiscountCollection.from_list(
                parser.get_list(), self.client._make_paginator(parser.get_pagination(), DiscountCollection)
            )
        return await self.client._get("/discounts", operation.get_parameters(), parse)

    async def get(self, discount_id: str, operation: GetDiscount | None = None) -> Discount:
        if operation is None:
            operation = GetDiscount()

        def parse(response):
            self.response = response
            return Discount.from_dict(ResponseParser(response).get_dict())
        return await self.client._get(f"/discounts/{discount_id}", operation.get_parameters(), parse)

    async def create(self, operation: CreateDiscount) -> Discount:
        def parse(response):
            self.response = response
            return Discount.from_dict(ResponseParser(response).get_dict())
        return await self.client._post("/discounts", operation, parse)

    async def update(self, discount_id: str, operation: UpdateDiscount) -> Discount:
        def parse(response):
            self.response = response
            return Discount.from_dict(ResponseParser(response).get_dict())
        return await self.client._patch(f"/discounts/{discount_id}", operation, parse)

    async def archive(self, discount_id: str) -> Discount:
        return await self.update(discount_id, UpdateDiscount(status=DiscountStatus.Archived))
