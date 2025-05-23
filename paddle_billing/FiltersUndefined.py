from paddle_billing.Undefined import Undefined
from typing import Any


class FiltersUndefined:
    @staticmethod
    def filter_undefined_values(input_dict) -> dict[str, Any]:
        """
        This method filters out values that are None from the given list
        """
        return {key: value for key, value in input_dict.items() if not isinstance(value, Undefined)}
