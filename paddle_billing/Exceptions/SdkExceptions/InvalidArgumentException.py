from paddle_billing.Exceptions.SdkException import SdkException


class InvalidArgumentException(SdkException):
    @staticmethod
    def array_contains_invalid_types(field, expected_type, given):
        message = f"Expected '{field}' to only contain only type/s '{expected_type}', '{given}' given"
        return InvalidArgumentException(message)
