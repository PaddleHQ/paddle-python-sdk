from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import DiscountCollection
from paddle_billing.Entities.Discount import Discount
from paddle_billing.Entities.Discounts import DiscountStatus

from paddle_billing.Resources.Discounts.Operations import CreateDiscount, GetDiscount, ListDiscounts, UpdateDiscount

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.Client import Client


class DiscountsClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response = None

    def list(self, operation: ListDiscounts | None = None) -> DiscountCollection:
        if operation is None:
            operation = ListDiscounts()

        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            return DiscountCollection.from_list(
                parser.get_list(), self.client._make_paginator(parser.get_pagination(), DiscountCollection)
            )
        return self.client._get("/discounts", operation.get_parameters(), parse)

    def get(self, discount_id: str, operation: GetDiscount | None = None) -> Discount:
        if operation is None:
            operation = GetDiscount()

        def parse(response):
            self.response = response
            return Discount.from_dict(ResponseParser(response).get_dict())
        return self.client._get(f"/discounts/{discount_id}", operation.get_parameters(), parse)

    def create(self, operation: CreateDiscount) -> Discount:
        def parse(response):
            self.response = response
            return Discount.from_dict(ResponseParser(response).get_dict())
        return self.client._post("/discounts", operation, parse)

    def update(self, discount_id: str, operation: UpdateDiscount) -> Discount:
        def parse(response):
            self.response = response
            return Discount.from_dict(ResponseParser(response).get_dict())
        return self.client._patch(f"/discounts/{discount_id}", operation, parse)

    def archive(self, discount_id: str) -> Discount:
        return self.update(discount_id, UpdateDiscount(status=DiscountStatus.Archived))
