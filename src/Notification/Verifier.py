from time               import time
from src                import log
from src.Notification   import PaddleSignature, Secret
import requests


class Verifier:
    def __init__(self, maximum_variance: int = 5):
        """"""
        self.__maximum_variance = maximum_variance


    @property
    def maximum_variance(self) -> int:
        return self.__maximum_variance


    def verify(self, request: requests, secret_key: Secret):
        """

        :param request:
        :param secret_key:
        :return:            True on verification success, False on verification failure
        """
        log.info(f"Attempting to verify the authenticity of a request")

        signature_header = request.headers.get(PaddleSignature.HEADER, None)
        if not signature_header:
            log.critical(f"Unable to extract the '{PaddleSignature.HEADER}' header from the request")
            return False

        timestamp, signature = PaddleSignature.parse(signature_header)
        if self.maximum_variance > 0 and time() > int(timestamp + self.maximum_variance):
            log.critical(f"Too much time has elapse between the request and this process")
            return False

        raw_body = request.body.decode('utf-8')

        return PaddleSignature.verify(signature_header, raw_body, secret_key)
