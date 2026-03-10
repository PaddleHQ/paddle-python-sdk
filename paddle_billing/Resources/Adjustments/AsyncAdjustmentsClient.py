# AUTO-GENERATED FILE — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/Adjustments/AdjustmentsClient.py
# Regenerate with: python scripts/generate_async_clients.py
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Adjustment import Adjustment
from paddle_billing.Entities.AdjustmentCreditNote import AdjustmentCreditNote
from paddle_billing.Entities.Collections import AdjustmentCollection

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

        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            return AdjustmentCollection.from_list(
                parser.get_list(), self.client._make_paginator(parser.get_pagination(), AdjustmentCollection)
            )
        return await self.client._get("/adjustments", operation.get_parameters(), parse)

    async def create(self, operation: CreateAdjustment) -> Adjustment:
        def parse(response):
            self.response = response
            return Adjustment.from_dict(ResponseParser(response).get_dict())
        return await self.client._post("/adjustments", operation, parse)

    async def get_credit_note(self, adjustment_id: str, operation: GetCreditNote | None = None) -> AdjustmentCreditNote:
        def parse(response):
            self.response = response
            return AdjustmentCreditNote.from_dict(ResponseParser(response).get_dict())
        return await self.client._get(f"/adjustments/{adjustment_id}/credit-note", operation, parse)
