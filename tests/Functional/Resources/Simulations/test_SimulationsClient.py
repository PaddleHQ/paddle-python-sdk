from json import loads, dumps
from pytest import mark
from urllib.parse import unquote
from datetime import datetime

from paddle_billing.Client import PayloadEncoder
from paddle_billing.Entities.Collections import SimulationCollection
from paddle_billing.Entities.Simulation import Simulation, SimulationScenarioType, SimulationStatus
from paddle_billing.Entities.Simulations.Config.Options import (
    BusinessSimulatedAs,
    CustomerSimulatedAs,
    DiscountSimulatedAs,
    DunningExhaustedAction,
    EffectiveFrom,
)
from paddle_billing.Notifications.Entities.Simulations import Address
from paddle_billing.Notifications.Entities.Simulations.SimulationEntity import SimulationEntity
from paddle_billing.Notifications.Entities.Simulations.Adjustment import Adjustment
from paddle_billing.Entities.Events import EventTypeName
from paddle_billing.Notifications.Entities.Shared import (
    CountryCode,
    CustomData,
    ImportMeta,
    Status,
)

from paddle_billing.Resources.Simulations.Operations import CreateSimulation, ListSimulations, UpdateSimulation
from paddle_billing.Resources.Shared.Operations import Pager

from paddle_billing.Resources.Simulations.Operations.Config.Subscription.Cancellation import (
    SubscriptionCancellationConfigCreate,
    SubscriptionCancellationEntitiesCreate,
    SubscriptionCancellationOptionsCreate,
)
from paddle_billing.Resources.Simulations.Operations.Config.Subscription.Creation import (
    SubscriptionCreationConfigCreate,
    SubscriptionCreationEntitiesCreate,
    SubscriptionCreationOptionsCreate,
    SubscriptionCreationItemCreate,
)
from paddle_billing.Resources.Simulations.Operations.Config.Subscription.Pause import (
    SubscriptionPauseConfigCreate,
    SubscriptionPauseEntitiesCreate,
    SubscriptionPauseOptionsCreate,
)
from paddle_billing.Resources.Simulations.Operations.Config.Subscription.Renewal import (
    SubscriptionRenewalConfigCreate,
    SubscriptionRenewalEntitiesCreate,
    SubscriptionRenewalOptionsCreate,
)
from paddle_billing.Resources.Simulations.Operations.Config.Subscription.Resume import (
    SubscriptionResumeConfigCreate,
    SubscriptionResumeEntitiesCreate,
    SubscriptionResumeOptionsCreate,
)
from tests.Utils.ReadsFixture import ReadsFixtures


class TestSimulationsClient:
    @mark.parametrize(
        "operation, expected_request_body, expected_response_status, expected_response_body, expected_path",
        [
            (
                CreateSimulation(
                    notification_setting_id="ntfset_01j82d983j814ypzx7m1fw2jpz",
                    type=EventTypeName.AddressCreated,
                    name="New US address created for CRM",
                    payload=Address(
                        id="add_01hv8gq3318ktkfengj2r75gfx",
                        city="New York",
                        region="NY",
                        status=Status.Active,
                        first_line="4050 Jefferson Plaza, 41st Floor",
                        customer_id="ctm_01hv6y1jedq4p1n0yqn5ba3ky4",
                        description="Head Office",
                        postal_code="10021",
                        second_line=None,
                        country_code=CountryCode.US,
                        created_at=datetime.fromisoformat("2024-04-12T06:42:58.785000Z"),
                        updated_at=datetime.fromisoformat("2024-04-12T06:42:58.785000Z"),
                        custom_data=CustomData(
                            {
                                "some": "data",
                            }
                        ),
                        import_meta=ImportMeta(
                            external_id="some-external-id",
                            imported_from="some-source",
                        ),
                    ),
                ),
                ReadsFixtures.read_raw_json_fixture("request/create_full"),
                201,
                ReadsFixtures.read_raw_json_fixture("response/full_entity"),
                "/simulations",
            ),
            (
                CreateSimulation(
                    notification_setting_id="ntfset_01j82d983j814ypzx7m1fw2jpz",
                    type=EventTypeName.AddressCreated,
                    name="New US address created for CRM",
                    payload=None,
                ),
                ReadsFixtures.read_raw_json_fixture("request/create_without_payload"),
                201,
                ReadsFixtures.read_raw_json_fixture("response/full_entity"),
                "/simulations",
            ),
            (
                CreateSimulation(
                    notification_setting_id="ntfset_01j82d983j814ypzx7m1fw2jpz",
                    type=SimulationScenarioType.SubscriptionResume,
                    name="Some Scenario",
                ),
                ReadsFixtures.read_raw_json_fixture("request/create_scenario"),
                201,
                ReadsFixtures.read_raw_json_fixture("response/full_entity"),
                "/simulations",
            ),
        ],
        ids=[
            "Create single event simulation with entity",
            "Create single event simulation without entity",
            "Create scenario simulation",
        ],
    )
    def test_create_simulation_uses_expected_payload(
        self,
        test_client,
        mock_requests,
        operation,
        expected_request_body,
        expected_response_status,
        expected_response_body,
        expected_path,
    ):
        expected_url = f"{test_client.base_url}{expected_path}"
        mock_requests.post(expected_url, status_code=expected_response_status, text=expected_response_body)

        response = test_client.client.simulations.create(operation)
        response_json = test_client.client.simulations.response.json()
        request_json = test_client.client.payload
        last_request = mock_requests.last_request

        assert isinstance(response, Simulation)
        assert last_request is not None
        assert last_request.method == "POST"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert loads(request_json) == loads(
            expected_request_body
        ), "The request JSON doesn't match the expected fixture JSON"
        assert response_json == loads(
            str(expected_response_body)
        ), "The response JSON doesn't match the expected fixture JSON"

    @mark.parametrize(
        "event_type, entity_name",
        [
            ("address.created", "Address"),
            ("address.imported", "Address"),
            ("address.updated", "Address"),
            ("adjustment.created", "Adjustment"),
            ("adjustment.updated", "Adjustment"),
            ("api_key.created", "ApiKey"),
            ("api_key.expired", "ApiKey"),
            ("api_key.expiring", "ApiKey"),
            ("api_key_exposure.created", "ApiKeyExposure"),
            ("api_key.revoked", "ApiKey"),
            ("api_key.updated", "ApiKey"),
            ("business.created", "Business"),
            ("business.imported", "Business"),
            ("business.updated", "Business"),
            ("customer.created", "Customer"),
            ("customer.imported", "Customer"),
            ("customer.updated", "Customer"),
            ("discount.created", "Discount"),
            ("discount.imported", "Discount"),
            ("discount.updated", "Discount"),
            ("payment_method.deleted", "PaymentMethodDeleted"),
            ("payment_method.saved", "PaymentMethod"),
            ("payout.created", "Payout"),
            ("payout.paid", "Payout"),
            ("price.created", "Price"),
            ("price.updated", "Price"),
            ("price.imported", "Price"),
            ("product.created", "Product"),
            ("product.updated", "Product"),
            ("product.imported", "Product"),
            ("subscription.activated", "Subscription"),
            ("subscription.canceled", "Subscription"),
            ("subscription.created", "SubscriptionCreated"),
            ("subscription.imported", "Subscription"),
            ("subscription.past_due", "Subscription"),
            ("subscription.paused", "Subscription"),
            ("subscription.resumed", "Subscription"),
            ("subscription.trialing", "Subscription"),
            ("subscription.updated", "Subscription"),
            ("transaction.billed", "Transaction"),
            ("transaction.canceled", "Transaction"),
            ("transaction.completed", "Transaction"),
            ("transaction.created", "Transaction"),
            ("transaction.paid", "Transaction"),
            ("transaction.past_due", "Transaction"),
            ("transaction.payment_failed", "Transaction"),
            ("transaction.ready", "Transaction"),
            ("transaction.revised", "Transaction"),
            ("transaction.updated", "Transaction"),
            ("report.created", "Report"),
            ("report.updated", "Report"),
        ],
        ids=[
            "address.created",
            "address.imported",
            "address.updated",
            "adjustment.created",
            "adjustment.updated",
            "api_key.created",
            "api_key.expired",
            "api_key.expiring",
            "api_key_exposure.created",
            "api_key.revoked",
            "api_key.updated",
            "business.created",
            "business.imported",
            "business.updated",
            "customer.created",
            "customer.imported",
            "customer.updated",
            "discount.created",
            "discount.imported",
            "discount.updated",
            "payment_method.deleted",
            "payment_method.saved",
            "payout.created",
            "payout.paid",
            "price.created",
            "price.updated",
            "price.imported",
            "product.created",
            "product.updated",
            "product.imported",
            "subscription.activated",
            "subscription.canceled",
            "subscription.created",
            "subscription.imported",
            "subscription.past_due",
            "subscription.paused",
            "subscription.resumed",
            "subscription.trialing",
            "subscription.updated",
            "transaction.billed",
            "transaction.canceled",
            "transaction.completed",
            "transaction.created",
            "transaction.paid",
            "transaction.past_due",
            "transaction.payment_failed",
            "transaction.ready",
            "transaction.revised",
            "transaction.updated",
            "report.created",
            "report.updated",
        ],
    )
    def test_create_simulation_uses_expected_entity_payload(
        self,
        test_client,
        mock_requests,
        event_type,
        entity_name,
    ):
        entity_data = ReadsFixtures.read_json_fixture(f"payload/{event_type}")
        payload = SimulationEntity.from_dict_for_event_type(entity_data, event_type)
        assert payload.__class__.__name__ == entity_name
        assert isinstance(payload, SimulationEntity)

        operation = CreateSimulation(
            notification_setting_id="ntfset_01j82d983j814ypzx7m1fw2jpz",
            type=EventTypeName(event_type),
            name="Some Simulation",
            payload=payload,
        )

        expected_path = "/simulations"

        expected_request_body = dumps(
            {
                "notification_setting_id": "ntfset_01j82d983j814ypzx7m1fw2jpz",
                "name": "Some Simulation",
                "type": event_type,
                "payload": entity_data,
            }
        )

        expected_response_body = dumps(
            {
                "data": {
                    "id": "ntfsim_01j82g2mggsgjpb3mjg0xq6p5k",
                    "notification_setting_id": "ntfset_01j82d983j814ypzx7m1fw2jpz",
                    "name": "Some Simulation",
                    "type": event_type,
                    "status": "active",
                    "payload": entity_data,
                    "last_run_at": None,
                    "created_at": "2024-09-18T12:00:25.616392Z",
                    "updated_at": "2024-09-18T12:00:25.616392Z",
                },
            }
        )

        expected_url = f"{test_client.base_url}{expected_path}"
        mock_requests.post(expected_url, status_code=201, text=expected_response_body)

        response = test_client.client.simulations.create(operation)
        response_json = test_client.client.simulations.response.json()
        request_json = test_client.client.payload
        last_request = mock_requests.last_request

        assert isinstance(response, Simulation)
        assert last_request is not None
        assert last_request.method == "POST"
        assert test_client.client.status_code == 201
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert loads(request_json) == loads(
            expected_request_body
        ), "The request JSON doesn't match the expected fixture JSON"
        assert response_json == loads(
            str(expected_response_body)
        ), "The response JSON doesn't match the expected fixture JSON"
        assert isinstance(response.payload, payload.__class__)

        # Check partial payloads are accepted.
        partial_payload = SimulationEntity.from_dict_for_event_type({"id": entity_data["id"]}, event_type)
        assert isinstance(partial_payload, SimulationEntity)

        partial_operation = CreateSimulation(
            notification_setting_id="ntfset_01j82d983j814ypzx7m1fw2jpz",
            type=EventTypeName(event_type),
            name="Some Simulation",
            payload=partial_payload,
        )

        expected_partial_request_body = dumps(
            {
                "notification_setting_id": "ntfset_01j82d983j814ypzx7m1fw2jpz",
                "name": "Some Simulation",
                "type": event_type,
                "payload": {"id": entity_data["id"]},
            }
        )

        expected_partial_response_body = dumps(
            {
                "data": {
                    "id": "ntfsim_01j82g2mggsgjpb3mjg0xq6p5k",
                    "notification_setting_id": "ntfset_01j82d983j814ypzx7m1fw2jpz",
                    "name": "Some Simulation",
                    "type": event_type,
                    "status": "active",
                    "payload": {"id": entity_data["id"]},
                    "last_run_at": None,
                    "created_at": "2024-09-18T12:00:25.616392Z",
                    "updated_at": "2024-09-18T12:00:25.616392Z",
                },
            }
        )

        mock_requests.post(expected_url, status_code=201, text=expected_partial_response_body)

        partial_response = test_client.client.simulations.create(partial_operation)
        partial_response_json = test_client.client.simulations.response.json()
        partial_request_json = test_client.client.payload
        partial_last_request = mock_requests.last_request

        assert isinstance(partial_response, Simulation)
        assert partial_last_request is not None
        assert partial_last_request.method == "POST"
        assert test_client.client.status_code == 201
        assert (
            unquote(partial_last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert loads(partial_request_json) == loads(
            expected_partial_request_body
        ), "The request JSON doesn't match the expected fixture JSON"
        assert partial_response_json == loads(
            str(expected_partial_response_body)
        ), "The response JSON doesn't match the expected fixture JSON"
        assert isinstance(partial_response.payload, partial_payload.__class__)
        assert partial_response.payload.id == entity_data["id"]

    @mark.parametrize(
        "operation, expected_request_body, expected_response_status, expected_response_body, expected_path",
        [
            (
                UpdateSimulation(status=SimulationStatus.Archived),
                ReadsFixtures.read_raw_json_fixture("request/update_single"),
                200,
                ReadsFixtures.read_raw_json_fixture("response/full_entity"),
                "/simulations/ntfsim_01j82g2mggsgjpb3mjg0xq6p5k",
            ),
            (
                UpdateSimulation(
                    notification_setting_id="ntfset_01j82d983j814ypzx7m1fw2jpz",
                    name="New simulation name",
                ),
                ReadsFixtures.read_raw_json_fixture("request/update_partial"),
                200,
                ReadsFixtures.read_raw_json_fixture("response/full_entity"),
                "/simulations/ntfsim_01j82g2mggsgjpb3mjg0xq6p5k",
            ),
            (
                UpdateSimulation(
                    notification_setting_id="ntfset_01j82d983j814ypzx7m1fw2jpz",
                    type=EventTypeName.AdjustmentUpdated,
                    name="Refund approved",
                    status=SimulationStatus.Active,
                    payload=Adjustment.from_dict(ReadsFixtures.read_json_fixture("request/adjustment_updated_payload")),
                ),
                ReadsFixtures.read_raw_json_fixture("request/update_full"),
                200,
                ReadsFixtures.read_raw_json_fixture("response/full_entity_adjustment_updated"),
                "/simulations/ntfsim_01j82g2mggsgjpb3mjg0xq6p5k",
            ),
        ],
        ids=[
            "Update simulation with single new value",
            "Update simulation with partial new values",
            "Update simulation with completely new values",
        ],
    )
    def test_update_simulation_uses_expected_payload(
        self,
        test_client,
        mock_requests,
        operation,
        expected_request_body,
        expected_response_status,
        expected_response_body,
        expected_path,
    ):
        expected_url = f"{test_client.base_url}{expected_path}"
        mock_requests.patch(expected_url, status_code=expected_response_status, text=expected_response_body)

        response = test_client.client.simulations.update("ntfsim_01j82g2mggsgjpb3mjg0xq6p5k", operation)
        response_json = test_client.client.simulations.response.json()
        request_json = test_client.client.payload
        last_request = mock_requests.last_request

        assert isinstance(response, Simulation)
        assert last_request is not None
        assert last_request.method == "PATCH"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert loads(request_json) == loads(
            expected_request_body
        ), "The request JSON doesn't match the expected fixture JSON"
        assert response_json == loads(
            str(expected_response_body)
        ), "The response JSON doesn't match the expected fixture JSON"

    @mark.parametrize(
        "operation, expected_response_status, expected_response_body, expected_path",
        [
            (
                ListSimulations(),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/simulations",
            ),
            (
                ListSimulations(Pager()),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/simulations?order_by=id[asc]&per_page=50",
            ),
            (
                ListSimulations(Pager(after="ntfsim_01j82d9tc19c67jds5vzbzjcns")),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/simulations?after=ntfsim_01j82d9tc19c67jds5vzbzjcns&order_by=id[asc]&per_page=50",
            ),
            (
                ListSimulations(statuses=[SimulationStatus.Archived]),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/simulations?status=archived",
            ),
            (
                ListSimulations(ids=["ntfsim_01j82d9tc19c67jds5vzbzjcns"]),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/simulations?id=ntfsim_01j82d9tc19c67jds5vzbzjcns",
            ),
            (
                ListSimulations(ids=["ntfsim_01j82d9tc19c67jds5vzbzjcns", "ntfsim_02j82d9tc19c67jds5vzbzjcns"]),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/simulations?id=ntfsim_01j82d9tc19c67jds5vzbzjcns,ntfsim_02j82d9tc19c67jds5vzbzjcns",
            ),
            (
                ListSimulations(notification_setting_ids=["ntfset_01j82d983j814ypzx7m1fw2jpz"]),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/simulations?notification_setting_id=ntfset_01j82d983j814ypzx7m1fw2jpz",
            ),
            (
                ListSimulations(
                    notification_setting_ids=["ntfset_01j82d983j814ypzx7m1fw2jpz", "ntfset_02j82d983j814ypzx7m1fw2jpz"]
                ),
                200,
                ReadsFixtures.read_raw_json_fixture("response/list_default"),
                "/simulations?notification_setting_id=ntfset_01j82d983j814ypzx7m1fw2jpz,ntfset_02j82d983j814ypzx7m1fw2jpz",
            ),
        ],
        ids=[
            "List simulations without pagination",
            "List simulations with default pagination",
            "List paginated simulations after specified simulation id",
            "List simulations filtered by status",
            "List simulations filtered by id",
            "List simulations filtered by multiple ids",
            "List simulations filtered by notification setting id",
            "List simulations filtered by multiple notification setting ids",
        ],
    )
    def test_list_simulations_returns_expected_response(
        self,
        test_client,
        mock_requests,
        operation,
        expected_response_status,
        expected_response_body,
        expected_path,
    ):
        expected_url = f"{test_client.base_url}{expected_path}"
        mock_requests.get(expected_url, status_code=expected_response_status, text=expected_response_body)

        response = test_client.client.simulations.list(operation)
        response_json = test_client.client.simulations.response.json()
        last_request = mock_requests.last_request

        assert isinstance(response, SimulationCollection)
        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == expected_response_status
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(
            str(expected_response_body)
        ), "The response JSON generated by ResponseParser() doesn't match the expected fixture JSON"

    def test_list_simulations_can_paginate(
        self,
        test_client,
        mock_requests,
    ):
        mock_requests.get(
            f"{test_client.base_url}/simulations",
            status_code=200,
            text=ReadsFixtures.read_raw_json_fixture("response/list_paginated_page_one"),
        )

        mock_requests.get(
            f"{test_client.base_url}/simulations?after=ntfsim_01j82fs5pvrdse93e1kawqy2fr",
            status_code=200,
            text=ReadsFixtures.read_raw_json_fixture("response/list_paginated_page_two"),
        )

        response = test_client.client.simulations.list()

        assert isinstance(response, SimulationCollection)

        all_simulations = []
        for simulation in response:
            all_simulations.append(simulation)

        assert len(all_simulations) == 2

    def test_get_simulations_returns_expected_response(
        self,
        test_client,
        mock_requests,
    ):
        simulation_id = "ntfsim_01j82g2mggsgjpb3mjg0xq6p5k"
        expected_response_body = ReadsFixtures.read_raw_json_fixture("response/full_entity")
        expected_url = f"{test_client.base_url}/simulations/ntfsim_01j82g2mggsgjpb3mjg0xq6p5k"

        mock_requests.get(expected_url, status_code=200, text=expected_response_body)

        simulation = test_client.client.simulations.get(simulation_id)
        response_json = test_client.client.simulations.response.json()
        last_request = mock_requests.last_request

        assert isinstance(simulation, Simulation)
        assert last_request is not None
        assert last_request.method == "GET"
        assert test_client.client.status_code == 200
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert response_json == loads(
            str(expected_response_body)
        ), "The response JSON generated by ResponseParser() doesn't match the expected fixture JSON"

        assert simulation.id == simulation_id
        assert simulation.name == "New US address created for CRM"
        assert simulation.notification_setting_id == "ntfset_01j82d983j814ypzx7m1fw2jpz"
        assert simulation.type == EventTypeName.AddressCreated
        assert simulation.last_run_at is None
        assert simulation.created_at.isoformat() == "2024-09-18T12:00:25.616392+00:00"
        assert simulation.updated_at.isoformat() == "2024-09-18T12:00:25.616392+00:00"

        address = simulation.payload
        assert isinstance(address, Address)

        assert address.id == "add_01hv8gq3318ktkfengj2r75gfx"
        assert address.city == "New York"
        assert address.region == "NY"
        assert address.status == Status.Active
        assert address.first_line == "4050 Jefferson Plaza, 41st Floor"
        assert address.customer_id == "ctm_01hv6y1jedq4p1n0yqn5ba3ky4"
        assert address.description == "Head Office"
        assert address.postal_code == "10021"
        assert address.second_line is None
        assert address.country_code == CountryCode.US
        assert address.created_at.isoformat() == "2024-04-12T06:42:58.785000+00:00"
        assert address.updated_at.isoformat() == "2024-04-12T06:42:58.785000+00:00"
        assert address.custom_data is None
        assert address.import_meta is None

    @mark.parametrize(
        "type, config, expected_request_config, expected_response_body",
        [
            (
                SimulationScenarioType.SubscriptionCreation,
                SubscriptionCreationConfigCreate(
                    entities=SubscriptionCreationEntitiesCreate(
                        customer_id="ctm_01h04vsc0qhwtsbsxh3422wjs4",
                        address_id="add_01h04vsc0qhwtsbsxh3422wjs4",
                        business_id="biz_01h04vsc0qhwtsbsxh3422wjs4",
                        payment_method_id="paymtd_01h04vsc0qhwtsbsxh3422wjs4",
                        discount_id="dsc_01h04vsc0qhwtsbsxh3422wjs4",
                        transaction_id="txn_01h04vsc0qhwtsbsxh3422wjs4",
                    ),
                    options=SubscriptionCreationOptionsCreate(
                        customer_simulated_as=CustomerSimulatedAs.New,
                        business_simulated_as=BusinessSimulatedAs.New,
                        discount_simulated_as=DiscountSimulatedAs.NotProvided,
                    ),
                ),
                ReadsFixtures.read_json_fixture("config/subscription_creation_txn_id"),
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_subscription_creation_txn_id"),
            ),
            (
                SimulationScenarioType.SubscriptionCreation,
                SubscriptionCreationConfigCreate(
                    entities=SubscriptionCreationEntitiesCreate(
                        customer_id="ctm_01h04vsc0qhwtsbsxh3422wjs4",
                        address_id="add_01h04vsc0qhwtsbsxh3422wjs4",
                        business_id="biz_01h04vsc0qhwtsbsxh3422wjs4",
                        payment_method_id="paymtd_01h04vsc0qhwtsbsxh3422wjs4",
                        discount_id="dsc_01h04vsc0qhwtsbsxh3422wjs4",
                        items=[
                            SubscriptionCreationItemCreate(
                                price_id="pri_01h04vsc0qhwtsbsxh3422wjs4",
                                quantity=1,
                            ),
                        ],
                    ),
                    options=SubscriptionCreationOptionsCreate(
                        customer_simulated_as=CustomerSimulatedAs.New,
                        business_simulated_as=BusinessSimulatedAs.New,
                        discount_simulated_as=DiscountSimulatedAs.NotProvided,
                    ),
                ),
                ReadsFixtures.read_json_fixture("config/subscription_creation_new_customer"),
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_subscription_creation"),
            ),
            (
                SimulationScenarioType.SubscriptionCreation,
                SubscriptionCreationConfigCreate(
                    entities=SubscriptionCreationEntitiesCreate(
                        customer_id="ctm_01h04vsc0qhwtsbsxh3422wjs4",
                        address_id="add_01h04vsc0qhwtsbsxh3422wjs4",
                        business_id="biz_01h04vsc0qhwtsbsxh3422wjs4",
                        payment_method_id="paymtd_01h04vsc0qhwtsbsxh3422wjs4",
                        discount_id="dsc_01h04vsc0qhwtsbsxh3422wjs4",
                        items=[
                            SubscriptionCreationItemCreate(
                                price_id="pri_01h04vsc0qhwtsbsxh3422wjs4",
                                quantity=1,
                            ),
                        ],
                    ),
                    options=SubscriptionCreationOptionsCreate(
                        customer_simulated_as=CustomerSimulatedAs.ExistingEmailMatched,
                        business_simulated_as=BusinessSimulatedAs.NotProvided,
                        discount_simulated_as=DiscountSimulatedAs.EnteredByCustomer,
                    ),
                ),
                ReadsFixtures.read_json_fixture("config/subscription_creation_matching_customer"),
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_subscription_creation"),
            ),
            (
                SimulationScenarioType.SubscriptionCreation,
                SubscriptionCreationConfigCreate(
                    entities=SubscriptionCreationEntitiesCreate(
                        customer_id="ctm_01h04vsc0qhwtsbsxh3422wjs4",
                        address_id="add_01h04vsc0qhwtsbsxh3422wjs4",
                        business_id="biz_01h04vsc0qhwtsbsxh3422wjs4",
                        payment_method_id="paymtd_01h04vsc0qhwtsbsxh3422wjs4",
                        discount_id="dsc_01h04vsc0qhwtsbsxh3422wjs4",
                        items=[
                            SubscriptionCreationItemCreate(
                                price_id="pri_01h04vsc0qhwtsbsxh3422wjs4",
                                quantity=1,
                            ),
                        ],
                    ),
                    options=SubscriptionCreationOptionsCreate(
                        customer_simulated_as=CustomerSimulatedAs.ExistingDetailsPrefilled,
                        business_simulated_as=BusinessSimulatedAs.ExistingDetailsPrefilled,
                        discount_simulated_as=DiscountSimulatedAs.NotProvided,
                    ),
                ),
                ReadsFixtures.read_json_fixture("config/subscription_creation_prefilled_customer"),
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_subscription_creation"),
            ),
            (
                SimulationScenarioType.SubscriptionCreation,
                SubscriptionCreationConfigCreate(
                    entities=SubscriptionCreationEntitiesCreate(),
                    options=SubscriptionCreationOptionsCreate(),
                ),
                {
                    "subscription_creation": {
                        "entities": {},
                        "options": {},
                    }
                },
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_subscription_creation"),
            ),
            (
                SimulationScenarioType.SubscriptionRenewal,
                SubscriptionRenewalConfigCreate(
                    entities=SubscriptionRenewalEntitiesCreate(
                        subscription_id="sub_01h04vsc0qhwtsbsxh3422wjs4",
                    ),
                    options=SubscriptionRenewalOptionsCreate.for_successful_payment(),
                ),
                ReadsFixtures.read_json_fixture("config/subscription_renewal_success"),
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_renewal_success"),
            ),
            (
                SimulationScenarioType.SubscriptionRenewal,
                SubscriptionRenewalConfigCreate(
                    entities=SubscriptionRenewalEntitiesCreate(),
                ),
                {
                    "subscription_renewal": {
                        "entities": {},
                    }
                },
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_renewal_success"),
            ),
            (
                SimulationScenarioType.SubscriptionRenewal,
                SubscriptionRenewalConfigCreate(
                    entities=SubscriptionRenewalEntitiesCreate(
                        subscription_id="sub_01h04vsc0qhwtsbsxh3422wjs4",
                    ),
                    options=SubscriptionRenewalOptionsCreate.for_failed_payment(
                        dunning_exhausted_action=DunningExhaustedAction.SubscriptionCanceled,
                    ),
                ),
                ReadsFixtures.read_json_fixture("config/subscription_renewal_failed"),
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_renewal_failed"),
            ),
            (
                SimulationScenarioType.SubscriptionRenewal,
                SubscriptionRenewalConfigCreate(
                    entities=SubscriptionRenewalEntitiesCreate(
                        subscription_id="sub_01h04vsc0qhwtsbsxh3422wjs4",
                    ),
                    options=SubscriptionRenewalOptionsCreate.for_recovered_updated_payment_method(),
                ),
                ReadsFixtures.read_json_fixture("config/subscription_renewal_recovered"),
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_renewal_recovered"),
            ),
            (
                SimulationScenarioType.SubscriptionRenewal,
                SubscriptionRenewalConfigCreate(
                    entities=SubscriptionRenewalEntitiesCreate(
                        subscription_id="sub_01h04vsc0qhwtsbsxh3422wjs4",
                    ),
                    options=SubscriptionRenewalOptionsCreate.for_recovered_existing_payment_method(),
                ),
                ReadsFixtures.read_json_fixture("config/subscription_renewal_recovered_existing"),
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_renewal_recovered_existing"),
            ),
            (
                SimulationScenarioType.SubscriptionResume,
                SubscriptionResumeConfigCreate(
                    entities=SubscriptionResumeEntitiesCreate(
                        subscription_id="sub_01h04vsc0qhwtsbsxh3422wjs4",
                    ),
                    options=SubscriptionResumeOptionsCreate.for_successful_payment(),
                ),
                ReadsFixtures.read_json_fixture("config/subscription_resume_success"),
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_resume_success"),
            ),
            (
                SimulationScenarioType.SubscriptionResume,
                SubscriptionResumeConfigCreate(
                    entities=SubscriptionResumeEntitiesCreate(),
                ),
                {
                    "subscription_resume": {
                        "entities": {},
                    }
                },
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_resume_success"),
            ),
            (
                SimulationScenarioType.SubscriptionResume,
                SubscriptionResumeConfigCreate(
                    entities=SubscriptionResumeEntitiesCreate(
                        subscription_id="sub_01h04vsc0qhwtsbsxh3422wjs4",
                    ),
                    options=SubscriptionResumeOptionsCreate.for_failed_payment(
                        dunning_exhausted_action=DunningExhaustedAction.SubscriptionPaused,
                    ),
                ),
                ReadsFixtures.read_json_fixture("config/subscription_resume_failed"),
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_resume_failed"),
            ),
            (
                SimulationScenarioType.SubscriptionResume,
                SubscriptionResumeConfigCreate(
                    entities=SubscriptionResumeEntitiesCreate(
                        subscription_id="sub_01h04vsc0qhwtsbsxh3422wjs4",
                    ),
                    options=SubscriptionResumeOptionsCreate.for_recovered_updated_payment_method(),
                ),
                ReadsFixtures.read_json_fixture("config/subscription_resume_recovered"),
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_resume_recovered"),
            ),
            (
                SimulationScenarioType.SubscriptionResume,
                SubscriptionResumeConfigCreate(
                    entities=SubscriptionResumeEntitiesCreate(
                        subscription_id="sub_01h04vsc0qhwtsbsxh3422wjs4",
                    ),
                    options=SubscriptionResumeOptionsCreate.for_recovered_existing_payment_method(),
                ),
                ReadsFixtures.read_json_fixture("config/subscription_resume_recovered_existing"),
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_resume_recovered_existing"),
            ),
            (
                SimulationScenarioType.SubscriptionPause,
                SubscriptionPauseConfigCreate(
                    entities=SubscriptionPauseEntitiesCreate(),
                    options=SubscriptionPauseOptionsCreate(),
                ),
                {
                    "subscription_pause": {
                        "entities": {},
                        "options": {},
                    }
                },
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_pause"),
            ),
            (
                SimulationScenarioType.SubscriptionPause,
                SubscriptionPauseConfigCreate(
                    entities=SubscriptionPauseEntitiesCreate(
                        subscription_id="sub_01h04vsc0qhwtsbsxh3422wjs4",
                    ),
                    options=SubscriptionPauseOptionsCreate(
                        effective_from=EffectiveFrom.NextBillingPeriod,
                        has_past_due_transaction=False,
                    ),
                ),
                ReadsFixtures.read_json_fixture("config/subscription_pause"),
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_pause"),
            ),
            (
                SimulationScenarioType.SubscriptionCancellation,
                SubscriptionCancellationConfigCreate(
                    entities=SubscriptionCancellationEntitiesCreate(),
                    options=SubscriptionCancellationOptionsCreate(),
                ),
                {
                    "subscription_cancellation": {
                        "entities": {},
                        "options": {},
                    }
                },
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_cancel"),
            ),
            (
                SimulationScenarioType.SubscriptionCancellation,
                SubscriptionCancellationConfigCreate(
                    entities=SubscriptionCancellationEntitiesCreate(
                        subscription_id="sub_01h04vsc0qhwtsbsxh3422wjs4",
                    ),
                    options=SubscriptionCancellationOptionsCreate(
                        effective_from=EffectiveFrom.NextBillingPeriod,
                        has_past_due_transaction=False,
                    ),
                ),
                ReadsFixtures.read_json_fixture("config/subscription_cancel"),
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_cancel"),
            ),
        ],
        ids=[
            "Subscription creation simulation - transaction ID and new customer",
            "Subscription creation simulation - items and new customer",
            "Subscription creation simulation - matching customer",
            "Subscription creation simulation - prefilled customer",
            "Subscription creation simulation - minimal",
            "Subscription renewal simulation with success outcome",
            "Subscription renewal simulation with success outcome - minimal",
            "Subscription renewal simulation with failed outcome",
            "Subscription renewal simulation with recovered updated payment method",
            "Subscription renewal simulation with recovered existing payment method",
            "Subscription resume simulation with success outcome",
            "Subscription resume simulation with success outcome - minimal",
            "Subscription resume simulation with failed outcome",
            "Subscription resume simulation with recovered updated payment method",
            "Subscription resume simulation with recovered existing payment method",
            "Subscription pause simulation",
            "Subscription pause simulation - minimal",
            "Subscription cancellation simulation",
            "Subscription cancellation simulation - minimal",
        ],
    )
    def test_create_simulation_uses_expected_config(
        self,
        test_client,
        mock_requests,
        type: SimulationScenarioType,
        config,
        expected_request_config,
        expected_response_body,
    ):
        operation = CreateSimulation(
            notification_setting_id="ntfset_01j82d983j814ypzx7m1fw2jpz",
            type=type,
            name="Scenario Create",
            config=config,
        )

        expected_request_body = dumps(
            {
                "name": "Scenario Create",
                "type": type.value,
                "notification_setting_id": "ntfset_01j82d983j814ypzx7m1fw2jpz",
                "config": expected_request_config,
            }
        )

        expected_url = f"{test_client.base_url}/simulations"
        mock_requests.post(expected_url, status_code=201, text=expected_response_body)

        response = test_client.client.simulations.create(operation)
        response_json = test_client.client.simulations.response.json()
        request_json = test_client.client.payload
        last_request = mock_requests.last_request

        assert isinstance(response, Simulation)
        assert last_request is not None
        assert last_request.method == "POST"
        assert test_client.client.status_code == 201
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert loads(request_json) == loads(
            expected_request_body
        ), "The request JSON doesn't match the expected fixture JSON"
        assert response_json == loads(
            str(expected_response_body)
        ), "The response JSON doesn't match the expected fixture JSON"
        assert loads(PayloadEncoder().encode(response)) == loads(expected_response_body)["data"]

    @mark.parametrize(
        "type, config, expected_request_config, expected_response_body",
        [
            (
                SimulationScenarioType.SubscriptionCreation,
                SubscriptionCreationConfigCreate(
                    entities=SubscriptionCreationEntitiesCreate(
                        customer_id="ctm_01h04vsc0qhwtsbsxh3422wjs4",
                        address_id="add_01h04vsc0qhwtsbsxh3422wjs4",
                        business_id="biz_01h04vsc0qhwtsbsxh3422wjs4",
                        payment_method_id="paymtd_01h04vsc0qhwtsbsxh3422wjs4",
                        discount_id="dsc_01h04vsc0qhwtsbsxh3422wjs4",
                        transaction_id="txn_01h04vsc0qhwtsbsxh3422wjs4",
                    ),
                    options=SubscriptionCreationOptionsCreate(
                        customer_simulated_as=CustomerSimulatedAs.New,
                        business_simulated_as=BusinessSimulatedAs.New,
                        discount_simulated_as=DiscountSimulatedAs.NotProvided,
                    ),
                ),
                ReadsFixtures.read_json_fixture("config/subscription_creation_txn_id"),
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_subscription_creation_txn_id"),
            ),
            (
                SimulationScenarioType.SubscriptionCreation,
                SubscriptionCreationConfigCreate(
                    entities=SubscriptionCreationEntitiesCreate(
                        customer_id="ctm_01h04vsc0qhwtsbsxh3422wjs4",
                        address_id="add_01h04vsc0qhwtsbsxh3422wjs4",
                        business_id="biz_01h04vsc0qhwtsbsxh3422wjs4",
                        payment_method_id="paymtd_01h04vsc0qhwtsbsxh3422wjs4",
                        discount_id="dsc_01h04vsc0qhwtsbsxh3422wjs4",
                        items=[
                            SubscriptionCreationItemCreate(
                                price_id="pri_01h04vsc0qhwtsbsxh3422wjs4",
                                quantity=1,
                            ),
                        ],
                    ),
                    options=SubscriptionCreationOptionsCreate(
                        customer_simulated_as=CustomerSimulatedAs.New,
                        business_simulated_as=BusinessSimulatedAs.New,
                        discount_simulated_as=DiscountSimulatedAs.NotProvided,
                    ),
                ),
                ReadsFixtures.read_json_fixture("config/subscription_creation_new_customer"),
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_subscription_creation"),
            ),
            (
                SimulationScenarioType.SubscriptionCreation,
                SubscriptionCreationConfigCreate(
                    entities=SubscriptionCreationEntitiesCreate(
                        customer_id="ctm_01h04vsc0qhwtsbsxh3422wjs4",
                        address_id="add_01h04vsc0qhwtsbsxh3422wjs4",
                        business_id="biz_01h04vsc0qhwtsbsxh3422wjs4",
                        payment_method_id="paymtd_01h04vsc0qhwtsbsxh3422wjs4",
                        discount_id="dsc_01h04vsc0qhwtsbsxh3422wjs4",
                        items=[
                            SubscriptionCreationItemCreate(
                                price_id="pri_01h04vsc0qhwtsbsxh3422wjs4",
                                quantity=1,
                            ),
                        ],
                    ),
                    options=SubscriptionCreationOptionsCreate(
                        customer_simulated_as=CustomerSimulatedAs.ExistingEmailMatched,
                        business_simulated_as=BusinessSimulatedAs.NotProvided,
                        discount_simulated_as=DiscountSimulatedAs.EnteredByCustomer,
                    ),
                ),
                ReadsFixtures.read_json_fixture("config/subscription_creation_matching_customer"),
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_subscription_creation"),
            ),
            (
                SimulationScenarioType.SubscriptionCreation,
                SubscriptionCreationConfigCreate(
                    entities=SubscriptionCreationEntitiesCreate(
                        customer_id="ctm_01h04vsc0qhwtsbsxh3422wjs4",
                        address_id="add_01h04vsc0qhwtsbsxh3422wjs4",
                        business_id="biz_01h04vsc0qhwtsbsxh3422wjs4",
                        payment_method_id="paymtd_01h04vsc0qhwtsbsxh3422wjs4",
                        discount_id="dsc_01h04vsc0qhwtsbsxh3422wjs4",
                        items=[
                            SubscriptionCreationItemCreate(
                                price_id="pri_01h04vsc0qhwtsbsxh3422wjs4",
                                quantity=1,
                            ),
                        ],
                    ),
                    options=SubscriptionCreationOptionsCreate(
                        customer_simulated_as=CustomerSimulatedAs.ExistingDetailsPrefilled,
                        business_simulated_as=BusinessSimulatedAs.ExistingDetailsPrefilled,
                        discount_simulated_as=DiscountSimulatedAs.NotProvided,
                    ),
                ),
                ReadsFixtures.read_json_fixture("config/subscription_creation_prefilled_customer"),
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_subscription_creation"),
            ),
            (
                SimulationScenarioType.SubscriptionCreation,
                SubscriptionCreationConfigCreate(
                    entities=SubscriptionCreationEntitiesCreate(),
                    options=SubscriptionCreationOptionsCreate(),
                ),
                {
                    "subscription_creation": {
                        "entities": {},
                        "options": {},
                    }
                },
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_subscription_creation"),
            ),
            (
                SimulationScenarioType.SubscriptionRenewal,
                SubscriptionRenewalConfigCreate(
                    entities=SubscriptionRenewalEntitiesCreate(
                        subscription_id="sub_01h04vsc0qhwtsbsxh3422wjs4",
                    ),
                    options=SubscriptionRenewalOptionsCreate.for_successful_payment(),
                ),
                ReadsFixtures.read_json_fixture("config/subscription_renewal_success"),
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_renewal_success"),
            ),
            (
                SimulationScenarioType.SubscriptionRenewal,
                SubscriptionRenewalConfigCreate(
                    entities=SubscriptionRenewalEntitiesCreate(),
                ),
                {
                    "subscription_renewal": {
                        "entities": {},
                    }
                },
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_renewal_success"),
            ),
            (
                SimulationScenarioType.SubscriptionRenewal,
                SubscriptionRenewalConfigCreate(
                    entities=SubscriptionRenewalEntitiesCreate(
                        subscription_id="sub_01h04vsc0qhwtsbsxh3422wjs4",
                    ),
                    options=SubscriptionRenewalOptionsCreate.for_failed_payment(
                        dunning_exhausted_action=DunningExhaustedAction.SubscriptionCanceled,
                    ),
                ),
                ReadsFixtures.read_json_fixture("config/subscription_renewal_failed"),
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_renewal_failed"),
            ),
            (
                SimulationScenarioType.SubscriptionRenewal,
                SubscriptionRenewalConfigCreate(
                    entities=SubscriptionRenewalEntitiesCreate(
                        subscription_id="sub_01h04vsc0qhwtsbsxh3422wjs4",
                    ),
                    options=SubscriptionRenewalOptionsCreate.for_recovered_updated_payment_method(),
                ),
                ReadsFixtures.read_json_fixture("config/subscription_renewal_recovered"),
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_renewal_recovered"),
            ),
            (
                SimulationScenarioType.SubscriptionRenewal,
                SubscriptionRenewalConfigCreate(
                    entities=SubscriptionRenewalEntitiesCreate(
                        subscription_id="sub_01h04vsc0qhwtsbsxh3422wjs4",
                    ),
                    options=SubscriptionRenewalOptionsCreate.for_recovered_existing_payment_method(),
                ),
                ReadsFixtures.read_json_fixture("config/subscription_renewal_recovered_existing"),
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_renewal_recovered_existing"),
            ),
            (
                SimulationScenarioType.SubscriptionResume,
                SubscriptionResumeConfigCreate(
                    entities=SubscriptionResumeEntitiesCreate(
                        subscription_id="sub_01h04vsc0qhwtsbsxh3422wjs4",
                    ),
                    options=SubscriptionResumeOptionsCreate.for_successful_payment(),
                ),
                ReadsFixtures.read_json_fixture("config/subscription_resume_success"),
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_resume_success"),
            ),
            (
                SimulationScenarioType.SubscriptionResume,
                SubscriptionResumeConfigCreate(
                    entities=SubscriptionResumeEntitiesCreate(),
                ),
                {
                    "subscription_resume": {
                        "entities": {},
                    }
                },
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_resume_success"),
            ),
            (
                SimulationScenarioType.SubscriptionResume,
                SubscriptionResumeConfigCreate(
                    entities=SubscriptionResumeEntitiesCreate(
                        subscription_id="sub_01h04vsc0qhwtsbsxh3422wjs4",
                    ),
                    options=SubscriptionResumeOptionsCreate.for_failed_payment(
                        dunning_exhausted_action=DunningExhaustedAction.SubscriptionPaused,
                    ),
                ),
                ReadsFixtures.read_json_fixture("config/subscription_resume_failed"),
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_resume_failed"),
            ),
            (
                SimulationScenarioType.SubscriptionResume,
                SubscriptionResumeConfigCreate(
                    entities=SubscriptionResumeEntitiesCreate(
                        subscription_id="sub_01h04vsc0qhwtsbsxh3422wjs4",
                    ),
                    options=SubscriptionResumeOptionsCreate.for_recovered_updated_payment_method(),
                ),
                ReadsFixtures.read_json_fixture("config/subscription_resume_recovered"),
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_resume_recovered"),
            ),
            (
                SimulationScenarioType.SubscriptionResume,
                SubscriptionResumeConfigCreate(
                    entities=SubscriptionResumeEntitiesCreate(
                        subscription_id="sub_01h04vsc0qhwtsbsxh3422wjs4",
                    ),
                    options=SubscriptionResumeOptionsCreate.for_recovered_existing_payment_method(),
                ),
                ReadsFixtures.read_json_fixture("config/subscription_resume_recovered_existing"),
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_resume_recovered_existing"),
            ),
            (
                SimulationScenarioType.SubscriptionPause,
                SubscriptionPauseConfigCreate(
                    entities=SubscriptionPauseEntitiesCreate(),
                    options=SubscriptionPauseOptionsCreate(),
                ),
                {
                    "subscription_pause": {
                        "entities": {},
                        "options": {},
                    }
                },
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_pause"),
            ),
            (
                SimulationScenarioType.SubscriptionPause,
                SubscriptionPauseConfigCreate(
                    entities=SubscriptionPauseEntitiesCreate(
                        subscription_id="sub_01h04vsc0qhwtsbsxh3422wjs4",
                    ),
                    options=SubscriptionPauseOptionsCreate(
                        effective_from=EffectiveFrom.NextBillingPeriod,
                        has_past_due_transaction=False,
                    ),
                ),
                ReadsFixtures.read_json_fixture("config/subscription_pause"),
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_pause"),
            ),
            (
                SimulationScenarioType.SubscriptionCancellation,
                SubscriptionCancellationConfigCreate(
                    entities=SubscriptionCancellationEntitiesCreate(),
                    options=SubscriptionCancellationOptionsCreate(),
                ),
                {
                    "subscription_cancellation": {
                        "entities": {},
                        "options": {},
                    }
                },
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_cancel"),
            ),
            (
                SimulationScenarioType.SubscriptionCancellation,
                SubscriptionCancellationConfigCreate(
                    entities=SubscriptionCancellationEntitiesCreate(
                        subscription_id="sub_01h04vsc0qhwtsbsxh3422wjs4",
                    ),
                    options=SubscriptionCancellationOptionsCreate(
                        effective_from=EffectiveFrom.NextBillingPeriod,
                        has_past_due_transaction=False,
                    ),
                ),
                ReadsFixtures.read_json_fixture("config/subscription_cancel"),
                ReadsFixtures.read_raw_json_fixture("response/full_entity_config_cancel"),
            ),
        ],
        ids=[
            "Subscription creation simulation - transaction ID and new customer",
            "Subscription creation simulation - items and new customer",
            "Subscription creation simulation - matching customer",
            "Subscription creation simulation - prefilled customer",
            "Subscription creation simulation - minimal",
            "Subscription renewal simulation with success outcome",
            "Subscription renewal simulation with success outcome - minimal",
            "Subscription renewal simulation with failed outcome",
            "Subscription renewal simulation with recovered updated payment method",
            "Subscription renewal simulation with recovered existing payment method",
            "Subscription resume simulation with success outcome",
            "Subscription resume simulation with success outcome - minimal",
            "Subscription resume simulation with failed outcome",
            "Subscription resume simulation with recovered updated payment method",
            "Subscription resume simulation with recovered existing payment method",
            "Subscription pause simulation",
            "Subscription pause simulation - minimal",
            "Subscription cancellation simulation",
            "Subscription cancellation simulation - minimal",
        ],
    )
    def test_update_simulation_uses_expected_config(
        self,
        test_client,
        mock_requests,
        type: SimulationScenarioType,
        config,
        expected_request_config,
        expected_response_body,
    ):
        operation = CreateSimulation(
            notification_setting_id="ntfset_01j82d983j814ypzx7m1fw2jpz",
            type=type,
            name="Scenario Create",
            config=config,
        )

        expected_request_body = dumps(
            {
                "name": "Scenario Create",
                "type": type.value,
                "notification_setting_id": "ntfset_01j82d983j814ypzx7m1fw2jpz",
                "config": expected_request_config,
            }
        )

        expected_url = f"{test_client.base_url}/simulations/ntfsim_01j82g2mggsgjpb3mjg0xq6p5k"
        mock_requests.patch(expected_url, status_code=200, text=expected_response_body)

        response = test_client.client.simulations.update("ntfsim_01j82g2mggsgjpb3mjg0xq6p5k", operation)
        response_json = test_client.client.simulations.response.json()
        request_json = test_client.client.payload
        last_request = mock_requests.last_request

        assert isinstance(response, Simulation)
        assert last_request is not None
        assert last_request.method == "PATCH"
        assert test_client.client.status_code == 200
        assert (
            unquote(last_request.url) == expected_url
        ), "The URL does not match the expected URL, verify the query string is correct"
        assert loads(request_json) == loads(
            expected_request_body
        ), "The request JSON doesn't match the expected fixture JSON"
        assert response_json == loads(
            str(expected_response_body)
        ), "The response JSON doesn't match the expected fixture JSON"
        assert loads(PayloadEncoder().encode(response)) == loads(expected_response_body)["data"]
