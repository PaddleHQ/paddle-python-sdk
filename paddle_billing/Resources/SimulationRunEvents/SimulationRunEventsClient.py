from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.SimulationRunEvent import SimulationRunEvent
from paddle_billing.Entities.Collections import Paginator, SimulationRunEventCollection
from paddle_billing.Resources.SimulationRunEvents.Operations import ListSimulationRunEvents

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.Client import Client


class SimulationRunEventsClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response = None

    def list(
        self, simulation_id: str, simulation_run_id: str, operation: ListSimulationRunEvents | None = None
    ) -> SimulationRunEventCollection:
        if operation is None:
            operation = ListSimulationRunEvents()

        self.response = self.client.get_raw(f"/simulations/{simulation_id}/runs/{simulation_run_id}/events", operation)
        parser = ResponseParser(self.response)

        return SimulationRunEventCollection.from_list(
            parser.get_list(), Paginator(self.client, parser.get_pagination(), SimulationRunEventCollection)
        )

    def get(self, simulation_id: str, simulation_run_id: str, simulation_event_id: str) -> SimulationRunEvent:
        self.response = self.client.get_raw(
            f"/simulations/{simulation_id}/runs/{simulation_run_id}/events/{simulation_event_id}"
        )
        parser = ResponseParser(self.response)

        return SimulationRunEvent.from_dict(parser.get_dict())

    def replay(self, simulation_id: str, simulation_run_id: str, simulation_event_id: str) -> SimulationRunEvent:
        self.response = self.client.post_raw(
            f"/simulations/{simulation_id}/runs/{simulation_run_id}/events/{simulation_event_id}/replay"
        )
        parser = ResponseParser(self.response)

        return SimulationRunEvent.from_dict(parser.get_dict())
