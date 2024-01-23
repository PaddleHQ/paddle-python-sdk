from src        import log
from hmac       import HMAC, compare_digest, new as hmac_new
from hashlib    import sha256


class PaddleSignature:
    HEADER:         str = 'Paddle-Signature'
    TIMESTAMP:      str = 'ts'
    HASH:           str = 'h1'
    HASH_ALGORITHM: str = sha256
    ENCODING:       str = 'utf-8'

    def __init__(self):
        """
        Verifies the integrity of a Paddle signature
        """


    def parse_headers_for_paddle_signature(self, headers) -> str:
        """
        TODO
        :param headers:
        :return:
        """
        pass


    def parse_paddle_signature_header(self, signature_header: str) -> tuple:
        """
        Parse the Paddle-Signature header to extract the timestamp and signature

        @param   signature_header:  The Paddle-Signature key=value from the webhook event's headers
        @return:                    A tuple containing (timestamp, signature)
        """
        timestamp, signature = signature_header.split(";")
        return timestamp.lstrip(f"{self.TIMESTAMP}="), signature.lstrip(f"{self.HASH}=")


    def calculate_hmac(self, secret_key: str, data: bytes) -> HMAC:
        return hmac_new(secret_key.encode(self.ENCODING), data, self.HASH_ALGORITHM)


    def verify(self, signature_header: str, raw_body: str, secret_key: str) -> bool:
        """
        https://developer.paddle.com/webhooks/signature-verification
        Performs an integrity check on a Paddle webhook's signature

        @param signature_header:    The Paddle-Signature header
        @param raw_body:            Raw body of the webhook request
        @param secret_key:          Our Paddle secret key
        @return:                    True on verification success, False on verification failure
        """
        log.info(f"Verifying Paddle signature integrity")

        timestamp, signature = self.parse_paddle_signature_header(signature_header)
        new_body_to_verify   = f"{timestamp}:{raw_body}".encode(self.ENCODING)
        generated_signature  = self.calculate_hmac(secret_key, new_body_to_verify).hexdigest()

        integrity_result = compare_digest(generated_signature, signature)
        log.info(f"Paddle signature integrity {'passed' if integrity_result else 'failed'}")

        return integrity_result
