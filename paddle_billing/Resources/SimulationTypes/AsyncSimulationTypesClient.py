# AUTO-GENERATED FILE — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/SimulationTypes/SimulationTypesClient.py
# Regenerate with: python scripts/generate_async_clients.py
from paddle_billing.ResponseParser import ResponseParser
from paddle_billing.Entities.Collections import SimulationTypeCollection

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient


class AsyncSimulationTypesClient:
    def __init__(self, client: "AsyncClient"):
        self.client = client
        self.response = None

    async def list(self) -> SimulationTypeCollection:
        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            return SimulationTypeCollection.from_list(parser.get_list())
        return await self.client._get("/simulation-types", None, parse)
