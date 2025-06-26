from paddle_billing.EnumStringify import enum_stringify
from paddle_billing.HasParameters import HasParameters

from paddle_billing.Entities.Shared import Status
from paddle_billing.Entities.Discounts.DiscountMode import DiscountMode

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException

from paddle_billing.Resources.Discounts.Operations.DiscountInclude import DiscountInclude
from paddle_billing.Resources.Shared.Operations import Pager


class ListDiscounts(HasParameters):
    def __init__(
        self,
        pager: Pager | None = None,
        ids: list[str] | None = None,
        statuses: list[Status] | None = None,
        codes: list[str] | None = None,
        discount_group_ids: list[str] | None = None,
        mode: DiscountMode | None = None,
        includes: list[DiscountInclude] | None = None,
    ):
        self.pager = pager
        self.ids = ids if ids is not None else []
        self.statuses = statuses if statuses is not None else []
        self.codes = codes if codes is not None else []
        self.discount_group_ids = discount_group_ids if discount_group_ids is not None else []
        self.mode = mode
        self.includes = includes if includes is not None else []

        # Validation
        for field_name, field_value, field_type in [
            ("ids", self.ids, str),
            ("statuses", self.statuses, Status),
            ("codes", self.codes, str),
            ("discount_group_ids", self.discount_group_ids, str),
            ("includes", self.includes, DiscountInclude),
        ]:
            invalid_items = [item for item in field_value if not isinstance(item, field_type)]
            if invalid_items:
                raise InvalidArgumentException.array_contains_invalid_types(
                    field_name, field_type.__name__, invalid_items
                )

    def get_parameters(self) -> dict[str, str]:
        parameters = {}
        if self.pager:
            parameters.update(self.pager.get_parameters())
        if self.ids:
            parameters["id"] = ",".join(self.ids)
        if self.statuses:
            parameters["status"] = ",".join(map(enum_stringify, self.statuses))
        if self.codes:
            parameters["code"] = ",".join(self.codes)
        if self.discount_group_ids:
            parameters["discount_group_id"] = ",".join(self.discount_group_ids)
        if self.mode:
            parameters["mode"] = self.mode.value
        if self.includes:
            parameters["include"] = ",".join(map(enum_stringify, self.includes))

        return parameters
