from paddle_billing.EnumStringify import enum_stringify
from paddle_billing.HasParameters import HasParameters

from paddle_billing.Entities.Shared import CollectionMode
from paddle_billing.Entities.Subscriptions import SubscriptionStatus, SubscriptionScheduledChangeAction

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException

from paddle_billing.Resources.Shared.Operations import DateComparison, Pager


class ListSubscriptions(HasParameters):
    def __init__(
        self,
        pager: Pager | None = None,
        address_ids: list[str] | None = None,
        collection_mode: CollectionMode | None = None,
        customer_ids: list[str] | None = None,
        ids: list[str] | None = None,
        next_billed_at: DateComparison | None = None,
        price_ids: list[str] | None = None,
        scheduled_change_actions: list[SubscriptionScheduledChangeAction] | None = None,
        statuses: list[SubscriptionStatus] | None = None,
    ):
        self.pager = pager
        self.collection_mode = collection_mode
        self.next_billed_at = next_billed_at
        self.address_ids = address_ids if address_ids is not None else []
        self.customer_ids = customer_ids if customer_ids is not None else []
        self.ids = ids if ids is not None else []
        self.price_ids = price_ids if price_ids is not None else []
        self.scheduled_change_actions = scheduled_change_actions if scheduled_change_actions is not None else []
        self.statuses = statuses if statuses is not None else []

        # Validation
        for field_name, field_value, field_type in [
            ("address_ids", self.address_ids, str),
            ("customer_ids", self.customer_ids, str),
            ("ids", self.ids, str),
            ("price_ids", self.price_ids, str),
            ("scheduled_change_actions", self.scheduled_change_actions, SubscriptionScheduledChangeAction),
            ("statuses", self.statuses, SubscriptionStatus),
        ]:
            invalid_items = [item for item in field_value if not isinstance(item, field_type)]
            if invalid_items:
                raise InvalidArgumentException.array_contains_invalid_types(
                    field_name, field_type.__name__, invalid_items
                )

    def get_parameters(self) -> dict[str, str]:
        parameters: dict[str, str | None] = self.pager.get_parameters() if self.pager else {}

        if self.next_billed_at is not None:
            parameters[f"next_billed_at{self.next_billed_at.comparator}"] = self.next_billed_at.formatted()

        parameters.update(
            {
                "address_id": ",".join(self.address_ids),
                "collection_mode": self.collection_mode.value if self.collection_mode else None,
                "customer_id": ",".join(self.customer_ids),
                "id": ",".join(self.ids),
                "price_id": ",".join(self.price_ids),
                "scheduled_change_action": ",".join(map(enum_stringify, self.scheduled_change_actions)),
                "status": ",".join(map(enum_stringify, self.statuses)),
            }
        )

        return {key: value for key, value in parameters.items() if value}
