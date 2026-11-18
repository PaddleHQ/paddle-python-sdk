from paddle_billing.FiltersNone import FiltersNone
from paddle_billing.HasParameters import HasParameters

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException

from paddle_billing.Resources.Shared.Operations import Pager


class ListApiKeyRotations(HasParameters):
    def __init__(
        self,
        pager: Pager | None = None,
        ids: list[str] | None = None,
    ):
        self.pager = pager
        self.ids = ids if ids is not None else []

        invalid_items = [item for item in self.ids if not isinstance(item, str)]
        if invalid_items:
            raise InvalidArgumentException.array_contains_invalid_types("ids", str.__name__, invalid_items)

    def get_parameters(self) -> dict[str, str]:
        parameters = {}
        if self.pager:
            # The list rotations endpoint doesn't accept order_by.
            parameters.update(
                FiltersNone.filter_none_values({"after": self.pager.after, "per_page": self.pager.per_page})
            )
        if self.ids:
            parameters["id"] = ",".join(self.ids)

        return parameters
