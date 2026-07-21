from paddle_billing.EnumStringify import enum_stringify
from paddle_billing.HasParameters import HasParameters

from paddle_billing.Entities.Shared import ActionSource, ActorType
from paddle_billing.Entities.Subscriptions.History import SubscriptionHistoryAction, SubscriptionHistoryReason

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException

from paddle_billing.Resources.Shared.Operations import DateComparison, Pager


class ListSubscriptionHistory(HasParameters):
    def __init__(
        self,
        pager: Pager | None = None,
        actions: list[SubscriptionHistoryAction] | None = None,
        sources: list[ActionSource] | None = None,
        actor_types: list[ActorType] | None = None,
        actor_ids: list[str] | None = None,
        reasons: list[SubscriptionHistoryReason] | None = None,
        occurred_at: DateComparison | None = None,
    ):
        self.pager = pager
        self.occurred_at = occurred_at
        self.actions = actions if actions is not None else []
        self.sources = sources if sources is not None else []
        self.actor_types = actor_types if actor_types is not None else []
        self.actor_ids = actor_ids if actor_ids is not None else []
        self.reasons = reasons if reasons is not None else []

        # Validation
        for field_name, field_value, field_type in [
            ("actions", self.actions, SubscriptionHistoryAction),
            ("sources", self.sources, ActionSource),
            ("actor_types", self.actor_types, ActorType),
            ("actor_ids", self.actor_ids, str),
            ("reasons", self.reasons, SubscriptionHistoryReason),
        ]:
            invalid_items = [item for item in field_value if not isinstance(item, field_type)]
            if invalid_items:
                raise InvalidArgumentException.array_contains_invalid_types(
                    field_name, field_type.__name__, invalid_items
                )

    def get_parameters(self) -> dict[str, str]:
        parameters: dict[str, str | None] = self.pager.get_parameters() if self.pager else {}

        if self.occurred_at is not None:
            parameters[f"occurred_at{self.occurred_at.comparator}"] = self.occurred_at.formatted()

        parameters.update(
            {
                "action": ",".join(map(enum_stringify, self.actions)),
                "source": ",".join(map(enum_stringify, self.sources)),
                "actor_type": ",".join(map(enum_stringify, self.actor_types)),
                "actor_id": ",".join(self.actor_ids),
                "reason": ",".join(map(enum_stringify, self.reasons)),
            }
        )

        return {key: value for key, value in parameters.items() if value}
