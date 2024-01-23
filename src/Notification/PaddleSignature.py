from src                        import log
from src.Notification.Secret    import Secret
from hmac                       import HMAC, compare_digest, new as hmac_new
from hashlib                    import sha256


class PaddleSignature:
    def __init__(self):
        """
        Verifies the integrity of a Paddle signature
        """


    @property
    def HEADER(self):  # noqa N802
        return 'Paddle-Signature'


    @staticmethod
    def parse(signature_header: str) -> tuple:
        """
        Parse the Paddle-Signature header to extract the timestamp and signature

        @param   signature_header:  The Paddle-Signature key=value from the webhook event's headers
        @return:                    A tuple containing (timestamp, signature)
        """
        timestamp, signature = signature_header.split(";")
        return timestamp.lstrip(f"ts="), signature.lstrip(f"h1=")


    @staticmethod
    def calculate_hmac(secret_key: str, data: bytes) -> HMAC:
        return hmac_new(secret_key.encode('utf-8'), data, sha256)


    @staticmethod
    def verify(signature_header: str, raw_body: str, secret_key: Secret) -> bool:
        """
        https://developer.paddle.com/webhooks/signature-verification
        Performs an integrity check on a Paddle webhook's signature

        @param signature_header:    The Paddle-Signature header
        @param raw_body:            Raw body of the webhook request
        @param secret_key:          Your Paddle secret key: https://developer.paddle.com/webhooks/signature-verification#get-secret-key
        @return:                    True on verification success, False on verification failure
        """
        log.info(f"Verifying Paddle signature integrity")

        timestamp, signature = PaddleSignature.parse(signature_header)
        new_body_to_verify   = f"{timestamp}:{raw_body}".encode('utf-8')
        generated_signature  = PaddleSignature.calculate_hmac(secret_key.secret_key, new_body_to_verify).hexdigest()

        integrity_result = compare_digest(generated_signature, signature)
        log.debug(f"Comparing received Paddle signature '{signature}' to our calculated signature: '{generated_signature}'")
        log.info(f"Paddle signature integrity {'passed' if integrity_result else 'failed'}")

        return integrity_result
