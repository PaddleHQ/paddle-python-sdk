from paddle_billing.Exceptions.SdkException import SdkException


class MalformedResponse(SdkException):
    def __init__(self, e):
        super().__init__(str(e))
        self.original_exception = e
