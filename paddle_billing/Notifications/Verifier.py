from os import getenv
from time import time

from paddle_billing.Logger import get_logger

from paddle_billing.Notifications.Requests.Request import Request
from paddle_billing.Notifications.Secret import Secret
from paddle_billing.Notifications.PaddleSignature import PaddleSignature


class Verifier:
    def __init__(self, maximum_variance: int | None = 5):
        """"""
        self.__maximum_variance = maximum_variance
        self.log = get_logger()
        self.paddle_signature = PaddleSignature()

    @property
    def maximum_variance(self) -> int:
        return self.__maximum_variance

    def verify(self, request: Request, secrets: list[Secret] | Secret, verify_time_drift=True):
        """
        :param request:           The request object to verify
        :param secrets:           One or more Secrets to use for verifying the request
        :param verify_time_drift: Defaults to True. Set False to disable time drift verification (NOT RECOMMENDED, counters MITM attacks)
        :return:                  True on verification success, False on verification failure
        """
        self.log.info("Attempting to verify the authenticity of a request")

        if getenv("TEST_MODE") is not None:
            verify_time_drift = not bool(int(getenv("TEST_MODE", "0")))  # Intentional bool(int())

        signature_header = request.headers.get(PaddleSignature().HEADER, None)
        if not signature_header:
            self.log.critical(f"Unable to extract the '{PaddleSignature().HEADER}' header from the request")
            return False

        timestamp, signature = PaddleSignature.parse(signature_header)
        if verify_time_drift and self.maximum_variance > 0 and time() > int(timestamp + self.maximum_variance):
            self.log.critical("Too much time has elapsed between the request and this process")
            return False

        raw_body = None
        if hasattr(request, "body"):
            raw_body = request.body.decode("utf-8")
        elif hasattr(request, "content"):
            raw_body = request.content.decode("utf-8")
        elif hasattr(request, "data"):
            raw_body = request.data.decode("utf-8")

        return self.paddle_signature.verify(signature_header, raw_body, secrets)
