from pytest import raises

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException
from paddle_billing.Resources.Simulations.Operations.Config.Subscription.Creation.SubscriptionCreationEntitiesCreate import (
    SubscriptionCreationEntitiesCreate,
)


class TestSubscriptionCreationEntitiesCreate:
    def test_raises_invalid_argument_exception_for_incompatible_arguments(self):
        with raises(InvalidArgumentException) as exception_info:
            SubscriptionCreationEntitiesCreate(
                transaction_id="txn_01h04vsc0qhwtsbsxh3422wjs4",
                items=[],
            )

        assert str(exception_info.value) == "'transaction_id' is not compatible with 'items'"
