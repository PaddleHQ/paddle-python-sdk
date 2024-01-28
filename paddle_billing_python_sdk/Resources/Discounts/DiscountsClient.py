from typing import TYPE_CHECKING

from paddle_billing_python_sdk.ResponseParser import ResponseParser

from paddle_billing_python_sdk.Entities.Collections.Paginator          import Paginator
from paddle_billing_python_sdk.Entities.Collections.DiscountCollection import DiscountCollection
from paddle_billing_python_sdk.Entities.Discount                       import Discount
from paddle_billing_python_sdk.Entities.Discounts.DiscountStatus       import DiscountStatus

from paddle_billing_python_sdk.Resources.Discounts.Operations.CreateDiscount   import CreateDiscount
from paddle_billing_python_sdk.Resources.Discounts.Operations.ListDiscounts    import ListDiscounts
from paddle_billing_python_sdk.Resources.Discounts.Operations.UpdateDiscount   import UpdateDiscount


if TYPE_CHECKING:
    from paddle_billing_python_sdk.Client import Client


class DiscountsClient:
    def __init__(self, client: 'Client'):
        self.client   = client
        self.response = None


    def list(self, operation: ListDiscounts = None) -> DiscountCollection:
        if operation is None:
            operation = ListDiscounts()

        self.response = self.client.get_raw('/discounts', operation.get_parameters())
        parser        = ResponseParser(self.response)

        return DiscountCollection.from_list(
            parser.get_data(),
            Paginator(self.client, parser.get_pagination(), DiscountCollection)
        )


    def get(self, discount_id: str) -> Discount:
        self.response = self.client.get_raw(f"/discounts/{discount_id}")
        parser        = ResponseParser(self.response)

        return Discount.from_dict(parser.get_data())


    def create(self, operation: CreateDiscount) -> Discount:
        self.response = self.client.post_raw('/discounts', operation.get_parameters())
        parser        = ResponseParser(self.response)

        return Discount.from_dict(parser.get_data())


    def update(self, discount_id: str, operation: UpdateDiscount) -> Discount:
        self.response = self.client.patch_raw(f"/discounts/{discount_id}", operation.get_parameters())
        parser        = ResponseParser(self.response)

        return Discount.from_dict(parser.get_data())


    def archive(self, discount_id: str) -> Discount:
        return self.update(discount_id, UpdateDiscount(status=DiscountStatus.Archived))
