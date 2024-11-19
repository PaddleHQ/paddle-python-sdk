from json import loads
from pytest import mark
from urllib.parse import unquote

from paddle_billing.Entities.Collections import SimulationRunCollection
from paddle_billing.Entities.SimulationRun import SimulationRun, SimulationRunStatus
from paddle_billing.Entities.Simulation import SimulationScenarioType
from paddle_billing.Resources.SimulationRuns.Operations import ListSimulationRuns, SimulationRunInclude
from paddle_billing.Resources.Shared.Operations import Pager

from tests.Utils.ReadsFixture import ReadsFixtures


class TestSimulationRunsClient:
    @mark.parametrize(
        "simulation_id, expected_response_status, expected_response_body, expected_path",
        [
            (
                "ntfsim_01j82g2mggsgjpb3mjg0xq6p5k",
                200,
                ReadsFixtures.read_raw_json_fixture("response/full_entity"),
                "/simulations/ntfsim_01j82g2mggsgjpb3mjg0xq6p5k/runs",
            ),
        ],
        ids=[
            "Create simulation run",
        ],
    )
    def test_create_simulation_run_uses_expected_payload(
        self,
        test_client,
        mock_requests,
        simulation_id,
        expected_response_status,
        expected_response_body,
        expected_path,
    ):
        expected_url = f"{test_client.base_url}{expected_path}"
        mock_requests.post(expected_url, status_code=expected_response_status, text=expected_response_body)

        response = test_client.client.simulation_runs.create(simulation_id)
        response_json = test_client.client.simulation_runs.response.json()
        request_body = test_client.client.payload
        last_request = mock_requests.last_request

        assert isinstance(response, SimulationRun)
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
        "simulation_id, operation, expected_response_status, expected_response_body, expected_path",
        [
            (
                "ntfsim_01j82g2mggsgjpb3mjg0xq6p5k",
                ListSimulationRuns(),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/simulations/ntfsim_01j82g2mggsgjpb3mjg0xq6p5k/runs",
            ),
            (
                "ntfsim_01j82g2mggsgjpb3mjg0xq6p5k",
                ListSimulationRuns(Pager()),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/simulations/ntfsim_01j82g2mggsgjpb3mjg0xq6p5k/runs?order_by=id[asc]&per_page=50",
            ),
            (
                "ntfsim_01j82g2mggsgjpb3mjg0xq6p5k",
                ListSimulationRuns(Pager(after="ntfsimrun_01j82d9tc19c67jds5vzbzjcns")),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/simulations/ntfsim_01j82g2mggsgjpb3mjg0xq6p5k/runs?after=ntfsimrun_01j82d9tc19c67jds5vzbzjcns&order_by=id[asc]&per_page=50",
            ),
            (
                "ntfsim_01j82g2mggsgjpb3mjg0xq6p5k",
                ListSimulationRuns(includes=[SimulationRunInclude.Events]),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/simulations/ntfsim_01j82g2mggsgjpb3mjg0xq6p5k/runs?include=events",
            ),
            (
                "ntfsim_01j82g2mggsgjpb3mjg0xq6p5k",
                ListSimulationRuns(ids=["ntfsimrun_01j82d9tc19c67jds5vzbzjcns"]),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/simulations/ntfsim_01j82g2mggsgjpb3mjg0xq6p5k/runs?id=ntfsimrun_01j82d9tc19c67jds5vzbzjcns",
            ),
            (
                "ntfsim_01j82g2mggsgjpb3mjg0xq6p5k",
                ListSimulationRuns(
                    ids=["ntfsimrun_01j82d9tc19c67jds5vzbzjcns", "ntfsimrun_02j82d9tc19c67jds5vzbzjcns"]
                ),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/simulations/ntfsim_01j82g2mggsgjpb3mjg0xq6p5k/runs?id=ntfsimrun_01j82d9tc19c67jds5vzbzjcns,ntfsimrun_02j82d9tc19c67jds5vzbzjcns",
            ),
        ],
        ids=[
            "List simulation runs without pagination",
            "List simulation runs with default pagination",
            "List paginated simulation runs after specified simulation run id",
            "List simulation runs with included events",
            "List simulation runs filtered by id",
            "List simulation runs filtered by multiple ids",
        ],
    )
    def test_list_simulation_runs_returns_expected_response(
        self,
        test_client,
        mock_requests,
        simulation_id,
        operation,
        expected_response_status,
        expected_response_body,
        expected_path,
    ):
        expected_url = f"{test_client.base_url}{expected_path}"
        mock_requests.get(expected_url, status_code=expected_response_status, text=expected_response_body)

        response = test_client.client.simulation_runs.list(simulation_id, operation)
        response_json = test_client.client.simulation_runs.response.json()
        last_request = mock_requests.last_request

        assert isinstance(response, SimulationRunCollection)
        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(
            str(expected_response_body)
        ), "The response JSON generated by ResponseParser() doesn't match the expected fixture JSON"

    def test_list_simulation_runs_can_paginate(
        self,
        test_client,
        mock_requests,
    ):
        mock_requests.get(
            f"{test_client.base_url}/simulations/ntfsim_01j82g2mggsgjpb3mjg0xq6p5k/runs",
            status_code=200,
            text=ReadsFixtures.read_raw_json_fixture("response/list_paginated_page_one"),
        )

        mock_requests.get(
            f"{test_client.base_url}/simulations/ntfsim_01j82g2mggsgjpb3mjg0xq6p5k/runs?after=ntfsimrun_01j82gvz2cgw08p7mak3gcd3a3",
            status_code=200,
            text=ReadsFixtures.read_raw_json_fixture("response/list_paginated_page_two"),
        )

        response = test_client.client.simulation_runs.list("ntfsim_01j82g2mggsgjpb3mjg0xq6p5k")

        assert isinstance(response, SimulationRunCollection)

        all_simulation_runs = []
        for simulation_run in response:
            all_simulation_runs.append(simulation_run)

        assert len(all_simulation_runs) == 2

    def test_get_simulation_run_returns_expected_response(
        self,
        test_client,
        mock_requests,
    ):
        simulation_id = "ntfsim_01j82g2mggsgjpb3mjg0xq6p5k"
        simulation_run_id = "ntfsimrun_01j82h13n87yq2sfv187hm2r0p"
        expected_response_body = ReadsFixtures.read_raw_json_fixture("response/full_entity")
        expected_url = f"{test_client.base_url}/simulations/ntfsim_01j82g2mggsgjpb3mjg0xq6p5k/runs/ntfsimrun_01j82h13n87yq2sfv187hm2r0p"

        mock_requests.get(expected_url, status_code=200, text=expected_response_body)

        simulation_run = test_client.client.simulation_runs.get(simulation_id, simulation_run_id)
        response_json = test_client.client.simulation_runs.response.json()
        last_request = mock_requests.last_request

        assert isinstance(simulation_run, SimulationRun)
        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == 200
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(
            str(expected_response_body)
        ), "The response JSON generated by ResponseParser() doesn't match the expected fixture JSON"

        assert simulation_run.id == simulation_run_id
        assert simulation_run.status == SimulationRunStatus.Pending
        assert simulation_run.type == SimulationScenarioType.SubscriptionCreation
        assert simulation_run.created_at.isoformat() == "2024-09-18T12:17:04.168467+00:00"
        assert simulation_run.updated_at.isoformat() == "2024-09-18T12:17:04.168467+00:00"
