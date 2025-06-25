from pytest import raises

from paddle_billing.Entities.Simulation import SimulationScenarioType
from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException
from paddle_billing.Resources.Simulations.SimulationsClient import CreateSimulation
from tests.Functional.Resources.Simulations.test_SimulationsClient import SubscriptionCreationConfigCreate


class TestCreateSimulation:
    def test_raises_invalid_argument_exception_for_incompatible_arguments(self):
        with raises(InvalidArgumentException) as exception_info:
            CreateSimulation(
                notification_setting_id="ntfset_01j82d983j814ypzx7m1fw2jpz",
                type=SimulationScenarioType.SubscriptionCancellation,
                name="Some simulation",
                config=SubscriptionCreationConfigCreate(),
            )

        assert str(exception_info.value) == "'config' is not compatible with 'type'"
