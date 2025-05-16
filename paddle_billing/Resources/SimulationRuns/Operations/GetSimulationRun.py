from paddle_billing.EnumStringify import enum_stringify
from paddle_billing.HasParameters import HasParameters
from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException
from paddle_billing.Resources.SimulationRuns.Operations.SimulationRunInclude import SimulationRunInclude


class GetSimulationRun(HasParameters):
    def __init__(
        self,
        includes: list[SimulationRunInclude] | None = None,
    ):
        self.includes = includes if includes is not None else []

        # Validation
        for field_name, field_value, field_type in [
            ("includes", self.includes, SimulationRunInclude),
        ]:
            invalid_items = [item for item in field_value if not isinstance(item, field_type)]
            if invalid_items:
                raise InvalidArgumentException.array_contains_invalid_types(
                    field_name, field_type.__name__, invalid_items
                )

    def get_parameters(self) -> dict[str, str]:
        parameters = {}
        if self.includes:
            parameters["include"] = ",".join(map(enum_stringify, self.includes))

        return parameters
