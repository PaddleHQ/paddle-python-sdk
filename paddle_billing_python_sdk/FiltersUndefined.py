from paddle_billing_python_sdk.Undefined import Undefined


class FiltersUndefined:
    def filter_undefined(self, values):  # noqa PEP-484
        """
        This method filters out values that are instances of Undefined from the given list.
        """
        return [value for value in values if not isinstance(value, Undefined)]

