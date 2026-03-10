# AUTO-GENERATED FILE — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/SimulationRunEvents/SimulationRunEventsClient.py
# Regenerate with: python scripts/generate_async_clients.py
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.SimulationRunEvent import SimulationRunEvent
from paddle_billing.Entities.Collections import SimulationRunEventCollection
from paddle_billing.Resources.SimulationRunEvents.Operations import ListSimulationRunEvents

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient


class AsyncSimulationRunEventsClient:
    def __init__(self, client: "AsyncClient"):
        self.client = client
        self.response = None

    async def list(
        self, simulation_id: str, simulation_run_id: str, operation: ListSimulationRunEvents | None = None
    ) -> SimulationRunEventCollection:
        if operation is None:
            operation = ListSimulationRunEvents()

        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            return SimulationRunEventCollection.from_list(
                parser.get_list(), self.client._make_paginator(parser.get_pagination(), SimulationRunEventCollection)
            )
        return await self.client._get(f"/simulations/{simulation_id}/runs/{simulation_run_id}/events", operation, parse)

    async def get(self, simulation_id: str, simulation_run_id: str, simulation_event_id: str) -> SimulationRunEvent:
        def parse(response):
            self.response = response
            return SimulationRunEvent.from_dict(ResponseParser(response).get_dict())
        return await self.client._get(
            f"/simulations/{simulation_id}/runs/{simulation_run_id}/events/{simulation_event_id}", None, parse
        )

    async def replay(self, simulation_id: str, simulation_run_id: str, simulation_event_id: str) -> SimulationRunEvent:
        def parse(response):
            self.response = response
            return SimulationRunEvent.from_dict(ResponseParser(response).get_dict())
        return await self.client._post(
            f"/simulations/{simulation_id}/runs/{simulation_run_id}/events/{simulation_event_id}/replay", None, parse
        )
