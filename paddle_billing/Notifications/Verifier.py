from os import getenv
from time import time
from paddle_billing.Logger import get_logger as get_logger

from paddle_billing.Notifications.Secret import Secret as Secret
from paddle_billing.Notifications.PaddleSignature import PaddleSignature as PaddleSignature
from paddle_billing.Notifications.Requests import (
    BodyRequest as BodyRequest,
    ContentRequest as ContentRequest,
    DataRequest as DataRequest,
    Request as Request,
)


class Verifier:
    def __init__(self, maximum_variance: int | None = 5):
        """
        :param maximum_variance: Seconds a webhook's timestamp may differ from now. None or 0 disables time drift
                                 verification (NOT RECOMMENDED, protects against replayed webhooks)
        """
        self.__maximum_variance = maximum_variance
        self.log = get_logger()
        self.paddle_signature = PaddleSignature()

    @property
    def maximum_variance(self) -> int | None:
        return self.__maximum_variance

    def verify(
        self,
        request: Request | BodyRequest | ContentRequest | DataRequest,
        secrets: list[Secret] | Secret,
        verify_time_drift: bool = True,
    ) -> bool:
        """
        :param request:           The request object to verify
        :param secrets:           One or more Secrets to use for verifying the request
        :param verify_time_drift: Defaults to True. Set False to disable time drift verification (NOT RECOMMENDED, protects against replayed webhooks)
        :return:                  True on verification success, False on verification failure
        """
        self.log.info("Attempting to verify the authenticity of a request")

        if getenv("TEST_MODE") is not None:
            verify_time_drift = not bool(int(getenv("TEST_MODE", "0")))  # Intentional bool(int())

        signature_header = request.headers.get(PaddleSignature().HEADER, None)
        if not signature_header:
            self.log.warning(f"Unable to extract the '{PaddleSignature().HEADER}' header from the request")
            return False

        timestamp, signature = PaddleSignature.parse(signature_header)
        if verify_time_drift and self.maximum_variance is not None and self.maximum_variance > 0:
            now = time()
            if now > int(timestamp + self.maximum_variance):
                self.log.warning("Too much time has elapsed between the request and this process")
                return False
            if int(timestamp - self.maximum_variance) > now:
                self.log.warning("The request timestamp is too far in the future")
                return False

        raw_body = None
        if (body := getattr(request, "body", None)) is not None:
            raw_body = body.decode("utf-8")
        elif (content := getattr(request, "content", None)) is not None:
            raw_body = content.decode("utf-8")
        elif (data := getattr(request, "data", None)) is not None:
            raw_body = data.decode("utf-8")

        if not isinstance(raw_body, str):
            raise ValueError("raw_body is not instance of str.")

        return self.paddle_signature.verify(signature_header, raw_body, secrets)
