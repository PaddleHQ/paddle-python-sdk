# AUTO-GENERATED FILE — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/DiscountGroups/DiscountGroupsClient.py
# Regenerate with: python scripts/generate_async_clients.py
from paddle_billing.Resources.DiscountGroups.Operations import (
    CreateDiscountGroup,
    ListDiscountGroups,
    UpdateDiscountGroup,
)
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import DiscountGroupCollection
from paddle_billing.Entities.DiscountGroup import DiscountGroup, DiscountGroupStatus

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient


class AsyncDiscountGroupsClient:
    def __init__(self, client: "AsyncClient"):
        self.client = client
        self.response = None

    async def list(self, operation: ListDiscountGroups | None = None) -> DiscountGroupCollection:
        if operation is None:
            operation = ListDiscountGroups()

        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            return DiscountGroupCollection.from_list(
                parser.get_list(), self.client._make_paginator(parser.get_pagination(), DiscountGroupCollection)
            )
        return await self.client._get("/discount-groups", operation.get_parameters(), parse)

    async def get(self, discount_group_id: str) -> DiscountGroup:
        def parse(response):
            self.response = response
            return DiscountGroup.from_dict(ResponseParser(response).get_dict())
        return await self.client._get(f"/discount-groups/{discount_group_id}", None, parse)

    async def create(self, operation: CreateDiscountGroup) -> DiscountGroup:
        def parse(response):
            self.response = response
            return DiscountGroup.from_dict(ResponseParser(response).get_dict())
        return await self.client._post("/discount-groups", operation, parse)

    async def update(self, discount_group_id: str, operation: UpdateDiscountGroup) -> DiscountGroup:
        def parse(response):
            self.response = response
            return DiscountGroup.from_dict(ResponseParser(response).get_dict())
        return await self.client._patch(f"/discount-groups/{discount_group_id}", operation, parse)

    async def archive(self, discount_group_id: str) -> DiscountGroup:
        return await self.update(discount_group_id, UpdateDiscountGroup(status=DiscountGroupStatus.Archived))
