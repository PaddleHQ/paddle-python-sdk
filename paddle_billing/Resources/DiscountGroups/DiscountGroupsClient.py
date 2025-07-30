from paddle_billing.Resources.DiscountGroups.Operations import (
    CreateDiscountGroup,
    ListDiscountGroups,
    UpdateDiscountGroup,
)
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import Paginator, DiscountGroupCollection
from paddle_billing.Entities.DiscountGroup import DiscountGroup

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.Client import Client


class DiscountGroupsClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response = None

    def list(self, operation: ListDiscountGroups | None = None) -> DiscountGroupCollection:
        if operation is None:
            operation = ListDiscountGroups()

        self.response = self.client.get_raw("/discount-groups", operation.get_parameters())
        parser = ResponseParser(self.response)

        return DiscountGroupCollection.from_list(
            parser.get_list(), Paginator(self.client, parser.get_pagination(), DiscountGroupCollection)
        )

    def get(self, discount_group_id: str) -> DiscountGroup:
        self.response = self.client.get_raw(f"/discount-groups/{discount_group_id}")
        parser = ResponseParser(self.response)

        return DiscountGroup.from_dict(parser.get_dict())

    def create(self, operation: CreateDiscountGroup) -> DiscountGroup:
        self.response = self.client.post_raw("/discount-groups", operation)
        parser = ResponseParser(self.response)

        return DiscountGroup.from_dict(parser.get_dict())

    def update(self, discount_group_id: str, operation: UpdateDiscountGroup) -> DiscountGroup:
        self.response = self.client.patch_raw(f"/discount-groups/{discount_group_id}", operation)
        parser = ResponseParser(self.response)

        return DiscountGroup.from_dict(parser.get_dict())
