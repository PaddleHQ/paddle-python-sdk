from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Adjustment import Adjustment
from paddle_billing.Entities.AdjustmentCreditNote import AdjustmentCreditNote
from paddle_billing.Entities.Collections import AsyncPaginator, AdjustmentCollection

from paddle_billing.Resources.Adjustments.Operations import CreateAdjustment, GetCreditNote, ListAdjustments

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient


class AsyncAdjustmentsClient:
    def __init__(self, client: "AsyncClient"):
        self.client = client
        self.response = None

    async def list(self, operation: ListAdjustments | None = None) -> AdjustmentCollection:
        if operation is None:
            operation = ListAdjustments()

        self.response = await self.client.get_raw("/adjustments", operation.get_parameters())
        parser = ResponseParser(self.response)

        return AdjustmentCollection.from_list(
            parser.get_list(), AsyncPaginator(self.client, parser.get_pagination(), AdjustmentCollection)
        )

    async def create(self, operation: CreateAdjustment) -> Adjustment:
        self.response = await self.client.post_raw("/adjustments", operation)
        parser = ResponseParser(self.response)

        return Adjustment.from_dict(parser.get_dict())

    async def get_credit_note(self, adjustment_id: str, operation: GetCreditNote | None = None) -> AdjustmentCreditNote:
        self.response = await self.client.get_raw(f"/adjustments/{adjustment_id}/credit-note", operation)
        parser = ResponseParser(self.response)

        return AdjustmentCreditNote.from_dict(parser.get_dict())
