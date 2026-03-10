from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.SimulationRun import SimulationRun
from paddle_billing.Entities.Collections import AsyncPaginator, SimulationRunCollection

from paddle_billing.Resources.SimulationRuns.Operations import GetSimulationRun, ListSimulationRuns

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient


class AsyncSimulationRunsClient:
    def __init__(self, client: "AsyncClient"):
        self.client = client
        self.response = None

    async def list(self, simulation_id: str, operation: ListSimulationRuns | None = None) -> SimulationRunCollection:
        if operation is None:
            operation = ListSimulationRuns()

        self.response = await self.client.get_raw(f"/simulations/{simulation_id}/runs", operation)
        parser = ResponseParser(self.response)

        return SimulationRunCollection.from_list(
            parser.get_list(), AsyncPaginator(self.client, parser.get_pagination(), SimulationRunCollection)
        )

    async def get(
        self, simulation_id: str, simulation_run_id: str, operation: GetSimulationRun | None = None
    ) -> SimulationRun:
        if operation is None:
            operation = GetSimulationRun()

        self.response = await self.client.get_raw(
            f"/simulations/{simulation_id}/runs/{simulation_run_id}", operation
        )
        parser = ResponseParser(self.response)

        return SimulationRun.from_dict(parser.get_dict())

    async def create(self, simulation_id: str) -> SimulationRun:
        self.response = await self.client.post_raw(f"/simulations/{simulation_id}/runs")
        parser = ResponseParser(self.response)

        return SimulationRun.from_dict(parser.get_dict())
