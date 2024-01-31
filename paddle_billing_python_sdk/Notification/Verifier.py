import requests

from time import time

from paddle_billing_python_sdk.Logger       import get_logger
from paddle_billing_python_sdk.Notification import PaddleSignature, Secret


class Verifier:
    def __init__(self, maximum_variance: int = 5):
        """"""
        self.__maximum_variance = maximum_variance
        self.log = get_logger()
        self.paddle_signature = PaddleSignature()


    @property
    def maximum_variance(self) -> int:
        return self.__maximum_variance


    def verify(self, request: requests, secrets: list[Secret] | Secret):
        """
        @param request: The request object to verify
        @param secrets: One or more Secrets to use for verifying the request
        @return:        True on verification success, False on verification failure
        """
        self.log.info(f"Attempting to verify the authenticity of a request")

        signature_header = request.headers.get(PaddleSignature().HEADER, None)
        if not signature_header:
            self.log.critical(f"Unable to extract the '{PaddleSignature().HEADER}' header from the request")
            return False

        timestamp, signature = PaddleSignature.parse(signature_header)
        if self.maximum_variance > 0 and time() > int(timestamp + self.maximum_variance):
            self.log.critical(f"Too much time has elapsed between the request and this process")
            return False

        raw_body = request.body.decode('utf-8') if hasattr(request, 'body') else request.content.decode('utf-8')

        return self.paddle_signature.verify(signature_header, raw_body, secrets)
