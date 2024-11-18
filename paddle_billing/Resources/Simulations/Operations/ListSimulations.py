from paddle_billing.EnumStringify import enum_stringify
from paddle_billing.HasParameters import HasParameters

from paddle_billing.Entities.Simulations import SimulationStatus

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException

from paddle_billing.Resources.Shared.Operations import Pager


class ListSimulations(HasParameters):
    def __init__(
        self,
        pager: Pager | None = None,
        notification_setting_ids: list[str] = None,
        ids: list[str] = None,
        statuses: list[SimulationStatus] = None,
    ):
        self.pager = pager
        self.ids = ids if ids is not None else []
        self.notification_setting_ids = notification_setting_ids if notification_setting_ids is not None else []
        self.statuses = statuses if statuses is not None else []

        # Validation
        for field_name, field_value, field_type in [
            ("notification_setting_ids", self.notification_setting_ids, str),
            ("ids", self.ids, str),
            ("statuses", self.statuses, SimulationStatus),
        ]:
            invalid_items = [item for item in field_value if not isinstance(item, field_type)]
            if invalid_items:
                raise InvalidArgumentException.array_contains_invalid_types(
                    field_name, field_type.__name__, invalid_items
                )

    def get_parameters(self) -> dict:
        parameters = {}
        if self.pager:
            parameters.update(self.pager.get_parameters())
        if self.ids:
            parameters["id"] = ",".join(self.ids)
        if self.notification_setting_ids:
            parameters["notification_setting_id"] = ",".join(self.notification_setting_ids)
        if self.statuses:
            parameters["status"] = ",".join(map(enum_stringify, self.statuses))

        return parameters
