from datetime import datetime

from pytest import raises

from paddle_billing.Entities.Shared import ActionSource, ActorType

from paddle_billing.Entities.Subscriptions.History import SubscriptionHistoryAction, SubscriptionHistoryReason

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException

from paddle_billing.Resources.Shared.Operations import Comparator, DateComparison, Pager
from paddle_billing.Resources.Subscriptions.Operations import ListSubscriptionHistory


class TestListSubscriptionHistory:
    def test_returns_no_parameters_by_default(self):
        operation = ListSubscriptionHistory()

        assert operation.get_parameters() == {}

    def test_serializes_pager_parameters(self):
        operation = ListSubscriptionHistory(pager=Pager())

        assert operation.get_parameters() == {"order_by": "id[asc]", "per_page": 50}

    def test_serializes_a_single_action(self):
        operation = ListSubscriptionHistory(actions=[SubscriptionHistoryAction.SubscriptionRenewed])

        assert operation.get_parameters() == {"action": "subscription_renewed"}

    def test_serializes_multiple_actions_as_a_comma_separated_list(self):
        operation = ListSubscriptionHistory(
            actions=[
                SubscriptionHistoryAction.SubscriptionRenewed,
                SubscriptionHistoryAction.SubscriptionPaused,
            ]
        )

        assert operation.get_parameters() == {"action": "subscription_renewed,subscription_paused"}

    def test_serializes_sources(self):
        operation = ListSubscriptionHistory(sources=[ActionSource.Api, ActionSource.Dashboard])

        assert operation.get_parameters() == {"source": "api,dashboard"}

    def test_serializes_actor_types(self):
        operation = ListSubscriptionHistory(actor_types=[ActorType.ApiKey])

        assert operation.get_parameters() == {"actor_type": "api_key"}

    def test_serializes_actor_ids(self):
        operation = ListSubscriptionHistory(actor_ids=["apikey_01h8441jn5pcwrfhwh78jqt8hl", "usr_01h8441jn5"])

        assert operation.get_parameters() == {"actor_id": "apikey_01h8441jn5pcwrfhwh78jqt8hl,usr_01h8441jn5"}

    def test_serializes_reasons(self):
        operation = ListSubscriptionHistory(reasons=[SubscriptionHistoryReason.CustomerRequest])

        assert operation.get_parameters() == {"reason": "customer_request"}

    def test_serializes_occurred_at_with_a_comparator(self):
        operation = ListSubscriptionHistory(occurred_at=DateComparison(datetime(2026, 6, 1, 0, 0, 0), Comparator.GTE))

        assert operation.get_parameters() == {"occurred_at[GTE]": "2026-06-01T00:00:00.000000Z"}

    def test_serializes_occurred_at_without_a_comparator(self):
        operation = ListSubscriptionHistory(occurred_at=DateComparison(datetime(2026, 6, 1, 0, 0, 0)))

        assert operation.get_parameters() == {"occurred_at": "2026-06-01T00:00:00.000000Z"}

    def test_raises_invalid_argument_exception_for_invalid_actions(self):
        with raises(InvalidArgumentException) as exception_info:
            ListSubscriptionHistory(actions=["subscription_renewed"])

        assert (
            str(exception_info.value)
            == "Expected 'actions' to only contain type 'SubscriptionHistoryAction' ('str' given)"
        )

    def test_raises_invalid_argument_exception_for_invalid_sources(self):
        with raises(InvalidArgumentException) as exception_info:
            ListSubscriptionHistory(sources=[1])

        assert str(exception_info.value) == "Expected 'sources' to only contain type 'ActionSource' ('int' given)"

    def test_raises_invalid_argument_exception_for_invalid_actor_types(self):
        with raises(InvalidArgumentException) as exception_info:
            ListSubscriptionHistory(actor_types=[1])

        assert str(exception_info.value) == "Expected 'actor_types' to only contain type 'ActorType' ('int' given)"

    def test_raises_invalid_argument_exception_for_invalid_actor_ids(self):
        with raises(InvalidArgumentException) as exception_info:
            ListSubscriptionHistory(actor_ids=[1, datetime.now()])

        assert str(exception_info.value) == "Expected 'actor_ids' to only contain type 'str' ('int', 'datetime' given)"

    def test_raises_invalid_argument_exception_for_invalid_reasons(self):
        with raises(InvalidArgumentException) as exception_info:
            ListSubscriptionHistory(reasons=[1])

        assert (
            str(exception_info.value)
            == "Expected 'reasons' to only contain type 'SubscriptionHistoryReason' ('int' given)"
        )
