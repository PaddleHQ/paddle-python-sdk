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
        self.response = await self.client.get_raw("/simulation-types")
        parser = ResponseParser(self.response)

        return SimulationTypeCollection.from_list(parser.get_list())
