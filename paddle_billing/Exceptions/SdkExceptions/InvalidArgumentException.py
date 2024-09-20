from paddle_billing.Exceptions.SdkException import SdkException


class InvalidArgumentException(SdkException):
    @staticmethod
    def array_is_empty(field):
        message = f"'{field}' cannot be empty"
        return InvalidArgumentException(message)

    @staticmethod
    def array_contains_invalid_types(field, expected_type, given = None):
        message = f"Expected '{field}' to only contain only type/s '{expected_type}'"

        if given is not None:
            message += f", '{given}' given"

        return InvalidArgumentException(message)
