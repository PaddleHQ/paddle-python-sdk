from paddle_billing.Exceptions.SdkException import SdkException


class InvalidArgumentException(SdkException):
    @staticmethod
    def array_is_empty(field):
        message = f"'{field}' cannot be empty"
        return InvalidArgumentException(message)

    @staticmethod
    def array_contains_invalid_types(field, expected_types: list[str] | str, given: list = None):
        if isinstance(expected_types, list):
            expected_types_str = "', '".join(expected_types)
            message = f"Expected '{field}' to only contain types '{expected_types_str}'"
        else:
            message = f"Expected '{field}' to only contain type '{expected_types}'"

        if given is not None:
            invalid_type_list = "', '".join(map(lambda x: type(x).__name__, given))
            message += f" ('{invalid_type_list}' given)"

        return InvalidArgumentException(message)
