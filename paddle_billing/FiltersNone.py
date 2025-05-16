from typing import Any


class FiltersNone:
    @staticmethod
    def filter_none_values(input_dict) -> dict[str, Any]:
        """
        This method filters out values that are None from the given list
        """
        return {key: value for key, value in input_dict.items() if value is not None}
