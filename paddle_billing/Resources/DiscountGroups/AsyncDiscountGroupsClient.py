from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import AsyncPaginator, DiscountGroupCollection
from paddle_billing.Entities.DiscountGroup import DiscountGroup, DiscountGroupStatus

from paddle_billing.Resources.DiscountGroups.Operations import (
    CreateDiscountGroup,
    ListDiscountGroups,
    UpdateDiscountGroup,
)

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

        self.response = await self.client.get_raw("/discount-groups", operation.get_parameters())
        parser = ResponseParser(self.response)

        return DiscountGroupCollection.from_list(
            parser.get_list(), AsyncPaginator(self.client, parser.get_pagination(), DiscountGroupCollection)
        )

    async def get(self, discount_group_id: str) -> DiscountGroup:
        self.response = await self.client.get_raw(f"/discount-groups/{discount_group_id}")
        parser = ResponseParser(self.response)

        return DiscountGroup.from_dict(parser.get_dict())

    async def create(self, operation: CreateDiscountGroup) -> DiscountGroup:
        self.response = await self.client.post_raw("/discount-groups", operation)
        parser = ResponseParser(self.response)

        return DiscountGroup.from_dict(parser.get_dict())

    async def update(self, discount_group_id: str, operation: UpdateDiscountGroup) -> DiscountGroup:
        self.response = await self.client.patch_raw(f"/discount-groups/{discount_group_id}", operation)
        parser = ResponseParser(self.response)

        return DiscountGroup.from_dict(parser.get_dict())

    async def archive(self, discount_group_id: str) -> DiscountGroup:
        return await self.update(discount_group_id, UpdateDiscountGroup(status=DiscountGroupStatus.Archived))
