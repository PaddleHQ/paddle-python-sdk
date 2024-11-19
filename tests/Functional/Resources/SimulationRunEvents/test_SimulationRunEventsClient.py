from json import loads
from pytest import mark
from urllib.parse import unquote

from paddle_billing.Entities.Collections import SimulationRunEventCollection
from paddle_billing.Entities.SimulationRunEvent import (
    SimulationRunEvent,
    SimulationRunEventStatus,
    SimulationRunEventRequest,
    SimulationRunEventResponse,
)
from paddle_billing.Entities.Events import EventTypeName
from paddle_billing.Entities.Notifications.NotificationEvent import NotificationEvent
from paddle_billing.Notifications.Entities.Adjustment import Adjustment, Action
from paddle_billing.Notifications.Entities.Shared import AdjustmentType, AdjustmentStatus
from paddle_billing.Resources.SimulationRunEvents.Operations import ListSimulationRunEvents
from paddle_billing.Resources.Shared.Operations import Pager

from tests.Utils.ReadsFixture import ReadsFixtures


class TestSimulationRunEventsClient:
    @mark.parametrize(
        "simulation_id, simulation_run_id, simulation_event_id, expected_response_status, expected_response_body, expected_path",
        [
            (
                "ntfsim_01j82g2mggsgjpb3mjg0xq6p5k",
                "ntfsimrun_01j82d9tc19c67jds5vzbzjcns",
                "ntfsimevt_01j82j3tr93j99gfv26tsngc27",
                200,
                ReadsFixtures.read_raw_json_fixture("response/full_entity"),
                "/simulations/ntfsim_01j82g2mggsgjpb3mjg0xq6p5k/runs/ntfsimrun_01j82d9tc19c67jds5vzbzjcns/events/ntfsimevt_01j82j3tr93j99gfv26tsngc27/replay",
            ),
        ],
        ids=[
            "Replay simulation run event",
        ],
    )
    def test_replay_simulation_run_event_uses_expected_payload(
        self,
        test_client,
        mock_requests,
        simulation_id,
        simulation_run_id,
        simulation_event_id,
        expected_response_status,
        expected_response_body,
        expected_path,
    ):
        expected_url = f"{test_client.base_url}{expected_path}"
        mock_requests.post(expected_url, status_code=expected_response_status, text=expected_response_body)

        response = test_client.client.simulation_run_events.replay(
            simulation_id, simulation_run_id, simulation_event_id
        )
        response_json = test_client.client.simulation_run_events.response.json()
        request_body = test_client.client.payload
        last_request = mock_requests.last_request

        assert isinstance(response, SimulationRunEvent)
        assert last_request is not None
        assert last_request.method == "POST"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert request_body is None, "The request JSON doesn't match the expected fixture JSON"
        assert response_json == loads(
            str(expected_response_body)
        ), "The response JSON doesn't match the expected fixture JSON"

    @mark.parametrize(
        "simulation_id, simulation_run_id, operation, expected_response_status, expected_response_body, expected_path",
        [
            (
                "ntfsim_01j82g2mggsgjpb3mjg0xq6p5k",
                "ntfsimrun_01j82d9tc19c67jds5vzbzjcns",
                ListSimulationRunEvents(),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/simulations/ntfsim_01j82g2mggsgjpb3mjg0xq6p5k/runs/ntfsimrun_01j82d9tc19c67jds5vzbzjcns/events",
            ),
            (
                "ntfsim_01j82g2mggsgjpb3mjg0xq6p5k",
                "ntfsimrun_01j82d9tc19c67jds5vzbzjcns",
                ListSimulationRunEvents(Pager()),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/simulations/ntfsim_01j82g2mggsgjpb3mjg0xq6p5k/runs/ntfsimrun_01j82d9tc19c67jds5vzbzjcns/events?order_by=id[asc]&per_page=50",
            ),
            (
                "ntfsim_01j82g2mggsgjpb3mjg0xq6p5k",
                "ntfsimrun_01j82d9tc19c67jds5vzbzjcns",
                ListSimulationRunEvents(Pager(after="ntfsimevt_03j82hf8jrwjsf9337a35tqghx")),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/simulations/ntfsim_01j82g2mggsgjpb3mjg0xq6p5k/runs/ntfsimrun_01j82d9tc19c67jds5vzbzjcns/events?after=ntfsimevt_03j82hf8jrwjsf9337a35tqghx&order_by=id[asc]&per_page=50",
            ),
            (
                "ntfsim_01j82g2mggsgjpb3mjg0xq6p5k",
                "ntfsimrun_01j82d9tc19c67jds5vzbzjcns",
                ListSimulationRunEvents(ids=["ntfsimevt_03j82hf8jrwjsf9337a35tqghx"]),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/simulations/ntfsim_01j82g2mggsgjpb3mjg0xq6p5k/runs/ntfsimrun_01j82d9tc19c67jds5vzbzjcns/events?id=ntfsimevt_03j82hf8jrwjsf9337a35tqghx",
            ),
            (
                "ntfsim_01j82g2mggsgjpb3mjg0xq6p5k",
                "ntfsimrun_01j82d9tc19c67jds5vzbzjcns",
                ListSimulationRunEvents(
                    ids=["ntfsimevt_03j82hf8jrwjsf9337a35tqghx", "ntfsimevt_04j82hf8jrwjsf9337a35tqghx"]
                ),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/simulations/ntfsim_01j82g2mggsgjpb3mjg0xq6p5k/runs/ntfsimrun_01j82d9tc19c67jds5vzbzjcns/events?id=ntfsimevt_03j82hf8jrwjsf9337a35tqghx,ntfsimevt_04j82hf8jrwjsf9337a35tqghx",
            ),
        ],
        ids=[
            "List simulation run events without pagination",
            "List simulation run events with default pagination",
            "List paginated simulation run events after specified simulation run event id",
            "List simulation run events filtered by id",
            "List simulation run events filtered by multiple ids",
        ],
    )
    def test_list_simulation_run_events_returns_expected_response(
        self,
        test_client,
        mock_requests,
        simulation_id,
        simulation_run_id,
        operation,
        expected_response_status,
        expected_response_body,
        expected_path,
    ):
        expected_url = f"{test_client.base_url}{expected_path}"
        mock_requests.get(expected_url, status_code=expected_response_status, text=expected_response_body)

        response = test_client.client.simulation_run_events.list(simulation_id, simulation_run_id, operation)
        response_json = test_client.client.simulation_run_events.response.json()
        last_request = mock_requests.last_request

        assert isinstance(response, SimulationRunEventCollection)
        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(
            str(expected_response_body)
        ), "The response JSON generated by ResponseParser() doesn't match the expected fixture JSON"

    def test_list_simulation_run_events_can_paginate(
        self,
        test_client,
        mock_requests,
    ):
        mock_requests.get(
            f"{test_client.base_url}/simulations/ntfsim_01j82g2mggsgjpb3mjg0xq6p5k/runs/ntfsimrun_01j82h13n87yq2sfv187hm2r0p/events",
            status_code=200,
            text=ReadsFixtures.read_raw_json_fixture("response/list_paginated_page_one"),
        )

        mock_requests.get(
            f"{test_client.base_url}/simulations/ntfsim_01j82g2mggsgjpb3mjg0xq6p5k/runs/ntfsimrun_01j82h13n87yq2sfv187hm2r0p/events?after=ntfsimevt_01j82hf8jrwjsf9337a35tqghp",
            status_code=200,
            text=ReadsFixtures.read_raw_json_fixture("response/list_paginated_page_two"),
        )

        response = test_client.client.simulation_run_events.list(
            "ntfsim_01j82g2mggsgjpb3mjg0xq6p5k", "ntfsimrun_01j82h13n87yq2sfv187hm2r0p"
        )

        assert isinstance(response, SimulationRunEventCollection)

        all_simulation_run_events = []
        for simulation_run in response:
            all_simulation_run_events.append(simulation_run)

        assert len(all_simulation_run_events) == 2

    def test_get_simulation_run_event_returns_expected_response(
        self,
        test_client,
        mock_requests,
    ):
        simulation_id = "ntfsim_01j82g2mggsgjpb3mjg0xq6p5k"
        simulation_run_id = "ntfsimrun_01j82h13n87yq2sfv187hm2r0p"
        simulation_event_id = "ntfsimevt_01j82j3tr93j99gfv26tsngc27"
        expected_response_body = ReadsFixtures.read_raw_json_fixture("response/full_entity")
        expected_url = f"{test_client.base_url}/simulations/ntfsim_01j82g2mggsgjpb3mjg0xq6p5k/runs/ntfsimrun_01j82h13n87yq2sfv187hm2r0p/events/ntfsimevt_01j82j3tr93j99gfv26tsngc27"

        mock_requests.get(expected_url, status_code=200, text=expected_response_body)

        simulation_event = test_client.client.simulation_run_events.get(
            simulation_id, simulation_run_id, simulation_event_id
        )
        response_json = test_client.client.simulation_run_events.response.json()
        last_request = mock_requests.last_request

        assert isinstance(simulation_event, SimulationRunEvent)
        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == 200
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(
            str(expected_response_body)
        ), "The response JSON generated by ResponseParser() doesn't match the expected fixture JSON"

        assert simulation_event.id == simulation_event_id
        assert simulation_event.status == SimulationRunEventStatus.Pending
        assert simulation_event.event_type == EventTypeName.AdjustmentCreated
        assert simulation_event.payload
        assert simulation_event.created_at.isoformat() == "2024-09-18T12:36:01.929359+00:00"
        assert simulation_event.updated_at.isoformat() == "2024-09-18T12:37:35.659788+00:00"

        adjustment = simulation_event.payload
        assert isinstance(adjustment, Adjustment)
        assert adjustment.id == "adj_01hvgf2s84dr6reszzg29zbvcm"
        assert adjustment.action == Action.Refund
        assert adjustment.reason == "error"
        assert adjustment.status == AdjustmentStatus.PendingApproval
        assert adjustment.items[0].id == "adjitm_01hvgf2s84dr6reszzg2gx70gj"
        assert adjustment.items[0].type == AdjustmentType.Partial
        assert adjustment.items[0].amount == "100"
        assert adjustment.items[0].totals.tax == "8"
        assert adjustment.items[0].totals.total == "100"
        assert adjustment.items[0].totals.subtotal == "92"
        assert adjustment.items[0].item_id == "txnitm_01hvcc94b7qgz60qmrqmbm19zw"
        assert adjustment.items[0].proration is None
        assert adjustment.totals.fee == "5"
        assert adjustment.totals.tax == "8"
        assert adjustment.totals.total == "100"
        assert adjustment.totals.earnings == "87"
        assert adjustment.totals.subtotal == "92"
        assert adjustment.totals.currency_code.value == "USD"
        assert adjustment.payout_totals.fee == "5"
        assert adjustment.payout_totals.tax == "8"
        assert adjustment.payout_totals.total == "100"
        assert adjustment.payout_totals.earnings == "87"
        assert adjustment.payout_totals.subtotal == "92"
        assert adjustment.payout_totals.currency_code.value == "USD"
        assert adjustment.created_at.isoformat() == "2024-04-15T08:48:20.239695+00:00"
        assert adjustment.updated_at.isoformat() == "2024-04-15T08:48:20.239695+00:00"
        assert adjustment.customer_id == "ctm_01hv6y1jedq4p1n0yqn5ba3ky4"
        assert adjustment.transaction_id == "txn_01hvcc93znj3mpqt1tenkjb04y"
        assert adjustment.subscription_id == "sub_01hvccbx32q2gb40sqx7n42430"
        assert adjustment.credit_applied_to_balance is None

        request = simulation_event.request
        assert isinstance(request, SimulationRunEventRequest)

        notification_event = NotificationEvent.from_dict(loads(request.body))
        assert notification_event.event_id == "ntfsimevt_01j82hf8jrwjsf9337a35tqghp"
        assert notification_event.notification_id == "ntfsimntf_02j82hf8jrwjsf9337a35tqghp"
        assert isinstance(notification_event.data, Adjustment)

        response = simulation_event.response
        assert isinstance(response, SimulationRunEventResponse)
        assert response.status_code == 200
        assert loads(response.body)["message"] == "success"
