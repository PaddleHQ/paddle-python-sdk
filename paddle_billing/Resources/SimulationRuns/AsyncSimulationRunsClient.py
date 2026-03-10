# AUTO-GENERATED FILE — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/SimulationRuns/SimulationRunsClient.py
# Regenerate with: python scripts/generate_async_clients.py
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.SimulationRun import SimulationRun
from paddle_billing.Entities.Collections import SimulationRunCollection
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

        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            return SimulationRunCollection.from_list(
                parser.get_list(), self.client._make_paginator(parser.get_pagination(), SimulationRunCollection)
            )
        return await self.client._get(f"/simulations/{simulation_id}/runs", operation, parse)

    async def get(
        self, simulation_id: str, simulation_run_id: str, operation: GetSimulationRun | None = None
    ) -> SimulationRun:
        if operation is None:
            operation = GetSimulationRun()

        def parse(response):
            self.response = response
            return SimulationRun.from_dict(ResponseParser(response).get_dict())
        return await self.client._get(f"/simulations/{simulation_id}/runs/{simulation_run_id}", operation, parse)

    async def create(self, simulation_id: str) -> SimulationRun:
        def parse(response):
            self.response = response
            return SimulationRun.from_dict(ResponseParser(response).get_dict())
        return await self.client._post(f"/simulations/{simulation_id}/runs", None, parse)
