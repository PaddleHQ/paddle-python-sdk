from paddle_billing.Exceptions.SdkException import SdkException


class InvalidArgumentException(SdkException):
    @staticmethod
    def array_is_empty(field):
        message = f"'{field}' cannot be empty"
        return InvalidArgumentException(message)

    @staticmethod
    def array_contains_invalid_types(field, expected_type, given: list = None):
        message = f"Expected '{field}' to only contain type '{expected_type}'"

        if given is not None:
            invalidTypeList = "', '".join(map(lambda x: type(x).__name__, given))
            message += f" ('{invalidTypeList}' given)"

        return InvalidArgumentException(message)
