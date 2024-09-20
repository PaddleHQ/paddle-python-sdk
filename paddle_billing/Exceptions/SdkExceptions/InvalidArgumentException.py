from paddle_billing.Exceptions.SdkException import SdkException


class InvalidArgumentException(SdkException):
    @staticmethod
    def array_is_empty(field):
        message = f"'{field}' cannot be empty"
        return InvalidArgumentException(message)

    @staticmethod
    def array_contains_invalid_types(field, expected_type):
        message = f"Expected '{field}' to only contain only type/s '{expected_type}'"
        return InvalidArgumentException(message)
